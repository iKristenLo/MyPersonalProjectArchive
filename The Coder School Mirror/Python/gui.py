import sys, ctypes
import hijackchecker
from flask import Flask, render_template, jsonify, request, redirect, url_for
import os
import subprocess
import shutil
import json
import sqlcipher3 as sqlite
from win32crypt import CryptProtectData, CryptUnprotectData
import win32crypt
import sqlite3
import win32security
import datetime
import win32api
import ntsecuritycon


def dbpath():
    appdata = os.getenv("APPDATA")
    appfolder = os.path.join(appdata,"Hijackapp")
    os.makedirs(appfolder,exist_ok=True)
    return os.path.join(appfolder,"excludes.db")

def lockperms(path):
    sd = win32security.GetFileSecurity(path,win32security.DACL_SECURITY_INFORMATION)
    dacl = win32security.ACL()
    uservar = win32api.GetUserNameEx(win32api.NameSamCompatible)
    usersid,_,_ = win32security.LookupAccountName(None,uservar)
    dacl.AddAccessAllowedAce(win32security.ACL_REVISION,ntsecuritycon.FILE_ALL_ACCESS,usersid)
    systemsid,_,_ = win32security.LookupAccountName(None,"SYSTEM")
    dacl.AddAccessAllowedAce(win32security.ACL_REVISION,ntsecuritycon.FILE_ALL_ACCESS,systemsid)
    sd.SetSecurityDescriptorDacl(1,dacl,0)
    win32security.SetFileSecurity(path,win32security.DACL_SECURITY_INFORMATION,sd)

def dbinit():
    db = dbpath()
    fileexist = os.path.exists(db)
    conn = sqlite3.connect(db)
    conn.execute("""
CREATE TABLE IF NOT EXISTS dbtable(
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 pathblob BLOB NOT NULL UNIQUE,
                 madetime TEXT NOT NULL);
""")
    conn.commit()
    conn.close()
    if not fileexist:
        lockperms(db)

def dataencrypt(text):
    data = win32crypt.CryptProtectData(
        text.encode("UTF-8"),
        None,
        None,
        None,
        None,
        0,
    )
    return data

def datadecode(blob):
    _,data = win32crypt.CryptUnprotectData(
        blob,
        None,
        None,
        None,
        0,
    )
    return data.decode("UTF-8")

def exclusionadd(path):
    dbinit()
    blob = dataencrypt(path)
    ts = datetime.datetime.utcnow().isoformat()+"Z"
    conconnect = sqlite3.connect(dbpath())
    conconnect.execute(
        "INSERT INTO dbtable (pathblob, madetime) VALUES (?,?);",(blob,ts)
    )
    conconnect.commit()
    conconnect.close()

def getexlusion():
    dbinit()
    conconnect = sqlite3.connect(dbpath())
    concursor = conconnect.execute("SELECT pathblob FROM dbtable;")
    roseblob = concursor.fetchall()
    conconnect.close()
    return [
        datadecode(row[0]) for row in roseblob
    ]

def excludecheck(e):
    for k in getexlusion():
        if e == k:
            return True
    return False

def removeexcludes(path):
    dbinit()
    conconnect = sqlite3.connect(dbpath())
    cursor = conconnect.cursor()
    cursor.execute("SELECT id,pathblob FROM dbtable;")
    rowdata = cursor.fetchall()
    bolhold = False
    for id,blob in rowdata:
        try:
            decodedata = datadecode(blob)
        except Exception:
            continue
        if decodedata == path:
            cursor.execute("DELETE FROM dbtable WHERE id = ?;",(id,))
            conconnect.commit()
            bolhold = True
            break
    conconnect.close()
    return bolhold
app = Flask("Hijackapp")
tempdir = "checktemp"
os.makedirs(tempdir, exist_ok=True)


@app.route("/Excludes",methods=["GET","POST"] )
def excludes():
    if request.method == "POST":
        path = request.form.get("path","").strip()
        action = request.form.get("action")
        if action == "add" and path and not excludecheck(path):
            exclusionadd(path)
        elif action == "remove" and path and excludecheck(path):
            removeexcludes(path)
        
        
        #if path:
        #    if not excludecheck(path):
        #     exclusionadd(path)
        return redirect(url_for("excludes"))
    allexcludes = getexlusion()
    return render_template("exclusions.html",exclusions = allexcludes)




@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Quratine")
def Quratine():
    try:
        with open("quradata.json", "r") as f:
            data = json.load(f)
            print(data)
        return render_template("quratine.html", data=data)
    except Exception as e:
        return jsonify({"Error": str(e)}), 500

@app.route("/filecheck")
def scanner():
    return render_template("scanner.html")

@app.route("/frontend")
def frontend():
    return render_template("FrontEnd.html")

@app.route("/endpoint", methods=["GET"])
def endroute():
    try:
        scanres = hijackchecker.checkdl2()
        filterres = []
        exclusions = getexlusion()
        for entry in scanres:
            dllpath = entry.get("path","")
            if dllpath in exclusions:
                continue
            filterres.append(entry)

        
        return jsonify({"dllresults": filterres}), 200
    except Exception as e:
        return jsonify({"Error": str(e)}), 500
    

@app.route("/sigcheck", methods=["POST"])
def sigcheck():
    fdata = request.files.get("file")
    if not fdata:
        return jsonify({"error": "no file uploaded"}), 400
    try:
        orgfn = fdata.filename
        temph = os.path.join(tempdir, orgfn)
        fdata.save(temph)
        fnex = os.path.splitext(temph)[0]
        print(fnex)
        execres = subprocess.run(["py", "sigcheck.py", temph], capture_output=True, text=True)
        if execres.returncode == 0:
            output = execres.stdout.strip().split('\n')
            return jsonify({
                "hash": output[0],
                "verdict": output[1] if len(output) > 1 else "Unknown"
            }), 200
        else:
            return jsonify({"error": execres.stderr.strip()}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if os.path.exists(temph):
            os.remove(temph)
            print("Done!")


for p in getexlusion():
    print(p)
app.run()
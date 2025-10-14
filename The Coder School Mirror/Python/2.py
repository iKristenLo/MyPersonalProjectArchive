import os
import shutil
import logging
import datetime
import json

logging.basicConfig(
    filename = "qura.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)
 
quradir = os.path.expanduser("~/quradir")
 
jsonholder = os.path.join(os.path.dirname(os.path.abspath(__file__)),"quradata.json")

def jsonupd(entry):
    if os.path.exists(jsonholder):
        with open(jsonholder,"r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    data.append(entry)
    with open(jsonholder,"w") as f:
        json.dump(data,f,indent = 4)
    




def setqura():
    if not os.path.exists(quradir):
        os.makedirs(quradir)
        logging.info(f"QuraFolder Created At {quradir}")
 
def qurafile(filepath):
    if not os.path.exists(filepath):
        logging.warning(f"The File Dose Not EXIST {filepath}")
        return
    setqura()
    filen = os.path.basename(filepath)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    qurafn = f"{timestamp}_{filen}"
    qurapath = os.path.join(quradir,qurafn)
    try:
        shutil.move(filepath,qurapath)
        logging.info(f"File Quratined in {qurapath}")
        os.system(f'attrib -a +r "{qurapath}"')
        os.system(f'icacls "{qurapath}" /inheritance:r /deny Everyone:(X)')
        logging.info(f"restricted permissions for {qurapath}")
        print("Restriction Set!")
        entry = {
            "filename":filen,
            "orgfilepath":filepath,
            "qurapath":qurapath,
            "timestamp":timestamp
        }
        jsonupd(entry)
    except Exception as e:
        logging.error(f"failed to quratine {qurapath} {e}")

if __name__ == "__main__":
    filename = input("Input File Path").strip()
    qurafile(filename)

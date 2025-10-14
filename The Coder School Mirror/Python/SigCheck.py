import sys
import requests
import hashlib

def shah(fath):
    sha2 = hashlib.sha256()
    try:
        with open(fath,"rb") as f:
            for p in iter(lambda: f.read(4096),b""):
                sha2.update(p)
        return sha2.hexdigest()
    except FileNotFoundError:
        print(f"File Not Found {fath}")
        sys.exit(1)


def vtcheck(api,hash):
    url = f"https://www.virustotal.com/api/v3/files/{hash}"
    header = { 
        "x-apikey":api,
        "Accept":"application/json"
    }
    response = requests.get(url,headers=header)
    if response.status_code == 200:
        result = response.json()
        malcount = result["data"]["attributes"]["last_analysis_stats"]["malicious"]
        if malcount > 1 and malcount < 5:
            return "Sus File"
        elif malcount >= 5:
            return "Bad File"
        else:
            return "Safe File"
    elif response.status_code == 404:
        print("File Not Found In DB")
        sys.exit(1)
    else:
        print("Unknown Error")
        sys.exit(2)

if len(sys.argv) != 2:
    print("Jut Provide A File Path")
    sys.exit(1)

apikey = "a6ca73951df7adb6a7205d83ce13628f7ac650c3dfe728e7be0cea39c54335ee"
path = sys.argv[1]
filehash = shah(path)
print(filehash)
result = vtcheck(apikey,filehash)
if result == "Bad File":
    print("File Is A Virus!")
elif result == "Sus File":
    print("File Is Sus")
else:
    print("File Is Safe!")
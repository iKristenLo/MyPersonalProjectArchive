#OLD VERSION DONT USE
import os
import shutil
import logging
import datetime
 
logging.basicConfig(
    filename = "qura.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)
 
quradir = os.path.expanduser("~/quradir")
 
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
        if os.name == "posix":
            os.chmod(qurapath,0o400)
        elif os.name == "nt":
            os.system(f"attrib -a +r {qurapath}")
        logging.info(f"Restricted Permissions {qurapath}")
        print("Restriction Sucessfull")
    except Exception as e:
        logging.error(f"Failed to quratine file: {filepath} {e}")
        print(f"An Error has Occured {e}")

if __name__ == "__main__":
    filehold = input("Enter the path of the file: ").strip()
    qurafile(filehold)


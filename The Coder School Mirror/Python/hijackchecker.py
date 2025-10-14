import psutil
import os
import pefile
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

def checkdl():
    susdll = []
    processs = list(psutil.process_iter(attrs=["pid","name"]))
    numberh = len(processs)
    with ThreadPoolExecutor() as executor, tqdm(total=numberh,desc="process") as progress:
        futures = []
        for proc in processs:
            futures.append(executor.submit(procan,proc))
        for future in as_completed(futures):
            result = future.result()
            if result:
                susdll.extend(result)
            progress.update(1)
    return susdll


def checkdl2():
    susdll = []
    processs = list(psutil.process_iter(attrs=["pid","name"]))
    numberh = len(processs)
    with ThreadPoolExecutor() as executor:
        futures = []
        for proc in processs:
            futures.append(executor.submit(procan,proc))
        for future in as_completed(futures):
            result = future.result()
            if result:
                susdll.extend(result)
    return susdll

def procan(proc):
    susdll = []
    try:
        pid = proc.info["pid"]
        name = proc.info["name"]
        process = psutil.Process(pid)
        for module in process.memory_maps():
            if module.path.endswith(".dll"):
                dllp = module.path
                susdata = dllany(dllp)
                if susdata:
                    susdata["pid"] = pid
                    susdata["name"] = name
                    print(f"Process: {name} (PID: {pid})\nSUS DLL: {susdata["dll"]} -> SUS DLL Path: {susdata["path"]}\nFound DLL: {susdata["syspath"]}\nSus DLL Score: {susdata["dlscore"]}")
                    susdll.append(susdata)
    except(psutil.AccessDenied,psutil.NoSuchProcess):
        pass
    return susdll

def dllany(dll):
    sys32d = os.environ.get("SystemRoot",r"C:\Windows") + r"\System32"
    syswow = os.environ.get("SystemRoot",r"C:\Windows") + r"\SysWOW64"
    syssxs = os.environ.get("SystemRoot",r"C:\Windows") + r"\WinSxS"

    if dll.startswith(sys32d) or dll.startswith(syswow) or dll.startswith(syssxs):
        return None

    dllname = os.path.basename(dll)
    sys32dp = os.path.join(sys32d,dllname)
    syswoww =  os.path.join(syswow,dllname)
    if not dll.startswith(sys32d) and os.path.exists(sys32dp):
        dlscore = 0
        try:
            syssize = os.path.getsize(sys32dp)
            sussize = os.path.getsize(dll)
            if syssize != sussize:
                dlscore += 1
        except:
            dlscore += 1
        try:
            pe = pefile.PE(dll)
            imports = {entry.dll.decode() for entry in pe.DIRECTORY_ENTRY_IMPORT}
            susimports = {"kernel32.dll","advapi32.dll","ntdll.dll"}
            if susimports.intersection(imports):
                dlscore += 2
        except:
            dlscore += 1
        return {"dll":dllname,"path":dll,"syspath":sys32dp,"dlscore":dlscore}
    if not dll.startswith(syswow) and os.path.exists(syswoww):
        dlscore = 0
        try:
            syssize = os.path.getsize(syswoww)
            sussize = os.path.getsize(dll)
            if syssize != sussize:
                dlscore += 1
        except:
            dlscore += 1
        try:
            pe = pefile.PE(dll)
            imports = {entry.dll.decode() for entry in pe.DIRECTORY_ENTRY_IMPORT}
            susimports = {"kernel32.dll","advapi32.dll","ntdll.dll"}
            if susimports.intersection(imports):
                dlscore += 2
        except:
            dlscore += 1
        return {"dll":dllname,"path":dll,"syspath":syswoww,"dlscore":dlscore}
    return None


if __name__ == '__main__':
    results = checkdl()
    for item in results:
            print(f"Process: {item['pid']} (PID: {item['pid']})")
            print(f"SUS DLL: {item['dll']} -> SUS DLL Path: {item['path']}")
            print(f"Found DLL: {item['syspath']}")
            print(f"SUS score: {item['dlscore']}\n")

   
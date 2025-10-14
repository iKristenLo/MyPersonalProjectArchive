import ctypes
from ctypes import wintypes

dllholder = ctypes.windll.user32
msgwbox = dllholder.MessageBoxW
msgwbox.argtypes = [
    wintypes.HWND,
    wintypes.LPCWSTR,
    wintypes.LPCWSTR,
    wintypes.UINT
]

msgwbox.restype = ctypes.c_int
msgwbox(None,"test","this is a test",0)
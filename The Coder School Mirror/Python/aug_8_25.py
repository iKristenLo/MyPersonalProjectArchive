import base64

shellcode_hex = (
    "48 83 EC 28 48 31 C9 48 8D 15 11 00 00 00 48 8D"
    "0D 12 00 00 00 41 B9 00 00 00 00 FF 15 25 00 00"
    "00 89 C1 FF 15 26 00 00 00 C3 48 65 6C 6C 6F 00"
    "48 65 6C 6C 6F 2C 20 57 6F 72 6C 64 21 00"
)
shellcode_bytes = bytes.fromhex(shellcode_hex.replace(" ", ""))


encoded_shellcode = base64.b64encode(shellcode_bytes)

with open("shellcode.bin", "wb") as f:
    f.write(encoded_shellcode)

print("Base64 encoded shellcode written to shellcode.bin")
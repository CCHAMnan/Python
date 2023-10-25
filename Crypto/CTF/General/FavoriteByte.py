import binascii

string = binascii.unhexlify("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
l = [c for c in string]
for i in range(256):
    f = [chr(n^i) for n in l]
    a = "".join(f)
    if a.startswith("crypto"):
        print(a)
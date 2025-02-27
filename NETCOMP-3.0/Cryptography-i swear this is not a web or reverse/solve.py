import itertools
import string

expected_string = "7X!7|!@V|7eV77_!|@8S"

magic = [
    0x1fa9787f52d6819dac3e51c96c9850ac9a68a000,
    0x551e7b2ade66a9cd21538d24f8232eb9e3c6a00,
    0x685130edf575c5fd89b4ea52d8ce440fb75d40,
    0x4d2b06845e7f210fd15f3697fe234c69919a0,
    0x267227d769f1422427c2f550f7852c59bfec,
    0xd9fd323c23dd5a26579cb53a8a42996b38,
    0x388a9fbf545b3b1a5e4b80376e94de767,
    0xadef7b085371d7244d43d0011e7c6d5,
    0x18cbc26aefc3b3b1ef4588ce4acc6b,
    0x296e5ed6f99d55e5efb08eb856e9,
    0x314ef6584d10a8c5226f105685,
    0x2798a7a450463592994fc72f,
    0x133caaa3da819c1ca0087d,
    0x445974d799d8bcf9c3b,
]

magic2 = 0x2971713e56d0006e6a0b48126ca34000

def reverse_hash(expected_char):
    for c in string.printable:  
        result = 0
        oneChar = -ord(c)
        for j in range(len(magic)):
            result *= oneChar
            result += magic[len(magic) - 1 - j]
        nresult = result % magic2
        result = -result // magic2
        result += (888 - result) * (result > 127)
        result += (888 - result) * (not (nresult == 0))
        result += (888 - result) * (result < 33)
        calculated_char = chr(result)
        if calculated_char == expected_char:
            return c
    return None

def find_password(expected_string):
    password = ""
    for expected_char in expected_string:
        c = reverse_hash(expected_char)
        if c is None:
            return None
        password += c
    return password

password = find_password(expected_string)

if password:
    print(f"Flag: Netcomp{{{password}}}")
else:
    print("Flag not found.")

import sys
from os import system, path, chdir, remove, makedirs
from requests import get
from platform import system as osname
USER_DIR = path.expanduser("~/.zxcvbn")

if osname() == "Windows":
    print("windows is not supported.")
    sys.exit(1)

makedirs(USER_DIR, exist_ok=True)
chdir(USER_DIR)

if not path.exists("CydiaSubstrate.framework"):
    print("[*] downloading CydiaSubstrate..")
    with open("CydiaSubstrate.framework.zip", "wb") as ss:
        ss.write(get("https://cdn.discordapp.com/attachments/1099871910155796495/1117506544091799623/CydiaSubstrate.framework.zip").content)
    system("unzip CydiaSubstrate.framework.zip")
    remove("CydiaSubstrate.framework.zip")
    print("[*] downloaded CydiaSubstrate")

if not path.exists("librocketbootstrap.dylib"):
    print("[*] downloading librocketbootstrap..")
    with open("librocketbootstrap.dylib", "wb") as ss:
        ss.write(get("https://cdn.discordapp.com/attachments/1105635370885992458/1120562207860736010/librocketbootstrap.dylib").content)
    print("[*] downloaded librocketbootstrap")

if not path.exists("libmryipc.dylib"):
    print("[*] downloading libmryipc..")
    with open("libmryipc.dylib", "wb") as ss:
        ss.write(get("https://cdn.discordapp.com/attachments/1105635370885992458/1120562207458070568/libmryipc.dylib").content)
    print("[*] downloaded libmryipc")

print("[*] downloading pyzule..")
with open("pyzule.py", "wb") as p:
    p.write(get("https://raw.githubusercontent.com/asdfzxcvbn/pyzule/main/pyzule.py").content)
print("[*] downloaded pyzule!")

with open("pyzule.py", "r") as o1:
    data = o1.readlines()

data[0] = f"#!{sys.executable}\n"
print("[*] fixed interpreter path!")

with open("pyzule.py", "w") as o2:
    o2.writelines(data)

print("[!] please enter your sudo password (if prompted) to finish the installation")
system("sudo mv pyzule.py /usr/local/bin/pyzule")
system("sudo chmod +x /usr/local/bin/pyzule")

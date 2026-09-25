import json
import os
os.chdir(os.path.dirname(__file__))
import sys
sys.dont_write_bytecode = True
import comandos


cmdDict = {
    "numnam": comandos.numNam,
    "cmdlist": comandos.cmdList,
    "info": comandos.info,
    "demonlist": comandos.demonList,
    "count": comandos.count,
    "create": comandos.create,
    "delete": comandos.delete,
    "change": comandos.change
}

while True:
    cmd = input("DemonsCMD> ")
    arg = ""
    par = ""
    attr = ""


    base = comandos.split(cmd, " ", False)

    for num, i in enumerate(base):
        if num > 1:
            base[1] += i
        if num >= 1:
            base[1] += " "

    base += [""] * (2 - len(base))
    base = base[:2]

    if base[1]:
        base[1] = base[1][:-1]

    arg, par = base

    
    if arg.lower() in cmdDict:
        cmdDict[arg.lower()](par)
        print("")
    elif cmd:
        print(f"Err1: {arg} no es un comando existente.")
        print("")

    with open("demons.json", "w", encoding="utf-8") as archivo:
        json.dump(comandos.demons, archivo, indent=4, ensure_ascii=False)

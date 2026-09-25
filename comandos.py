import json


with open("demons.json", "r", encoding="utf-8") as archivo:
    demons = json.load(archivo)

alist = {
    "g": "Gauntlet",
    "p": "Plataforma",
    "w": "Weekly",
    "e": "Evento",
    "r": "Rebeat"
}
difs = [
    "Easy demon",
    "Medium demon",
    "Hard demon",
    "Insane demon",
    "Extreme demon",
    "Robtop demon"
]


# Divide una cadena en partes para facilitar su uso.
def split(s, s2, delQuote=True):
    div = []
    part = ""
    found = False

    for i in s:
        if i == s2 and not found:
            div += [part]
            part = ""
            continue
        if i == '"':
            found = not found
            if delQuote:
                continue
        part += i

    div += [part]
    return div

def cmdList(n=None):
    print("INFO - Muestra información sobre un demon.")
    print("NUMNAM - Muestra que nivel le corresponde a ese número en el orden y viceversa.")
    print("CMDLIST - Muestra la lista de comandos.")
    print("DEMONLIST - Muestra la lista de demons")
    print("COUNT - Cuenta cuantos demons hay con cada propiedad.")
    print("CREATE - Crea un demon con las propiedades proporcionadas.")
    print("DELETE - Elimina un demon.")
    print("CHANGE - Cambia una propiedad de un demon.")

def numNam(n):
    if n.isdigit():
        n = int(n)
        if 1 <= n <= len(demons):
            for i in demons:
                if demons[i]["num"] == n:
                    print(f"{n} - {i}")
        else:
            print(f"Err2: Número fuera de rango. Números válidos: 1-{len(demons)}")
    else:
        for nombre in demons:
            if n.lower() == nombre.lower():
                print(f"{demons[nombre]['num']} - {nombre}")
                return
        print(f"Err3: {n} no está en la lista.")

def demonList(n=None):
    print("Nombre                   Número                   Dificultad               Atributos")
    print("======                   ======                   ======                   ======", end="")
    for i in demons:
        print("\n" + i + " " * (25 - len(i)), end="")
        for i2 in demons[i]:
            if i2 == "attr":
                attr2 = ""
                for i3 in demons[i][i2]:
                    attr2 += alist[i3] + ", "
                attr2 = attr2[:len(attr2) - 2]
                print(f"{attr2}{' ' * (25 - len(attr2))}", end="")
            else:
                print(f"{demons[i][i2]}{' ' * (25 - len(str(demons[i][i2])))}", end="")
    print("\n")

def info(s):
    for key in demons:
        if s.lower() == key.lower():
            print(key)
            print("=====")
            print(f"Número: {demons[key]['num']}")
            print(f"Dificultad: {demons[key]['dif']}\n")
            
            if demons[key]["attr"]:
                for i in demons[key]["attr"]:
                    print(alist[i])
            return
    print(f"Err3: {s} no está en la lista.")

def count(n=None):
    if n == None or n == "":
        print(f"Total: {len(demons)}\n")
        for i in difs:
            diftotal = 0
            for i2 in demons:
                if demons[i2]["dif"] == i:
                    diftotal += 1
            if diftotal:
                print(f"{i}: {diftotal} ({diftotal / len(demons) * 100:.2f}%)")

def create(s):
    demon = split(s, " ")[0]
    
    if demon in demons:
        print(f"Err4: {demon} ya está en la lista.")
    else:
        prop = split(s, " ")
        prop = prop[1:]
        prop2 = {"num": len(demons) + 1, "dif": "", "attr": ""}

        for i in prop:
            splitted = split(i, "=")

            if splitted[0] not in ["/num", "/dif", "/attr"]:
                print("Err5: Ese atributo no existe.")
                return
            if splitted[0] == "/num":
                print("Err6: /num no es válido.")
                return
                
            prop2[splitted[0][1:]] = splitted[1]
        demons[demon] = prop2

def delete(s):
    if s not in demons:
        print(f"Err3: {s} no está en la lista.")
    elif input("¿Estás seguro?: ") == "si":
        for i in demons:
            if demons[i]["num"] >= demons[s]["num"]:
                demons[i]["num"] -= 1
        del(demons[s])


def change(s):
    print("Funcion inacabada")

import json

DATA_FILE = "data.json"


def cargar_datos():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"usuarios": {}, "cuentas": {}}


def guardar_datos(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def login(data, pin):
    for cuenta in data["cuentas"].values():
        if str(cuenta.get("pin")) == str(pin):
            return cuenta
    return None


def cuentas_de_usuario(data, id_usuario):
    return [c for c in data["cuentas"].values() if c.get("id_usuario") == id_usuario]

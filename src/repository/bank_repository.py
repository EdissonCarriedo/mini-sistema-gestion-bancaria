import json

DATA_FILE = "data.json"

def cargar_datos():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"usuarios": {}, "cuentas": {}}

# Esto guarda los datos en data.json hay que tener cuidado por que
# borra tooooodo el contenido del json y lo reescribe entonces hay que 
# pasarle el data completo habiendo cambiado ya previamente los datos.
def guardar_datos(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def login(data, pin):
    for cuenta in data["cuentas"].values():
        if str(cuenta.get("pin")) == str(pin):
            return cuenta
    return None

def cuentas_de_usuario(data, id_usuario):
    return [c for c in data["cuentas"].values() if c.get("id_usuario") == id_usuario]

# Añade una cantidad de dinero a la cuenta que se le pasa
def deposit_money(data, account, quantity):
    account["balance"] += quantity
    guardar_datos(data)


def get_user_by_dni(dni,data):
    for user in data["users"].values():
        if dni == user["dni"]:
            return user
    return None

def get_account_by_id (id,data):
    account_list = []
    for account in data["accounts"].values():
        if id == account["id_user"]:
            account_list.append(account)
    return account_list

def get_balance(account):
    return account['balance']

def get_account_number(account):
    return account["account_number"]

def select_account(accounts, selected_account):
    return accounts[selected_account - 1]

def withdraw_cash(data, account, quantity):
    account["balance"] -= quantity
    guardar_datos(data)

def get_user_name(user):
    return user["name"] + " " + user["surname"]
import json

DATA_FILE = "data.json"

def cargar_datos():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"users": {}, "accounts": {}}

def guardar_datos(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def deposit_money(data, account, quantity):
    account["balance"] += quantity
    guardar_datos(data)

def get_user_by_dni(dni,data):
    for user in data["users"].values():
        if user["dni"] == dni:
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
    index = selected_account - 1
    if 0 <= index < len(accounts):
        return accounts[index]
    return None

def withdraw_cash(data, account, quantity):
    account["balance"] -= quantity
    guardar_datos(data)

def get_user_name(user):
    return user["name"] + " " + user["surname"]
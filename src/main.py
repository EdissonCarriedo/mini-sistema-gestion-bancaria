
import getpass
from repository.bank_repository import *

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
#TODO:Que devuelva el saldo de una cuenta 
def get_balance(accounts):
    print("seleccione una cuenta: ")

    i = 1
    for a in accounts:
        print(f"{i}. {a['account_number']}")
        i += 1
    user_input = input("Cuenta seleccionada: ")
    selected_account = accounts[int(user_input) - 1]
    return selected_account['saldo']
# TODO:Devolvera una cuenta(objeto), account es una lista y select_account
def select_account(accounts, selected_account):
    l = 1
    for a in accounts:
        l +=1
    return
#TODO: lo mismo que ingresar pero restando xD 
def cash_out(account, quantity):
    for c in account:
        print (c['saldo'])
    quantity = input("Que cantidad desea retirar: ")
    quantity -= c['saldo']



def main():
    # simulacion de entrada
    data = cargar_datos()
    dni_input = "12345678X"

    usuario = get_user_by_dni(dni_input, data)
    id_user = usuario["id_user"]
    account = get_account_by_id(id_user, data)

    print(usuario["dni"])
    print(account)

    # esto es vista
    print("seleccione una cuenta: ")
    selected_account = get_balance(account)
    print(selected_account)
    # i = 1
    # for a in account:
    #     print(f"{i}. {a['account_number']}")
    #     i += 1
    # user_input = input("Cuenta seleccionada: ")
    # print(int(user_input) - 1)
    # # print(account[int(user_input) - 1])
    # selected_account = account[int(user_input) - 1]
    # print(selected_account)
    # print()
    # print(deposit_money(data, account, quantity))
    
    # quantity = 10000
    # deposit_money(data, selected_account, quantity)
    # print(deposit_money(data, account, quantity))





    # data = cargar_datos()
    # print(data)

if __name__ == "__main__":
    main()
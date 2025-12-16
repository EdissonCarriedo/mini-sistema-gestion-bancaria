
import getpass
from repository.bank_repository import *

def get_user_by_dni(dni,data):
    for user in data["users"].values():
        if dni == user["dni"]:
            return user
        else:
            return None

def get_account_by_id (id,data):
    account_list = []
    for account in data["accounts"].values():
        if id == account["id_user"]:
            account_list.append(account)
    return account_list




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
    i = 1
    for a in account:
        print(f"{i}. {a["account_number"]}")
        i += 1
    user_input = input("Cuenta seleccionada: ")
    print(int(user_input) - 1)
    # print(account[int(user_input) - 1])
    selected_account = account[int(user_input) - 1]
    print(selected_account)






    # data = cargar_datos()
    # print(data)

if __name__ == "__main__":
    main()

import getpass
from repository.bank_repository import *

def get_user_by_dni(dni,data):
    for user in data["users"].values():
        if dni == user["dni"]:
            return user
        else:
            return None

def main():
    # simulacion de entrada
    data = cargar_datos()
    dni_input = "12345678X"
    usuario = get_user_by_dni(dni_input, data)
    print(usuario["dni"])
    





    # data = cargar_datos()
    # print(data)

if __name__ == "__main__":
    main()
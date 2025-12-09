
import getpass
from repository.bank_repository import *

def main():
    # el getpass oculta la entrada del usuario en la terminal
    pin = getpass.getpass("Ingrese su PIN: ")
    pin2 = int(input("Ingrese su PIN (input normal): "))
    print(f"PIN ingresado: {pin}")
    print(f"PIN ingresado (input normal): {pin2}")

    data = cargar_datos()
    print(data)

if __name__ == "__main__":
    main()
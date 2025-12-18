import getpass

def show_menu():
    print(
            """
    ========================================
            SISTEMA DE GESTIÓN BANCARIA
    ========================================
    Seleccione una operación:

    1) Consultar saldo
    2) Ingresar dinero
    3) Retirar dinero
    4) Salir

    ----------------------------------------
    """
        )
    return input("Operación seleccionada: ")

def show_accounts(accounts_list):
    print("\n")
    i = 1
    for a in accounts_list:
        print(f"{i}. {a['account_number']}")
        i += 1

def input_select_account():
    valid_input = False
    selected_account = None
    while not valid_input:
        try:
            print("\n")
            selected_account = int(input("Seleccione una cuenta: "))
            valid_input = True
        except ValueError:
            print("Error: por favor ingrese un número válido.")
    return selected_account

def show_balance(account):
    print(
        f"""
    ----------------------------------------
        RESUMEN DE CUENTA BANCARIA
    ----------------------------------------
    Cuenta Nº : {account['account_number']}
    Saldo     : {account['balance']:,.2f} €
    ----------------------------------------
    """
    )

def show_login():
    print(
        """
    ========================================
            ACCESO BANCA ELECTRÓNICA
    ========================================
    Por favor, identifíquese para continuar
    ----------------------------------------
    """
        )

    dni = input("DNI : ").strip().upper()
    pin = getpass.getpass("PIN : ")

    return dni, pin

def input_deposit_money():
    while True:
        try:
            entrada = input("\nIntroduzca la cantidad a ingresar: ")
            entrada = entrada.replace(",", "")
            cantidad = float(entrada)
            return cantidad
        except ValueError:
            print("Error: por favor ingrese un número válido.")

def input_withdraw_cash():
    while True:
        try:
            entrada = input("\nIntroduzca la cantidad a retirar: ")
            entrada = entrada.replace(",", "")
            cantidad = float(entrada)
            return cantidad
        except ValueError:
            print("Error: por favor ingrese un número válido.")

def goodbye(user_name):
    print("\n")
    print(f"Hasta pronto {user_name}")

def hello(user_name):
    print("\n")
    print(f"!Bienvenido! {user_name}")
    
def authenticated_failed():
    print(
            """
    ========================================
            ACCESO DENEGADO
    ========================================
    El DNI o el código PIN ingresado
    no coinciden con nuestros registros.
    Por motivos de seguridad, por favor inténtelo nuevamente.
    ----------------------------------------
    """
        )
    
def dni_not_valid():
    print(
            """
    ========================================
            ACCESO DENEGADO
    ========================================
    El DNI ingresado no es válido.
    Por favor inténtelo nuevamente.
    ----------------------------------------
    """
        )

def press_enter_to_continue():
    input("\nPulsa ENTER para volver al menú...")

def invalid_amount():
    print(
            """
    ----------------------------------------
    IMPORTE NO VÁLIDO
    ----------------------------------------
    El importe debe ser un número positivo.
    ----------------------------------------
    """
        )

def insufficient_funds():
    print(
            """
    ----------------------------------------
    OPERACIÓN DENEGADA
    ----------------------------------------
    Fondos insuficientes para realizar
    la operación solicitada.
    ----------------------------------------
    """
        )

def zero_funds():
    print(
            """
    ----------------------------------------
    La cuenta está a cero no se puede 
    proceder con la operación.
    ----------------------------------------
    """
        )
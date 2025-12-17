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
    print("\n")
    return int(input("Seleccione una cuenta: "))

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
    
def input_deposit_money():
    print("\n")
    return float(input("Introduzca la cantidad a ingresar: "))

def input_withdraw_cash():
    print("\n")
    return float(input("Introduzca la cantidad a retirar: "))

def goodbye(user_name):
    print("\n")
    print(f"Hasta pronto {user_name}")
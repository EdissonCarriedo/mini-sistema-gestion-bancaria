from repository import bank_repository as BankRepository
from view import menu as Menu
from utils.constants import *

def main():
    # simulacion de entrada
    data = BankRepository.cargar_datos()
    dni_input = "12345678X"

    user = BankRepository.get_user_by_dni(dni_input, data)
    accounts = BankRepository.get_account_by_id(user["id_user"], data)
    
    option_menu = int(Menu.show_menu())
    
# 1) Consultar saldo

    if option_menu == GET_BALANCE:
        Menu.show_accounts(accounts)
        selected_account = Menu.input_select_account()
        account = BankRepository.select_account(accounts, selected_account)
        Menu.show_balance(account)

# 2) Ingresar dinero
    elif option_menu == DEPOSIT:
        Menu.show_accounts(accounts)
        selected_account = Menu.input_select_account()
        account = BankRepository.select_account(accounts, selected_account)
        print(f"Cuenta seleccionada: {BankRepository.get_account_number(account)}")
        quantity = Menu.input_deposit_money()
        BankRepository.deposit_money(data, account, quantity)
        Menu.show_balance(account)

# 3) Retirar dinero
    elif option_menu == WITHDRAW:
        Menu.show_accounts(accounts)
        selected_account = Menu.input_select_account()
        account = BankRepository.select_account(accounts, selected_account)
        print(f"Cuenta seleccionada: {BankRepository.get_account_number(account)}")
        quantity = Menu.input_withdraw_cash()
        BankRepository.withdraw_cash(data, account, quantity)
        Menu.show_balance(account)

# 4) Salir
    elif option_menu == EXIT:
        user_name = BankRepository.get_user_name(user)
        Menu.goodbye(user_name)
        
if __name__ == "__main__":
    main()
from repository import bank_repository as BankRepository
from view import menu as Menu
from utils.constants import *
from utils.validators import *

def main():

    data = BankRepository.cargar_datos()
    user = None
    # LOGIN
    while not user:
        user_dni_input, user_pin_input = Menu.show_login()

        if not validate_dni(user_dni_input):
            Menu.dni_not_valid()
            continue

        if not validate_login(data, user_dni_input, user_pin_input):
            Menu.authenticated_failed()
            continue

        user = BankRepository.get_user_by_dni(user_dni_input, data)
        accounts = BankRepository.get_account_by_id(user["id_user"], data)
        Menu.hello(BankRepository.get_user_name(user))

    # MENU
    run = True
    
    while True:
        option_menu = int(Menu.show_menu())

        # 1) Consultar saldo
        if option_menu == GET_BALANCE:
            Menu.show_accounts(accounts)
            selected_account = Menu.input_select_account()
            account = BankRepository.select_account(accounts, selected_account)
            Menu.show_balance(account)
            Menu.press_enter_to_continue()

        # 2) Ingresar dinero
        elif option_menu == DEPOSIT:
            Menu.show_accounts(accounts)
            selected_account = Menu.input_select_account()
            account = BankRepository.select_account(accounts, selected_account)
            quantity = Menu.input_deposit_money()
            BankRepository.deposit_money(data, account, quantity)
            Menu.show_balance(account)
            Menu.press_enter_to_continue()

        # 3) Retirar dinero
        elif option_menu == WITHDRAW:
            Menu.show_accounts(accounts)
            selected_account = Menu.input_select_account()
            account = BankRepository.select_account(accounts, selected_account)
            quantity = Menu.input_withdraw_cash()
            BankRepository.withdraw_cash(data, account, quantity)
            Menu.show_balance(account)
            Menu.press_enter_to_continue()

        # 4) Salir
        elif option_menu == EXIT:
            Menu.goodbye(BankRepository.get_user_name(user))
            run = False

        else:
            Menu.option_not_valid()
            Menu.press_enter_to_continue()


if __name__ == "__main__":
    main()

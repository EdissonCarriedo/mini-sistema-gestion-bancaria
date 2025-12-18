from repository import bank_repository as BankRepository
from view import menu as Menu
from utils.constants import *
from utils.validators import *

def input_menu_option():

    while True:
        option = Menu.show_menu()
        if option.isdigit():
            option = int(option)
            if option in [GET_BALANCE, DEPOSIT, WITHDRAW, EXIT]:
                return option
        print("\nPor favor, introduzca un valor válido de la pantalla.")

def select_account_safe(accounts):

    valid_account = False
    while not valid_account:
        selected_account = Menu.input_select_account()
        account = BankRepository.select_account(accounts, selected_account)
        if account is not None:
            valid_account = True
        else:
            print("\nPor favor, seleccione un número de cuenta válido.")
    return account

def main():
    data = BankRepository.cargar_datos()
    user = None

    # LOGIN
    while not user:
        user_dni_input, user_pin_input = Menu.show_login()

        if not validate_dni(user_dni_input):
            Menu.dni_not_valid()
        elif not validate_login(data, user_dni_input, user_pin_input):
            Menu.authenticated_failed()
        else:
            user = BankRepository.get_user_by_dni(user_dni_input, data)
            accounts = BankRepository.get_account_by_id(user["id_user"], data)
            Menu.hello(BankRepository.get_user_name(user))

    # MENU
    run = True
    while run:
        option_menu = input_menu_option()

        # 1) Consultar saldo
        if option_menu == GET_BALANCE:
            Menu.show_accounts(accounts)
            account = select_account_safe(accounts)
            Menu.show_balance(account)
            Menu.press_enter_to_continue()

        # 2) Ingresar dinero
        elif option_menu == DEPOSIT:
            Menu.show_accounts(accounts)
            account = select_account_safe(accounts)

            valid_input = False
            while not valid_input:
                amount_input = Menu.input_deposit_money()
                if validate_amount(amount_input):
                    amount = float(amount_input)
                    BankRepository.deposit_money(data, account, amount)
                    Menu.show_balance(account)
                    Menu.press_enter_to_continue()
                    valid_input = True
                else:
                    Menu.invalid_amount()

        # 3) Retirar dinero
        elif option_menu == WITHDRAW:
            Menu.show_accounts(accounts)
            account = select_account_safe(accounts)

            if account["balance"] <= 0:
                Menu.show_balance(account)
                Menu.zero_funds()
                Menu.press_enter_to_continue()
            else:
                valid_input = False
                while not valid_input:
                    amount_input = Menu.input_withdraw_cash()
                    try:
                        amount = float(amount_input)
                    except ValueError:
                        print("Ingrese un número válido.")
                        continue

                    if validate_withdraw(amount, account["balance"]):
                        BankRepository.withdraw_cash(data, account, amount)
                        Menu.show_balance(account)
                        Menu.press_enter_to_continue()
                        valid_input = True
                    else:
                        Menu.insufficient_funds()


        # 4) Salir
        elif option_menu == EXIT:
            Menu.goodbye(BankRepository.get_user_name(user))
            run = False

if __name__ == "__main__":
    main()

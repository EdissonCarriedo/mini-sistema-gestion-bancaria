import re
from repository import bank_repository as BankRepository

def validate_login(data, dni, pin):
    user = BankRepository.get_user_by_dni(dni, data)
    validate = False
    if user and pin == user["pin"]:
        validate = True
    return validate   

def validate_dni(dni):
    
    dni = dni.strip().upper()
    
    if not re.fullmatch(r"\d{8}[A-Z]", dni):
        return False

    numero = int(dni[:8])
    letra = dni[8]

    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    return letra == letras[numero % 23]

def validate_amount(amount):
    try:
        amount = float(amount)
    except (TypeError, ValueError):
        return False

    return amount > 0

def validate_withdraw(amount, balance):
    if not validate_amount(amount):
        return False

    return amount <= balance

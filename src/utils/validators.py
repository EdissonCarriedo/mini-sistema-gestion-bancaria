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
    print(letra, letras[numero % 23])
    return letra == letras[numero % 23]


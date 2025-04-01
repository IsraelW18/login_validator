# ========== validator.py ==========
import re
from exceptions.username_exceptions import *
from exceptions.password_exceptions import *

def check_input(user_name, password):
    # === Username validation ===
    if not re.fullmatch(r'[A-Za-z0-9_]+', user_name):
        raise UsernameContainsIllegalCharacter(user_name)
    elif len(user_name) < 3:
        raise UsernameTooShort(user_name)
    elif len(user_name) > 16:
        raise UsernameTooLong(user_name)

    # === Password validation ===
    if len(password) < 8:
        raise PasswordTooShort(password)
    elif not re.search(r'[A-Z]', password):
        raise PasswordMissingCharacterUppercase(password)
    elif not re.search(r'[a-z]', password):
        raise PasswordMissingCharacterLowercase(password)
    elif not re.search(r'[0-9]', password):
        raise PasswordMissingCharactersDigit(password)
    elif not re.search(r'[!@#$%^&*()_+~`/\\\"{}\[\]:;,.<>?-]', password):
        raise PasswordMissingCharactersSpecial(password)
    elif len(password) > 40:
        raise PasswordTooLong(password)
    else:
        return True
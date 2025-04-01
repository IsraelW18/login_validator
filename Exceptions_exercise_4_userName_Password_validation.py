import re

# === Base Exception Classes ===

# Base class for all username-related exceptions
class UserNameException(Exception):
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return "Username Problem: "

# Base class for all password-related exceptions
class PasswordException(Exception):
    def __init__(self, password):
        self.password = password

    def __str__(self):
        return "Password problem: "

# === Specific Username Exceptions ===

# Raised when the username contains illegal characters
class UsernameContainsIllegalCharacter(UserNameException):
    def __str__(self):
        for i, letter in enumerate(self.username):
            if not re.fullmatch(r'[A-Za-z0-9_]', letter):
                return super().__str__() + f"Username \"{self.username}\" includes illegal character '{letter}' at index {i}.\n"

# Raised when the username is too short
class UsernameTooShort(UserNameException):
    def __str__(self):
        return super().__str__() + f"Username \"{self.username}\" is too short, should be at least 3 characters.\n"

# Raised when the username is too long
class UsernameTooLong(UserNameException):
    def __str__(self):
        return super().__str__() + f"Username \"{self.username}\" is too long, should be less than 17 characters.\n"

# === Specific Password Exceptions ===

# General class for password missing character types
class PasswordMissingCharacter(PasswordException):
    def __str__(self):
        return super().__str__() + f'Password is missing a required character type '

# Raised when the password is too short
class PasswordTooShort(PasswordException):
    def __str__(self):
        return super().__str__() + f'Password "{self.password}" is too short, should be at least 8 characters long.'

# Raised when the password is too long
class PasswordTooLong(PasswordException):
    def __str__(self):
        return super().__str__() + f'Password "{self.password}" is too long, should be maximum 40 characters.\n'

# === Specific character-type exceptions (inherit from PasswordMissingCharacter) ===

class PasswordMissingCharacterUppercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + "(Uppercase)"

class PasswordMissingCharacterLowercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + "(Lowercase)"

class PasswordMissingCharactersDigit(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + "(Digit)"

class PasswordMissingCharactersSpecial(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + "(Special)"

# === Validation Function ===

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

    # If all validations passed, return True
    return True

# === Main Logic (Loop Until Valid Input) ===

def main():
    while True:
        username = input("Please enter your 'Username':    ")
        password = input("Please enter your 'Password':    ")

        try:
            check_input(username, password)
            print("You are logged-in successfully!")
            break
        except Exception as e:
            print(e)

# Entry point
if __name__ == "__main__":
    main()

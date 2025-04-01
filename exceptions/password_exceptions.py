# ========== exceptions/password_exceptions.py ==========
class PasswordException(Exception):
    def __init__(self, password):
        self.password = password

    def __str__(self):
        return "Password problem: "


class PasswordMissingCharacter(PasswordException):
    def __str__(self):
        return super().__str__() + 'Password is missing a required character type '


class PasswordTooShort(PasswordException):
    def __str__(self):
        return super().__str__() + f'Password "{self.password}" is too short, should be at least 8 characters long.'


class PasswordTooLong(PasswordException):
    def __str__(self):
        return super().__str__() + f'Password "{self.password}" is too long, should be maximum 40 characters.\n'


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
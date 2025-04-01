# ========== exceptions/username_exceptions.py ==========
import re

class UserNameException(Exception):
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return "Username Problem: "


class UsernameContainsIllegalCharacter(UserNameException):
    def __str__(self):
        for i, letter in enumerate(self.username):
            if not re.fullmatch(r'[A-Za-z0-9_]', letter):
                return super().__str__() + f"Username \"{self.username}\" includes illegal character '{letter}' at index {i}.\n"


class UsernameTooShort(UserNameException):
    def __str__(self):
        return super().__str__() + f"Username \"{self.username}\" is too short, should be at least 3 characters.\n"


class UsernameTooLong(UserNameException):
    def __str__(self):
        return super().__str__() + f"Username \"{self.username}\" is too long, should be less than 17 characters.\n"
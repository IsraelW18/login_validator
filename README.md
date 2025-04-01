# 🔐 Python Login Validator Mechanism

A modular Python project that validates username and password input based on predefined rules, using custom exceptions, object-oriented design, and regular expressions. This project is structured for clarity, scalability, and professional-level maintainability.

---

## Features

- Modular architecture with clear file separation
- Strong validation logic for both username and password
- Custom exception hierarchy with detailed messages
- Continuous user input until valid credentials
- Designed for extensibility (future GUI, database, API integration)

---

## 📁 Project Structure

```
login_validator/
├── main.py                      # Entry point, handles user interaction
├── validator.py                 # Contains check_input() logic
├── exceptions/
│   ├── __init__.py              # Marks the folder as a package
│   ├── username_exceptions.py   # Custom exceptions for username errors
│   └── password_exceptions.py   # Custom exceptions for password errors
```

---

## Architecture

```text
                    +------------------+
                    |     main.py      |
                    |------------------|
                    |  input()         |
                    |  try/except      |
                    |  print(errors)   |
                    +--------+---------+
                             |
                             v
                    +--------+---------+
                    |   validator.py   |
                    |------------------|
                    | check_input()    |
                    |  - validate user |
                    |  - raise custom  |
                    +--------+---------+
                             |
          +------------------+------------------+
          |                                     |
          v                                     v
+---------------------------+       +----------------------------+
| username_exceptions.py    |       | password_exceptions.py     |
|---------------------------|       |----------------------------|
| UsernameTooShort          |       | PasswordTooShort           |
| UsernameTooLong           |       | PasswordTooLong            |
| UsernameContainsIllegal...|       | PasswordMissingCharacter.. |
+---------------------------+       +----------------------------+
```

---

## Validation Rules

### Username
- Length: 3–16 characters
- Allowed characters: letters, digits, underscore
- Custom error for illegal characters, short or long input

### Password
- Length: 8–40 characters
- Must contain:
  - At least one uppercase letter
  - At least one lowercase letter
  - At least one digit
  - At least one special character

---

## ▶️ How to Run

```bash
python main.py
```

Follow the prompts and fix any errors returned until login is successful.

---

## Virtual Environment Setup (Recommended)

To isolate dependencies and work in a clean environment:

```bash
# Create virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Activate it (Linux/macOS)
source venv/bin/activate

# Install any needed packages (if applicable)
pip install -r requirements.txt

# To save dependencies
pip freeze > requirements.txt
```

> Don't forget to add `venv/` to your `.gitignore` to avoid pushing it to GitHub.

---

## Example Output

```
Please enter your 'Username': da@vid
Username Problem: Username "da@vid" includes illegal character '@' at index 2.

Please enter your 'Password': 12345
Password problem: Password "12345" is too short, should be at least 8 characters long

Please enter your 'Password': David123
Password problem: Password is missing a required character type (Special)

You are logged-in successfully!
```

---

## 📄 License

MIT License. Free to use, distribute, and modify.

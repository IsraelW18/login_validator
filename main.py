# ========== main.py ==========
from validator import check_input


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


if __name__ == "__main__":
    main()
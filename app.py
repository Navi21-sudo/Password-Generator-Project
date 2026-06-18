import password_gen
import utilities

def program():
        while True:
            print("----PASSWORD GENERATOR----")
            print("You can generate a random password by specifying the desired length and the account name.")
            print("\nFirst enter your account name")
            account_name = input("Account name: ")
            print("Now enter the desired password length")
            input_length = utilities.try_except(input("Password length: "))

            password = password_gen.generate_password(input_length)
            print(f"Generated password for {account_name}: {password}")

            print("\nSaving account name and passwords in passwords.txt...")
            file_repo = "passwords.txt"
            with open(file_repo, "a") as file:
                file.write(f"{account_name}: \n{password}\n\n")

            print("Want to continue generating passwords? (y/n)")
            continue_choice = input().lower()
            if continue_choice != 'y':
                print("Exiting the password generator. Goodbye!")
                break
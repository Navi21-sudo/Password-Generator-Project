def try_except(length):
    while True:
        try:
            length = int(length)
            if length <= 0:
                print("Please enter a positive integer for the password length.")
                continue
            return length
        except ValueError:
            print("Invalid input. Please enter a valid integer for the password length.")
            length = input("Password length: ")

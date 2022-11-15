import time
import os
import random

# String of characters, numbers and symbols.
characters = "123456789abcdefghijklmnopqrstuvABCDEFGHIJKLMNOP!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

if __name__ == "__main__":
    repeat = True
    while (repeat):
        # Ask for the password length.
        passwordLength = input("Enter password length between 8 and 50: ")

        # Verify type.
        try:
            passwordLength = int(passwordLength)
        except TypeError:
            print(
                f'The entered value is not a number (value={passwordLength})')
            print(" ")
            time.sleep(0.5)
            continue

        if passwordLength < 8 or passwordLength > 50:
            print(
                f'Password length must be between 8 and 14 characters. Entered: {passwordLength}')
            print(" ")
            time.sleep(0.5)
            continue

        os.system('cls')

        # Generate passowrd.
        password = ""
        for char in range(0, passwordLength):

            # Random index from charactes.
            randomIndex = random.randint(0, len(characters) - 1)
            password = password + characters[randomIndex]

        print(f'Generated password: {password}')
        print(" ")

        tryAgain = input("Generate a diferent password? (y/n): ")

        if tryAgain.lower() == "y":
            os.system('cls')
            continue
        else:
            repeat = False
            os.system('cls')

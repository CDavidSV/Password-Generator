import time
import os
import random
from PasswordGenerator import PasswordGenerator

# Allows the user to modify the password.
# Input: PasswordGenerator object.
# Output: none.
def modifyPassword(passwordObj):
    return     

# Generates a new password based on input values given by the user.
# Input: none.
# Output: none.
def generateNewPassword():
    repeat = True
    while(repeat):
        # Ask for the password length.
        passwordLength = input("Enter password length between 8 and 50: ")

        # Verify type.
        try:
            passwordLength = int(passwordLength)
        except ValueError:
            print(f'The entered value is not a number (value={passwordLength})')
            print(" ")
            time.sleep(0.5)
            continue

        if passwordLength < 8 or passwordLength > 50:
            print(f'Password length must be between 8 and 50 characters. Entered: {passwordLength}')
            print(" ")
            time.sleep(0.5)
            continue
        
        uppercase = input("Would you like the password to contain uppercase letters? (y/n): ")
        lowercase = input("Would you like the password to contain lowercase letters? (y/n): ")
        numbers = input("Would you like the password to contain numbers? (y/n): ")
        symbols = input("Would you like the password to contain symbols? (y/n): ")
        os.system('cls')

        # Index 1: uppercase characters.
        # Index 2: lowercase characters.
        # Index 3: add numbers.
        # Index 4: add symbols.
        parameters = [uppercase, lowercase, numbers, symbols]
        selectedParameters = [False, False, False, False]
        falseParameters = 4

        for i, parameter in enumerate(parameters):
            if parameter.lower() == "y":
                selectedParameters[i] = True
                falseParameters -= 1

        if (falseParameters == 4):
            selectedParameters[3] = True
        
        generatedPassword = PasswordGenerator(passwordLength, selectedParameters[0], selectedParameters[1], selectedParameters[2], selectedParameters[3])

        repeatOptions = True
        while(repeatOptions):
            print(f"Generated password: {generatedPassword}")
            print(f"Strength: {generatedPassword.getStrength()}\n")
            
            print("1. Modify Password.\n2. Generate a new password.\n3. Exit")
            option = input("Select an option: ")

            if option == "1":
                modifyPassword(generatedPassword)
            elif option == "2":
                repeatOptions = False
            elif option == "3":
                return
            else:
                print("Incorrect or invalid option selected. Try again...")
                time.sleep(2)
                os.system("cls")  
        continue

# Tests the password strength given by the user.
# Input: Users password.
# output: none.
def testPasswordStrength():
    return

if __name__ == "__main__":
    repeat = True
    while (repeat):
        # Options.
        print("Password Generator\n")
        print("1. Test your passwords strength.\n2. Generate a new password.\n3. Exit\n")
        option = input("Select an option: ")

        if option == "1":
            os.system("cls")
            testPasswordStrength()
            repeat = False        
        elif option == "2":
            os.system("cls")
            generateNewPassword()
            repeat = False
        elif option == "3":
            repeat = False
        else:
            print("Incorrect or invalid option selected. Try again...")
            time.sleep(2)
            os.system("cls")
    os.system("cls")
    print("See you")
    time.sleep(2)
    os.system("cls")
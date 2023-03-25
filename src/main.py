import time
import os
import secrets
import math

# Verify a yes or no questions. Requires a yes or no question prompt as input.
# Returns true or false and handles if the user enters an invalid input.
def verify_response(question):
    response = ''
    while (response != 'y' and response != 'n'):
        response = input(f'{question} (y/n):').lower()

    if response == 'y':
        return True
    else:
        return False

# Using entropy to calculate password strength
def calculate_strength(password):
    chars = 95 # Total ammount of printable ASCII characters excluding the space.
    length = len(password)
    N = chars ** length
    entropy = math.log2(N)

    if entropy < 28:
        return 'Very Weak'
    elif entropy < 36:
        return 'Weak'
    elif entropy < 60:
        return 'Reasonable'
    elif entropy < 128:
        return 'Strong'
    else:
        return 'Very strong'   

# Generates a new password based on input values given by the user.
# Input: none.
# Output: none.
def generate_new_password():
    repeat = True
    while(repeat):
        # Ask for the password length.
        password_length = input("Enter password length between 8 and 50: ")

        # Verify type.
        try:
            password_length = int(password_length)
        except ValueError:
            print(f'The entered value is not a number (value={password_length})')
            print(" ")
            time.sleep(0.5)
            continue

        if password_length < 8 or password_length > 50:
            print(f'Password length must be between 8 and 50 characters. Entered: {password_length}')
            print(" ")
            time.sleep(0.5)
            continue
        
        uppercase = verify_response("Would you like the password to contain uppercase letters?")
        lowercase = verify_response("Would you like the password to contain lowercase letters?")
        numbers = verify_response("Would you like the password to contain numbers?")
        symbols = verify_response("Would you like the password to contain symbols?")
        os.system('cls')

        # Arrays of characters, numbers and symbols.
        uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
        numbers = "0123456789"
        special_characters = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

        options = []
        if uppercase:
            options.append(uppercase_letters)
        if lowercase: 
            options.append(lowercase_letters)
        if numbers:
            options.append(numbers)
        if symbols:
            options.append(special_characters)
        
        password = ''
        for i in range(password_length):
            characters = secrets.choice(options)
            password += secrets.choice(characters)

        repeat_options = True
        while(repeat_options):
            print(f"Generated password: {password}")
            print(f"Strength: {calculate_strength(password)}\n")
            
            print("1. Generate a new password.\n2. Exit")
            option = input("Select an option: ")

            if option == "1":
                repeat_options = False
            elif option == "2":
                return
            else:
                print("Incorrect or invalid option selected. Try again...")
                time.sleep(2)
                os.system("cls")  
        continue

if __name__ == "__main__":
    repeat = True
    while (repeat):
        # Options.
        print("Password Generator\n")
        print("1. Test your passwords strength.\n2. Generate a new password.\n3. Exit\n")
        option = input("Select an option: ")

        if option == "1":
            os.system("cls")
            input_password = input('Enter your password: ')
            print(f'Strength: {calculate_strength(input_password)}\n')      
        elif option == "2":
            os.system("cls")
            generate_new_password()
            repeat = False
        elif option == "3":
            repeat = False
        else:
            print("Incorrect or invalid option selected. Try again...")
            time.sleep(2)
            os.system("cls")
    os.system("cls")
    print("See you")
    time.sleep(1)
    os.system("cls")
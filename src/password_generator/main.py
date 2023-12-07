import argparse
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
def generate_new_password(password_length):
    if password_length < 8 or password_length > 100:
        print(f'Password length must be between 8 and 100 characters. Entered: {password_length}')
        print(" ")
        return
    
    uppercase = verify_response("Would you like the password to contain uppercase letters?")
    lowercase = verify_response("Would you like the password to contain lowercase letters?")
    numbers = verify_response("Would you like the password to contain numbers?")
    symbols = verify_response("Would you like the password to contain symbols?")

    # Arrays of characters, numbers and symbols.
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    special_characters = "!#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

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
    for _ in range(password_length):
        characters = secrets.choice(options)
        password += secrets.choice(characters)

    print(f"Generated password: {password}")
    print(f"Strength: {calculate_strength(password)}\n")

def main():
    parser = argparse.ArgumentParser(prog='Password Generator', description='Generate a random password or test the strength of a password.')
    
    parser.add_argument('-g', '--generate', type=int, help='Generate a new password.')
    parser.add_argument('-t', '--test', type=str, help='Test the strength of a password.')
    
    args = parser.parse_args()

    if args.generate is not None:
        generate_new_password(args.generate)
    elif args.test is not None:
        print(f"Strength: {calculate_strength(args.test)}")

if __name__ == "__main__":
    main()
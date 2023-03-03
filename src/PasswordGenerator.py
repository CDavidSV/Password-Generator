import secrets

class PasswordGenerator:
    __password = ""
    __strength = ""
    
    def __init__(self, pLength, uppercase, lowercase, numbers, symbols):
        self.__passwordLength = pLength
        self.__uppercase = uppercase
        self.__lowercase = lowercase
        self.__numbers = numbers
        self.__symbols = symbols

        if pLength <= 0: 
            self.__passwordLength = 1
        else:
            self.__passwordLength = pLength
        
        # Generate the password.
        self.generatePassword()

    def __str__(self):
        return f'{self.__password}'

    # Check the characters that the password contains.

    def generatePassword(self):
        # Arrays of characters, numbers and symbols.
        uppercaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lowercaseLetters = "abcdefghijklmnopqrstuvwxyz"
        numbers = "0123456789"
        specialCharacters = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

        options = []
        if self.__uppercase:
            options.append(uppercaseLetters)
        if self.__lowercase: 
            options.append(lowercaseLetters)
        if self.__numbers:
            options.append(numbers)
        if self.__symbols:
            options.append(specialCharacters)
        
        for i in range(self.__passwordLength):
            characters = secrets.choice(options)
            self.__password += secrets.choice(characters)



        return

    def calculateStrength():
        return

    def savePassword():
        return

    def copyPassword():
        return
    
    def removeCharacters():
        return
    
    def changeLenght():
        return
    
    def getStrength(self):
        return f'{self.__strength}'
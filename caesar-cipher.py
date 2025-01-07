
# user-defined function
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

# Request a message to be encrypted
def getMessage():
    stringToEncrypt = input("Inserisci un messaggio da crittografare: ")
    return stringToEncrypt

# Getting a cipher key
def getCipherKey():
    shiftAmount = input("Inserisci una chiave (numero intero da 1 a 25): ")
    return shiftAmount

# Encrypt the message
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = message.upper()  # Converts the message to uppercase
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage += alphabet[newPosition]
        else:
            encryptedMessage += currentCharacter
    return encryptedMessage

# Decrypting the message
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)

# Creating a main function
def runCaesarCipherProgram():
    myAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    myMessage = getMessage()
    myCipherKey = getCipherKey()
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Messaggio crittografato: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Messaggio decrittografato: {myDecryptedMessage}')

# call the function
runCaesarCipherProgram()
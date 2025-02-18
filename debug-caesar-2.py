# Module Lab: Caesar Cipher Program Bug #2
#
# In a previous lab, you created a Caesar cipher program. This version of
# the program is buggy. Use a debugger to find the bug and fix it.

# Double the given alphabet
def getDoubleAlphabet(alphabet):
    return alphabet  #fixed error/ There is no need to duplicate the alphabet

# Get a message to encrypt
def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt

# Get a cipher key
def getCipherKey():
    shiftAmount = input("Please enter a key (whole number from 1-25): ")
    return int(shiftAmount)  #fixed error/ Convert input to integer

# Encrypt message
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = message.upper()  #fixed/ Convert the message to uppercase
    for currentCharacter in uppercaseMessage:
        if currentCharacter in alphabet:  #fixed/ Encrypt only alphabetic characters
            position = alphabet.find(currentCharacter)
            newPosition = (position + cipherKey) % len(alphabet)  # Handle wraparound
            encryptedMessage += alphabet[newPosition]
        else:
            encryptedMessage += currentCharacter  # Keep non-alphabetic characters unchanged
    return encryptedMessage

# Decrypt message
def decryptMessage(message, cipherKey, alphabet):
    return encryptMessage(message, -cipherKey, alphabet)  #fixed/ Decrypt by reversing the cipher key

# Main program logic
def runCaesarCipherProgram():
    myAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Standard alphabet
    print(f'Alphabet: {myAlphabet}')
    myMessage = getMessage()
    print(f'Message to encrypt: {myMessage}')
    myCipherKey = getCipherKey()
    print(f'Cipher Key: {myCipherKey}')
    
    # Encrypt the message
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet)
    print(f'Encrypted Message: {myEncryptedMessage}')
    
    # Decrypt the message
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet)
    print(f'Decrypted Message: {myDecryptedMessage}')

# Main logic
runCaesarCipherProgram()

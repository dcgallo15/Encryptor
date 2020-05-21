stringInput = input('Enter a string to encrypt: ')
encryptCode = int(input('Enter the string shift: '))

print("In 'encrypt.txt' you will find your encrypted message")

def encrypt(string,encryptKey):
    myFile = open('encrypt.txt','w')
    encryptedString = []
    for x in range(len(string)):
        numVal = ord(string[x])
        numVal = numVal - encryptKey + x
        encryptChar = chr(numVal)
        encryptedString.append(encryptChar)
    
    for z in range(len(encryptedString)):
        myFile.write(encryptedString[z])
    myFile.close()
          
def decrypt(string,encryptKey):
    decryptedString = []
    for y in range(len(string)):
        numVal = ord(string[y])
        numVal = numVal + encryptKey - y
        decryptChar = chr(numVal)
        decryptedString.append(decryptChar)
        
    for c in range(len(decryptedString)):
        print(decryptedString[c],end="") 
    print(' is your decrypted string')     
        
encrypt(stringInput,encryptCode)

myFile = open('encrypt.txt','r')
read = myFile.read()
print('Your encrypted message is:',read)
decrypt(read,encryptCode)
myFile.close()
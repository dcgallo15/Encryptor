stringInput = input('Enter a string to encrypt: ')

while True:
    try:
        encryptCode = int(input('Enter the string shift: '))

        if encryptCode > 26:
            print('TRY AGAIN STRING SHIFT CANNOT BE OVER 26')

        else:
            break
    except:
        print('Try again enter a number'.center(30,'-'))

def encrypt(string,encryptKey):
    myFile = open('encrypt.txt','w')
    split = string.split()
    encryptedString = [[]for o in range(len(split))]
    
    for i in range(len(split)):
        for x in range(len(string)):
            numVal = ord(string[x])
            numVal = numVal - encryptKey + x
            encryptChar = chr(numVal)
            encryptedString[i].append(encryptChar)
    print(' ',end='')
    
    print('Your encrypted string is:')
    for p in range(len(encryptedString)):
        for z in range(len(encryptedString[p])):
            temp = encryptedString[p]
            #print(encryptedString[p[z]],end = '')
            print(temp[z],end = '')
            myFile.write(temp[z])
        print('\n',end='')
    myFile.close()

          
def decrypt(encryptKey):
    myFile = open('encrypt.txt','r')
    string = myFile.read()
    split = string.split()
    encryptedString = [[]for o in range(len(split))]
    
    for i in range(len(split)):
        for x in range(len(string)):
            numVal = ord(string[x])
            numVal = numVal + encryptKey - x
            encryptChar = chr(numVal)
            encryptedString[i].append(encryptChar)
    print(' ',end='')
    
    print('Your decrypted string is:')
    for p in range(len(encryptedString)):
        for z in range(len(encryptedString[p])-15):
            temp = encryptedString[p]
#            temp1 = temp[z]
#            temp1 = temp1[:-13]
            print(temp[z],end = '')
        print('\n',end='')
    myFile.close()
    
encrypt(stringInput,encryptCode)
decrypt(encryptCode)

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
    
decrypt('b`n!kv$f&wirx',2)
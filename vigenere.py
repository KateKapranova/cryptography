#vigenere cipher
#polyalphabetic shift cipher

alphabet={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,
"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,
"P":15,"Q":16,"R":17,"S":18,"T":19,"U":20,"V":21,"W":22,
"X":23,"Y":24,"Z":25," ":26}

key="A KEY"
n=27

def digitToLetter(L):
    cipherText=""
    for i in range(len(L)):
        for key in alphabet:
            if L[i]==alphabet[key]:
                cipherText+=key
    return cipherText

def encoding_vigenere(plaintext):
    keys=[]
    keyLength=len(key)
    cipher=[]
    for i in range(len(key)):
        keys.append(alphabet[key[i]])
    while (len(plaintext)>=keyLength):
        chunk=plaintext[:keyLength]
        for i in range(keyLength):
            cipher.append((alphabet[chunk[i]]+keys[i])%n)
        plaintext=plaintext[keyLength:]
    if len(plaintext)==0:
        return cipher
    while (len(plaintext)<keyLength):
        plaintext+=" "
    for j in range(len(plaintext)):
        cipher.append((alphabet[plaintext[j]]+keys[j])%n)
    
    return digitToLetter(cipher)
print(encoding_vigenere("INFORMATIK BRAUCHT MATHEMATIK"))


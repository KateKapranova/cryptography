#caesar cipher implementation

dict={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,
"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,
"P":15,"Q":16,"R":17,"S":18,"T":19,"U":20,"V":21,"W":22,
"X":23,"Y":24,"Z":25," ":26}
n=27
key="F"

def encoding_shift(x):
    encoded=(dict[x] + dict[key])%n
    for k in dict.keys():
        if dict[k]==encoded:
            return k

def decoding_shift(x):
    decoded = (dict[x]-dict[key])%n
    for k in dict.keys():
        if dict[k]==decoded:
            return k

def caesarEncode(plain_text):
    cipher=""
    for i in range(len(plain_text)):
        cipher+=encoding_shift(plain_text[i])
    return cipher

print(caesarEncode("ALL CATS ARE BLACK AT NIGHT"))

def caesarDecode(cipher):
    message=""
    for i in range(len(cipher)):
        message+=decoding_shift(cipher[i])
    return message

print(caesarDecode("FQQEHFYXEFWJEGQFHPEFYESNLMY"))
    

#affine cipher:
#two keys: a and b, a is used to multiply and b provides the linear shift
#important not all a in Z27 have a multiplicative inverse!
#sufficient requirement for having a multiplicative inverse: gcd(a,n)=1

dict={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,
"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,
"P":15,"Q":16,"R":17,"S":18,"T":19,"U":20,"V":21,"W":22,
"X":23,"Y":24,"Z":25," ":26}

n=27
a=8
b=3

#inversion implemented via brute force
#doesn't take into account absence of multiplicative inverse for some elements in Z27 (for instance 18)
def findInverse(b):
    for i in range(0,n):
        if (b*i)%n == 1:
            return i

def encoding_shift(x):
    encoded=(a*dict[x] + b)%n
    for k in dict.keys():
        if dict[k]==encoded:
            return k

def decoding_shift(x):
    decoded = (findInverse(a)*(dict[x]-b))%n
    for k in dict.keys():
        if dict[k]==decoded:
            return k

def affineEncode(plain_text):
    cipher=""
    for i in range(len(plain_text)):
        cipher+=encoding_shift(plain_text[i])
    return cipher

print(affineEncode("ENDE UM ZWEI UHR"))

def affineDecode(cipher):
    message=""
    for i in range(len(cipher)):
        message+=decoding_shift(cipher[i])
    return message

print(affineDecode("I AIWBSWORINWBFE"))



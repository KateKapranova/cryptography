#substitution cipher
#defines a permutation tabel


encoding_permutation={"A":"X","B":"N","C":"Y","D":"A","E":"H","F":"P","G":"O",
"H":"G","I":"Z","J":"Q","K":" ","L":"W","M":"B","N":"T","O":"S",
"P":"F","Q":"L","R":"R","S":"C","T":"V","U":"M","V":"U","W":"E",
"X":"K","Y":"J","Z":"D"," ":"I"}

decoding_permutation={"X":"A","N":"B","Y":"C","A":"D","H":"E","P":"F","O":"G",
"G":"H","Z":"I","Q":"J"," ":"K","W":"L","B":"M","T":"N","S":"O",
"F":"P","L":"Q","R":"R","C":"S","V":"T","M":"U","U":"V","E":"W",
"K":"X","J":"Y","D":"Z","I":" "}

def encode_substitution(clearText):
    cipher=""
    for i in range(len(clearText)):
        cipher+=encoding_permutation[clearText[i]]
    return cipher
    
print(encode_substitution("ENDE UM ZWEI UHR"))

def decode_substitution(cipherText):
    message=""
    for i in range(len(cipherText)):
        message+=decoding_permutation[cipherText[i]]
    return message

print(decode_substitution("HTAHIMBIDEHZIMGR"))
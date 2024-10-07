import fileAcc as fA

def main():
    org = fA.FileRead("org.txt")
    key = fA.FileRead("key.txt")
    # orgLetter = ""
    # keyLetter = ""
    encryptKey = {}
    for i in range(org.__len__()):
        if ('A' <= org[i]) & (org[i] <= 'Z'):
            # orgLetter += org[i]
            # keyLetter += key[i]
            print(org[i] + " >> " + key[i])
            encryptKey[org[i]] = key[i]
    # print(orgLetter)
    # print(keyLetter)
    # print(encryptKey)
    orgDes = fA.FileRead("description.txt")
    # print(orgDes)
    encryption = ""
    for i in orgDes:
        if ('A' <= i) & (i <= 'Z'):
            i = encryptKey[i]
        elif ('a' <= i) & (i <= 'z'):
            i = encryptKey[chr(ord(i)-97+65)]
        # print(char)
        encryption += i
    # print(encryption)
    fA.FileWrite("encrypt.txt",encryption)

if __name__=='__main__':
    main()
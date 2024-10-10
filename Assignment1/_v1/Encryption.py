import fileAcc as fA

def main():
    key = fA.FileRead("key.txt")
    alphaBat = key.split("\n")
    dictVal =""
    for i in range(len(alphaBat)):
        dictVal += (alphaBat[i])[0]
    dictKey = ''.join(sorted(dictVal))

    encryptKey = {}
    for i in range(len(dictKey)):
        encryptKey[dictKey[i]] = dictVal[i]

    des = fA.FileRead("description.txt")
    encryption = ""
    for i in des:
        if ('A' <= i) & (i <= 'Z'):
            i = encryptKey[i]
        elif ('a' <= i) & (i <= 'z'):
            i = chr(ord(encryptKey[chr(ord(i)-32)])+32)
        encryption += i
    fA.FileWrite("encrypt.txt",encryption)
    
    print("Success encrypt text!!!")

if __name__=='__main__':
    main()
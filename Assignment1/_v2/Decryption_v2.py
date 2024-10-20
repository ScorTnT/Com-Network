import fileAcc as fA

def main():
    key = fA.FileRead("key_v2.txt")
    key = key.replace("\n","")
    keyVal = ''.join(sorted(key))
    keyDict = {}
    for i in range(len(key)):
        keyDict[key[i]] = keyVal[i]

    encDes = fA.FileRead("encrypt_v2.txt")
    decDes = ""
    for i in encDes:
        if ('a' <= i) & (i <= 'z'):
            i = keyDict[i]
        elif ('A' <= i) & (i <= 'Z'):
            i = chr(ord(keyDict[chr(ord(i)+32)])-32)
        decDes += i

    fA.FileWrite("decrypt_v2.txt",decDes)
    print("Success decrypt text!!!")

if __name__=='__main__':
    main()
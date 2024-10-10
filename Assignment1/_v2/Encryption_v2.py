import fileAcc as fA

def main():
    key = fA.FileRead("key_v2.txt")
    key = key.replace("\n","")
    keyVal = ''.join(sorted(key))
    keyDict = {}
    for i in range(len(key)):
        keyDict[key[i]] = keyVal[i]

    des = fA.FileRead("description.txt")
    encDes = ""
    for i in des:
        if ('a' <= i) & (i <= 'z'):
            i = keyDict[i]
        elif ('A' <= i) & (i <= 'Z'):
            i = chr(ord(keyDict[chr(ord(i)+32)])-32)
        encDes += i

    fA.FileWrite("encrypt_v2.txt",encDes)
    print("Success encrypt text!!!")

if __name__=='__main__':
    main()
import fileAcc as fA

def main():
    key = fA.FileRead("key.txt")
    key = key.replace("\n","")
    keyVal = ""
    for i in key:
        if ('A' <= i) & (i <= 'Z'):
            keyVal += i
    key = keyVal
    keyVal = ''.join(sorted(keyVal))
    
    keyDict = {}
    for i in range(len(key)):
        keyDict[key[i]] = keyVal[i]

    encDes = fA.FileRead("encrypt.txt")
    decDes = ""
    for i in encDes:
        if (('A' <= i) & (i <= 'Z')) | (('a' <= i)&(i <= 'z')):
            tmp = 0
            if i not in keyDict:
                tmp = -32
            i = chr(ord(keyDict[chr(ord(i)+tmp)])-tmp)
        decDes += i
    fA.FileWrite("decrypt.txt", decDes)

    print("Success decrypt text!!!")

if __name__=='__main__':
    main()
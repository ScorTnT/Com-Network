import fileAcc as fA

def main():
    des = fA.FileRead("description.txt")
    des = des.replace("\n","")

    keyDict = {}
    for i in des:
        if ('A' <= i) & (i <= 'Z'):
            i = chr(ord(i)+32)

        if ('a' <= i) & (i <= 'z'):
            if(i not in keyDict):
                keyDict[i] = 0
            keyDict[i] += 1
    keyDict = dict(sorted(keyDict.items(),key=lambda x:x[1]))

    writeDes = ""
    for key in keyDict:
        print(key, keyDict[key])
        writeDes += (str(key) + ("\n"))
    fA.FileWrite("key_v2.txt",writeDes)

    print("Success generate Key!!!")
    
if __name__=='__main__':
    main()
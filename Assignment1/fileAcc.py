def FileRead(route):
    print("")
    print("---File Open process---")
    print("read file: " + route)
    readF = open(route, 'r')
    full = readF.read()
    #print(full)
    readF.close()
    print("---File Closed---")
    print("")
    return full

def FileWrite(route, des):
    print("")
    print("---File Open process---")
    print("write file: " + route)
    print("description: " + des)
    writeF = open(route, 'w')
    writeF.write(des)
    writeF.close()
    print("---File Closed---")
    print("")
import fileAcc as fA

def letterCounter(descript_):
    #print(description)
    print("\n---Sort process---")
    SIZE = 26
    cnt = [0 for i in range(SIZE)]

    for k in descript_:
        #print(ord(k))
        if ('A' <= k) & (k <= 'Z'):
            cnt[ord(k)-65] += 1
        elif ('a' <= k) & (k <= 'z'):
            cnt[ord(k)-97] += 1

    makeDictionary = {}
    for i in range(SIZE):
        #print("...")
        if cnt[i] == 0:
            continue
        alpha = chr(i+65)
        #print( alpha + " " + str(cnt[i]))
        makeDictionary[alpha] = cnt[i]
    print("---Sort Fin. ---")
    print("")
    return makeDictionary

def SortD(diction_):
    sortedDition_ = dict(sorted(diction_.items(),key=lambda x:x[1]))
    print("")
    return sortedDition_

def main():
    description = ""
    description = fA.FileRead("description.txt")
    # print(description)

    orgCntLetter = {}
    orgCntLetter = letterCounter(description)
    # print(orgCntLetter)

    writeDes = ""
    print("orgin")
    for i in orgCntLetter:
        print(str(i) + " = " + str(orgCntLetter[i]))
        writeDes += (str(i) + " = " + str(orgCntLetter[i]) + "\n")
    print("")
    fA.FileWrite("org.txt", writeDes)

    sortCnt = {}
    sortCnt = SortD(orgCntLetter)
    # print(sortCnt)
    writeDes = ""
    
    print("sorted")
    for i in sortCnt:
        print(str(i) + " = " + str(sortCnt[i]))
        writeDes += (str(i) + " = " + str(sortCnt[i]) + "\n")
    
    print("")
    for i, k in zip(orgCntLetter, sortCnt):
        print(i + " >> " + k)
    # print(sortCnt.__len__())
    writeDes.strip()
    fA.FileWrite("key.txt", writeDes)
    # Key = fA.FileRead("key.txt")
    # print("Key\n" + Key)
    print("Success generate Key!!!")
    
if __name__=='__main__':
    main()
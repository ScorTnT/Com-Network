def FileRead(route):
    print("")
    print("---File Open process---")
    print(route)
    readF = open(route, 'r')
    full = readF.read()
    #print(full)
    readF.close()
    print("---File Closed---")
    print("")
    return full

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
    description = FileRead("Assignment1/description.txt")
    # print(description)

    orgCntLetter = {}
    orgCntLetter = letterCounter(description)
    # print(orgCntLetter)

    for i in orgCntLetter:
        print(str(i) + " = " + str(orgCntLetter[i]))
    print("")

    sortCnt = {}
    sortCnt = SortD(orgCntLetter)
    # print(sortCnt)

    for i in sortCnt:
        print(str(i) + " = " + str(sortCnt[i]))
    
    print("")
    for i, k in zip(orgCntLetter, sortCnt):
        print(i+ " >> "+k)
    #print(sortCnt.__len__())

if __name__=='__main__':
    main()
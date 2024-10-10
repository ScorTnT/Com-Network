import fileAcc as fA

def letterCounter(descript_):
    print("\n---Count process---")
    SIZE = 26
    cnt = [0 for i in range(SIZE)]

    for k in descript_:
        if ('A' <= k) & (k <= 'Z'):
            cnt[ord(k)-65] += 1
        elif ('a' <= k) & (k <= 'z'):
            cnt[ord(k)-97] += 1

    makeDictionary = {}
    for i in range(SIZE):
        if cnt[i] == 0:
            continue
        alpha = chr(i+65)
        makeDictionary[alpha] = cnt[i]
    print("--- Fin. ---")
    print("")
    return makeDictionary

def SortD(diction_,instruction):
    return dict(sorted(diction_.items(),key=lambda x:x[instruction]))

def main():
    description = ""
    description = fA.FileRead("description.txt")

    orgCntLetter = {}
    orgCntLetter = letterCounter(description)
    orgCntLetter = dict(sorted(orgCntLetter.items(),key=lambda x:x[1]))
    writeDes = ""
    print("key")
    for i in orgCntLetter:
        print(str(i) + " = " + str(orgCntLetter[i]))
        writeDes += (str(i) + " = " + str(orgCntLetter[i]) + "\n")
    print("")
    fA.FileWrite("key.txt", writeDes)

    print("Success generate Key!!!")
    
if __name__=='__main__':
    main()
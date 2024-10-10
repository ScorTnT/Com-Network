def appendZero(a, b):
    tmp = "1"
    for i in range(b):
        tmp += "0"
    a += int(tmp)
    return a

def formToBit(polyno):
    result = 0
    tmp = 0
    polyno = polyno.split("+")
    print(polyno)

    for i in polyno:
        if i == "1":
            tmp = 0
            print(tmp)
            result = appendZero(result, tmp)
        if "x" in i:
            if "x" == i:
                tmp = 1
            else:
                tmp = int(i[1:])
            print(tmp)
            result = appendZero(result, tmp)
    

    return result

def main():
    # 1 1 0 1 1 0 0 0  >> 11011001
    # 1 0 1 0 0 0 0 0
    #   1 1 1 1 0 0 0 
    #   1 0 1 0 0 0 0 
    #     1 0 1 0 0 0  
    #     1 0 1 0 0 0 
    #         0 0 0 0 
    commandA = "x+1+x2+x4" #input('다항식 입력')
    commandB = "100101011" #input('데이터 입력')
    print(commandA, commandB)
    commandA = formToBit(commandA)
    print(commandA)

if __name__=='__main__':
    main()
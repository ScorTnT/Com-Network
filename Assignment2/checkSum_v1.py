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

    for i in polyno:
        if i == "1":
            tmp = 0
            result = appendZero(result, tmp)
        if "x" in i:
            if "x" == i:
                tmp = 1
            else:
                tmp = int(i[1:])
            result = appendZero(result, tmp)
    return result

def cal(a, b):
    org = b
    if len(b) > len(a):
        return a
    else:
        gap = len(a) - len(b)
        for i in range(gap):
            b+="0"
    # print(a,b)

    result = ""
    for i in range(len(a)):
        if a[i] != b[i]:
            result += "1"
        else:
            result += "0"
    result = result[result.find("1"):]
    # print (result)
    return cal(result, org)

def main():
    # 1 0 0 1 0 1 0 1 1 0 0 1 1 1
    # 1 0 1 1 1 0 0 0 0 
    #   0 1 0 1 1 0 1 1 
    #     1 0 1 1 1 0 0  
    #     0 0 0 0 1 1 1 
    #     1 0 1 0 0 0 
    #         0 0 0 0
    commandA = "x+1+x2+x4" #input('다항식 입력')
    commandB = "1001010" #input('데이터 입력')
    commandA = str(formToBit(commandA))
    print(commandB, commandA)
    result = cal(commandB, commandA)
    for i in range(len(commandA)):
        commandB += "0"
    # print(commandB, result)
    commandB = str(int(commandB) + int(result))
    # print(commandB, result)
    print(commandB)

if __name__=='__main__':
    main()
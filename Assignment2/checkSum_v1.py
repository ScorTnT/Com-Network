def appendZero(a, b):
    tmp = '1'
    for i in range(b):
        tmp += '0'
    a += int(tmp)

    return a

def formToBit(polyno):
    result = 0
    tmp = 0
    polyno = polyno.split('+')

    for i in polyno:
        if i == '1':
            tmp = 0
            result = appendZero(result, tmp)
        if 'x' in i:
            if 'x' == i:
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
            b+='0'

    result = ''
    for i in range(len(a)):
        if a[i] != b[i]:
            result += '1'
        else:
            result += '0'
    result = result[result.find('1'):]

    return cal(result, org)

def main():
    commandA = 'x+1+x2+x4' #input('다항식 입력')
    commandB = '1110110110010' #input('데이터 입력')
    print('전송 데이터: ' + commandB)
    commandA = str(formToBit(commandA))
    result = cal(commandB, commandA)
    for i in range(len(commandA)):
        commandB += '0'
    commandB = str(int(commandB) + int(result))
    print('전송될 데이터: ' + commandB)

if __name__=='__main__':
    main()
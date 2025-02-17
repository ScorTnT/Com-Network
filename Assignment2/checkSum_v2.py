def cal(data, polyno):
    org = polyno
    data = format(data, 'b')
    polyno = format(polyno, 'b')
    print(data, polyno)
    if len(data) < len(polyno):
        return data
    else:
        gap = len(data)-len(polyno)
        polyno = int(polyno,2)
        polyno = polyno<<gap
        polyno = format(polyno,'b')

    result = ''
    for i in range(len(data)):
        if data[i] != polyno[i]:
            result += '1'
        else:
            result += '0'
    
    return cal(int(result[result.find('1'):],2),org)

def formToint(polyno):
    result = 0
    polyno = polyno.split('+')
    
    for i in polyno:
        if 'x' in i:
            if i == 'x':
                result += 2
            else:
                result += 2**int(i[1:])
        else:
            result += 1

    return result

def main():
    commandA = input('다항식 입력') # 'x+1+x2+x4'
    commandB = int(input('전송 데이터 입력'),2) # int('1110110110010',2)
    commandA = formToint(commandA)
    commandB <<= len(format(commandA,'b'))-1
    print('계산에 사용할 전송 데이터: ' + format(commandB,'b'))
    result= cal(data=commandB, polyno=commandA)
    commandB += int(result,2)
    print('전송될 데이터: '+format(commandB,'b'))
    
if __name__=='__main__':
    main()
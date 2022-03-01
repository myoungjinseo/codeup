n= int(input(),16)      #16진수 표현문

for i in range(1,16):   
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')     # '%X'%n => 16 진수 형태로 출력  , sep='' => 공백 없이 모두 붙여서 출력
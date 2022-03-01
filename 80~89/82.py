a = int(input())

for i in range(1,a+1):
    if(i%10==3 or i%10==6 or i%10==9):      # 30이하의 수의 경우 3,6,9가 일의 자리에 있을 경우 박수를 친다.
        print('X', end=' ')         # end = ' ' => 한칸 띄움 , '' 일경우 공백없이
    else:
        print(i,end=' ')
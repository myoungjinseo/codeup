a,b,c,d = map(int,input().split())

result = a*b*c*d/8/(1024**2)

print(round(result,1),"MB")  # round() = 변수의 소수 값 반올림해준다. 
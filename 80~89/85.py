w,h,b = map(int,input().split())

result = w*h*b /8/(1024**2)

print("{0:.2f}".format(result),"MB")    # "{0:.Xf}".format(N) => N의 소수점 X자리까지 반올림
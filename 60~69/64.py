a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
if (min(a,b,c) == a):
    print(a)
elif(min(a,b,c) == b):
    print(b)
else:
    print(c)
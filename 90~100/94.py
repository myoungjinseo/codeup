n = int(input())
a = input().split()
j = 10001
for i in range(n):
    a[i] = int(a[i])
    if(j >a[i]):
        j =a[i] 

print(j)
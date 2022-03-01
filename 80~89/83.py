# r, g, b = input().split()

# r = int(r)
# g = int(g)
# b = int(b)

r,g,b = map(int,input().split())        # 기존의 방법대로 할 시 시간초과가 뜸 => map() 이용
count =0

for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i,j,k)
            count += 1
print(count)
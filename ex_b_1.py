import math
import sys
n,m = map(int,sys.stdin.readline().split(" "))
array = [True for i in range(m+1)] 

for i in range(2,int(math.sqrt(m))+1):  
  if array[i] == True: 
    j=2
    while i * j <= m:
      array[i*j] = False
      j+=1

for i in range(n,m+1):
  if array[i] and i>=2:
    print(i)

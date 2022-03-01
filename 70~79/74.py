c = ord(input())
t = ord('a')  #ord() == 문자를 유니코드로 변환
while t<=c :
  print(chr(t), end=' ')    # chr(정수) == 문자에 정수를 입력시 유니코드에 해당된 문자로 변환  
  t += 1
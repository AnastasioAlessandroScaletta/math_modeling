a = int(input("Введите число: "))
b = 0

while a>0:
  b = a%10
  a = a//10
  print(b, end='')
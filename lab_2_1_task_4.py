a = int(input("Введите число: "))
b = 2
c = 0

while a > 1:
  while 1:
    if a%b == 0:
      a = a // b
      print(b, end=' ')
      c = 1
      break
    else:
      b += 1
  if c == 1:
    continue
print()
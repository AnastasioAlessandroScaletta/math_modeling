a = int(input("Введите число: "))
b = 1

while b <= a:
  c = 0
  d = 1
  while d < b:
    if not b % d:
      c += d
    d = d + 1
  if c == b:
    print(b)
  b = b + 1
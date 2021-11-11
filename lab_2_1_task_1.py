a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))

print(f"{a}x^2 + {b}x + {c} = 0") 
d = b ** 2 - 4 * a * c
print(f"Дискриминант равен {d}")

if d > 0:
  print(f"x1 = {(-b + (d ** 0.5)) / (2 * a)}")
  print(f"x2 = {(-b - (d ** 0.5)) / (2 * a)}")
elif d == 0:
  print(f"x = {-b / (2 * a)}")
else:
  print("Корней нет")
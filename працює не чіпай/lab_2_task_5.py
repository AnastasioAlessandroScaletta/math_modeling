a = int(input())
b = int(input())
if b == 0:
  print("Делитель не может быть равен 0")
elif a%b == 0:
  print(f"{a} делится на {b}")
  print(f"Частное: {a // b}")
else:
  print(f"{a} не делится на {b}")
  print(f"Остаток: {a % b}")
  print(f"Частное: {a // b}")
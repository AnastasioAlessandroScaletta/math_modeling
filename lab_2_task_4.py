a = int(input())
n1 = 1
n2 = 2
print(n1, n2, end=' ')
for i in range(3, a+1):
    print(n1+n2, end=' ')
    b = n1
    n1 = n2
    n2 = b+n1
print()
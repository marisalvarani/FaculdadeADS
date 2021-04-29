n = input().split()

n1 = int(n[0])
n2 = int(n[1])

lst = []

while n1>0:
    nome = input()
    n1 = n1 - 1
    lst.append(nome)


lst.sort()

print(lst[((n2)-1)])





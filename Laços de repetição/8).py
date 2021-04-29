n1 = int(input())
n2 = int(input())

while n1<1 or n1>9:
        n1 = int(input("Insira um número inicial entre 1 e 9"))
while n2<1 or n2>9:
        n2 = int(input("Insira um número final entre 1 e 9"))

if n1>n2:
    print("Nenhuma tabuada nesse intervalo")

else:  
    cont = 0
    soma = 0
    while cont<=n2-1:
        cont = soma + n1
        soma = soma + 1
        for x in range (1,10):
            print(cont, "x", x, "=", cont*x)
        print()
            

    




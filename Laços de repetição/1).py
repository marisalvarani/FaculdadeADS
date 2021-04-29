x = int(input())
n = int(input())
soma = 1
cont = 0
while (soma*x)<n:
       soma = soma + 1
    
print("O numero",x,"tem",soma-1,"multiplos menores que","{:.0f}.".format(n))

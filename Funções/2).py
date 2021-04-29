n = int(input())
import math

def eh_primo(n):
    b = 0
    for x in range(1,n+1):
        if n%x==0:
            b = b + 1
    if b == 2:
        primo = True
    else:
        primo = False
        
    
    return primo


print(eh_primo(n))



    
def lista_primos(n):
    lista = []
    for x in range(1,n):
        b = 0
        for i in range(1,n+1):
            if x%i==0:
                b = b + 1
        if b == 2:
            lista.append(x)
           

    return lista

print(lista_primos(n))



def eh_armstrong(n):
    cont = 0
    s = 0
    b = n
    c = n
    while n>0:
        cont = cont + 1
        n=n//10
    
    while b>0:
        s = s + math.pow((b%10),cont)
        b = b//10
    
    if c==s:
        arms = True
    else:
        arms = False


    return arms

print(eh_armstrong(n))



def lista_armstrong(n):
    lista = []
    for x in range(1,n):
        if eh_armstrong(x) == True:
            lista.append(x)

    return lista

print(lista_armstrong(n))



def eh_perfeito(n):
    s = 0
    for x in range (1,n):
        if n%x==0:
            s = s + x

    if s == n:
        perfeito = True
    else:
        perfeito = False

    return perfeito

print(eh_perfeito(n))


def lista_perfeitos(n):
    lista = []
    for x in range(1,n):
        if eh_perfeito(x) == True:
            lista.append(x)

    return lista

print(lista_perfeitos(n))

        

  

        
            

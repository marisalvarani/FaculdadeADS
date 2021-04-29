d = input().split()
n = []
for x in d:
    n.append(int(x))
    
def contaDigitos(d):
    l = []
    c = 0
    for x in (d):
        cont = 0
        c = x
        for item in (c):
            cont = cont + 1
        l.append(int(cont))
    return l

def ehBissexto(n):
    b = 0
    for x in (n):
        if x%4==0 and x%100!=0:
            b = 1
        elif x%4==0 and x%100==0 and x%400==0:
            b = 2
        else:
            b = 3
    return b

def Mensagem(n):
    for x in (contaDigitos(d)):
        if x<4 :
            print("Ano invalido")
        else:
            for x in (n):
                if (ehBissexto(n) == 1 or ehBissexto(n) == 2) and x<2018:
                    print("O ano",x,"foi bissexto")
                elif (ehBissexto(n) == 1 or ehBissexto(n) == 2) and x>2018:
                    print("O ano",x,"serah bissexto")
                elif x==2018:
                    print("O ano",x,"NAO eh bissexto")
                else:
                    print("O ano",x,"NAO eh bissexto")
     

    


print(Mensagem(n))


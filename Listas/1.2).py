cadeia=[]
aux=[]

def contaDigitos(ano):  
    cont = 0
    for c in ano:    
        if c.isdigit():  
            cont = cont + 1  
    if cont==4:  
        aux=int(ano)  
        ehBissexto(aux)  
         
    else:
        print('Ano invalido')  

def ehBissexto(ano):   
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        if ano<2018:
            print(f'O ano {ano} foi bissexto')
        elif ano ==2018:
            print(f'O ano {ano} eh bissexto')
        else:
            print(f'O ano {ano} serah bissexto')

                   

    else:

        if ano<2018:
            print(f'O ano {ano} NAO eh bissexto')
        elif ano==2018:
            print(f'O ano {ano} NAO eh bissexto')
        else:
            print(f'O ano {ano} NAO eh bissexto')
        
def Mensagem(cadeia): 
    global aux
        
    for i in cadeia.split():
        aux.append(i)
        contaDigitos(i)

Mensagem(input())

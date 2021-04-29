seq = str(input())
carac = str(input())
soma = 0


for x in seq:
    if carac == x:
       soma = soma + 1
    else:
        soma = soma

if soma == 0:
    print("Caractere nao encontrado.")
else:
    print("O caractere buscado ocorre",soma,"vezes na sequencia.")
              
        

        
        
    



    

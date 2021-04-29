n = int(input("Digite a quantidade de nomes:" ))

lst_nomes = []

while n<3 or n>10:
    n = int(input("Digite a quantidade de nomes entre 4 e 9:" ))

for x in range(1,n):
    nome = str(input("Digite o nome:" ))
    lst_nomes.append(nome)

print("Nomes digitados:", lst_nomes)

lst_nomes.insert(3, "Teste")
print("Lista após incluir 'Teste' no índice 3:",lst_nomes)

del lst_nomes[2]
print("Lista após excluir o elemeno de índice 2",lst_nomes)

qtde = lst_nomes.count("Ana")

if qtde > 0:
    print("Índice da primeira ocorrência do nome Ana na lista:", lst_nomes.index("Ana"))
else:
     print("Não existe o nome Ana na lista")


lst_nomes.sort()

print("Lista ordenada:",lst_nomes)




    

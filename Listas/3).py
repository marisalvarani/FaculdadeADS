l = [int(char)for char in input().split()]

while True:
    comando = input()
    acao = comando.split()[0]
    if acao == "inserir":
        l.append(int(comando.split()[1]))
    elif acao == "remover":
        l.remove(int(comando.split()[1]))
    elif acao == "parcial":
        l.sort()
        print(*l)
    else: break

l.sort()
print(*l)
        


l = input().split()

l1 = int(l[0])
l2 = int(l[1])
l3 = float(l[2])

lst_codigo = []
lst_qtde = []
lst_custo = []
custo = 0
lst_codigo.append(l1)
lst_qtde.append(l2)
lst_custo.append(l2*l3)

if l1==0 and l2==0 and l3==0:
    print("nao tem compras")
else:
    while l1!=0 and l2!=0 and l3!=0:
        l = input().split()
        l1 = int(l[0])
        l2 = int(l[1])
        l3 = float(l[2])
        lst_codigo.append(l1)
        lst_qtde.append(l2)
        custo = l2*l3
        lst_custo.append(custo)
    maxcusto = lst_custo.index(max(lst_custo))
    print("Item mais caro")
    print("Codigo:",lst_codigo[maxcusto])
    print("Quantidade:",lst_qtde[maxcusto])
    print("Custo:","{:.2f}".format(max(lst_custo)))      

        
    


        
        
        
        
    

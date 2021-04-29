i = int(input())

if i<16:
    print("nao eleitor")
elif i>=18 and i<=65:
    print("eleitor obrigatorio")
else:
    print("eleitor facultativo")

n1=int(2)
n2=int(11)

for n in range(n1,n2):
    ePrimo = True
    for x in range(2,n):
        if n%2==0:
            ePrimo = False

        if ePrimo == True:
            print(n)

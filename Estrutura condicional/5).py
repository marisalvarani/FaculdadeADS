S = float(input())
I = S*0.08
II = S*0.09
III = S*0.11
IIII = 5839.45*0.11
if S<=1751.81:
    print("Desconto do INSS: R$", "{:.2f}".format(I))
elif S>1751.81 and S<=2919.72:
    print("Desconto do INSS: R$", "{:.2f}".format(II))
elif S>2919.72 and S<=5839.45:
    print("Desconto do INSS: R$", "{:.2f}".format(III))
else:
    print("Desconto do INSS: R$", "{:.2f}".format(IIII))

x = float(input())
import math

a = x/7
aa = math.ceil(a/24)
aaa = aa*91

b = math.ceil(a/5.4)
bb = b*23

c = math.floor(a/24)
cc = math.ceil((a%24)/5.4)
ccc = c*91
cccc = cc*23
ccccc = ccc+cccc

print("a)",aa, "lata(s) de 24 litros: R$", "{:.2f}".format(aaa))
print ("b)",b, "lata(s) de 5.4 litros: R$", "{:.2f}".format(bb))
print("c)",c, "lata(s) de 24 litros e",cc, "lata(s) de 5.4 litros: R$", "{:.2f}".format(ccccc))

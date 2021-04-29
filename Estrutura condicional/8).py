n = float(input())

a1 = n//100
a2 = n%100
b1 = a2//50
b2 = a2%50
c1 = b2//20
c2 = b2%20
d1 = c2//10
d2 = c2%10
e1 = d2//5
e2 = d2%5
f1 = e2//2
f2 = e2%2
g1 = f2//1
g2 = f2%1
h1 = (g2*100)//50
h2 = (g2*100)%50
i1 = h2//25
i2 = h2%25
j1 = i2//10
j2 = i2%10
k1 = j2//5
k2 = j2%5
l1 = k2/1


if a1>0:
    print("{:.0f}".format(a1),"nota(s) de R$ 100.00")
if b1>0:
    print("{:.0f}".format(b1),"nota(s) de R$ 50.00")
if c1>0:
    print("{:.0f}".format(c1),"nota(s) de R$ 20.00")
if d1>0:
    print("{:.0f}".format(d1),"nota(s) de R$ 10.00")
if e1>0:
    print("{:.0f}".format(e1),"nota(s) de R$ 5.00")
if f1>0:
    print("{:.0f}".format(f1),"nota(s) de R$ 2.00")
if g1>0:
    print("{:.0f}".format(g1),"moeda(s) de R$ 1.00")
if h1>0:
    print("{:.0f}".format(h1),"moeda(s) de R$ 0.50")
if i1>0:
    print("{:.0f}".format(i1),"moeda(s) de R$ 0.25")
if j1>0:
    print("{:.0f}".format(j1),"moeda(s) de R$ 0.10")
if k1>0:
    print("{:.0f}".format(k1),"moeda(s) de R$ 0.05")
if l1>0:
    print("{:.0f}".format(l1),"moeda(s) de R$ 0.01")

n = int(input())

c=0
s=0

while (c<n):
    c = c + 1
    if c%2 !=0:
        s = s -(1/c)
    else:
        s = s +(1/c)

print("{:.6f}".format(s))

        


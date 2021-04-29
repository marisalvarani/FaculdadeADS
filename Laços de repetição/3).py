n = int(input())

c=0
s=0


while (c<n):
    c = c + 1
    s = s +(1/(c*c))

print("{:.6f}".format(s))

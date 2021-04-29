s1 = int(input())
s2 = int(input())
s3 = int(input())
s4 = int(input())
s5 = int(input())
s6 = int(input())
s7 = int(input())

media = (s1 + s2 + s3 + s4 + s5 + s6 + s7)/7

l = [s1,s2,s3,s4,s5,s6,s7]
soma = 0

for x in l:
    if x>=100:
        soma = soma + 1

print(soma)
print("{:.0f}".format(media))
        

from animais import *

r1 = Reptil('Cobra', 'Verde', 4)
print(Reptil.botar_ovo(r1))
print(Reptil.tomar_sol(r1))

m1 = Mamifero('Leão', 'Caramelo', 7, 'pata')
print(Mamifero.mamar(m1))
print(Mamifero.correr(m1))

c1 = Camaleao('Django', 'verde', 4, 'mosca')
print(Camaleao.mudar_de_cor(c1))
print(Camaleao.comer_inseto(c1))

cavalo = Cavalo('Carpeado', 'marrom', 11, 'pata', 'marrom')
print(Cavalo.galopar(cavalo))
print(Cavalo.relinchar(cavalo))
print(Cavalo.mamar(cavalo))

gato = Gato('Belo', 'marrom', '7', 'pata')
print(Gato.miar(gato))
print(Gato.morrer(gato))

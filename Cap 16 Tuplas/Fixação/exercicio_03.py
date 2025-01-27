from math import sqrt

def calc_distancia(ponto1, ponto2):
    dist = (ponto1[0] - ponto2[0]) ** 2 + (ponto1[1] - ponto2[1]) ** 2 + (ponto1[2] - ponto2[2]) ** 2
    return sqrt(dist) 


x = float(input("Informe a coordenada x do ponto 1: "))
y = float(input("Informe a coordenada y do ponto 1: "))
z = float(input("Informe a coordenada x do ponto 1: "))
ponto1 = (x, y, z)

x = float(input("Informe a coordenada x do ponto 2: "))
y = float(input("Informe a coordenada y do ponto 2: "))
z = float(input("Informe a coordenada x do ponto 2: "))
ponto2 = (x, y, z)

print("A distância entre os pontos é de", calc_distancia(ponto1, ponto2))
from math import sqrt

def ponto_medio(ponto1, ponto2):
    x = (ponto1[0] + ponto2[0]) / 2
    y = (ponto1[1] + ponto2[1]) / 2
    
    return (x, y)


x = float(input("Informe a coordenada x do ponto 1: "))
y = float(input("Informe a coordenada y do ponto 1: "))
ponto1 = (x, y)

x = float(input("Informe a coordenada x do ponto 2: "))
y = float(input("Informe a coordenada y do ponto 2: "))
ponto2 = (x, y)

print("O ponto médio entre os pontos é", ponto_medio(ponto1, ponto2))
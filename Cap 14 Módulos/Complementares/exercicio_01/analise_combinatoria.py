def fatorial(n):
    produto = 1
    for e in range(n, 0, -1):
        produto = produto * e
    return produto

def permutacao(n):
    return fatorial(n)


def arranjo(n, k):
    return fatorial(n) / fatorial(n - k)


def combinacao(n, k):
    return fatorial (n) / (fatorial(k) * fatorial(n - k))

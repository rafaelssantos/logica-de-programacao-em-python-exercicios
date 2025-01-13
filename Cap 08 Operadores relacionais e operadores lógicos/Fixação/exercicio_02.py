p = 8
q = 4
r = 2
resultado = (p - q * r <= q) and (not (r ** 2 > p))

# resultado = (8 - 4 * 2 <= 4) and (not (2 ** 2 > 8))
# resultado = (8 - 8 <= 4) and (not (4 > 8))
# resultado = (0 <= 4) and (not (False))
# resultado = (True) and (not False)
# resultado = True and True
# resultado = True
valores = [3, 6, 1]
resultado = 10

for valor in valores:
    if valor > 4:
        resultado += valor
    else:
        resultado -= 2

print("el resultado es:", resultado)
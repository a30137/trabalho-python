n1 = int(input("Valor da compra: "))

if n1 < 50:
    percentagem = 0
elif n1 <= 100:
    percentagem = 5
else:
    percentagem = 10

desconto = n1 * (percentagem / 100)
preco_final = n1 - desconto

print("Valor da compra:", n1, "€")
print("Desconto aplicado:", percentagem, "%")
print("Valor do desconto:", desconto, "€")
print("Preço final:", preco_final, "€")
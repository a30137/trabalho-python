def CalcularPrecoFinal(preco, desconto):
    valor_desconto = (preco * desconto / 100)
    preco_final = preco - valor_desconto
    return preco_final


preço = float(input("Introduza o preço: "))
desconto_ = float(input("Introduza a percentagem de desconto: "))

resultado = CalcularPrecoFinal(preço, desconto_)

print(f"O preço final é: {resultado}")
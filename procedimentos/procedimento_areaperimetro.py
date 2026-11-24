def CalcularRetangulo(comprimento, largura):
    area = comprimento * largura
    perimetro = 2 * (comprimento + largura)
    
    return area, perimetro

comprimento = float(input("Introduza o comprimento: "))
largura = float(input("Introduza a largura: "))

área, perímetro = CalcularRetangulo(comprimento, largura)

print(f"Área: {área}cm²")
print(f"Perímetro: {perímetro}cm")

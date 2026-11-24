def media(a, b, c):
    return float(a+b+c)/3


num1 = float(input("Introduza o primeiro número: "))
num2 = float(input("Introduza o segundo número: "))
num3 = float(input("Introduza o terceiro número: "))

resultado = media(num1, num2, num3)

print(f"A média é: {resultado}")
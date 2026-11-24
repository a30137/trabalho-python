import os
os.system("cls") # limpar ecrâ do termina]


def Media(a, b, c):
    media = (a + b + c) / 3
    return media


num1 = int(input("Introduza o primeiro número: "))
num2 = int(input("Introduza o segundo número: "))
num3 = int(input("Introduza o terceiro número: "))

resultado_media = Media(10, 11, 12)

print(f"Média = resultado_media:")
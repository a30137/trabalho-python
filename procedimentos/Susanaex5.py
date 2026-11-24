import os
os.system("cls")

def calcular_media(notas):
    return sum(notas) / len(notas)

def contar_positivas(notas):
    contador = 0
    for nota in notas:
        if nota >= 10:
            contador = contador + 1
    return contador

def contar_bons(notas):
    contador = 0
    for nota in notas:
        if 14 <= nota <= 17:
            contador = contador + 1
    return contador

def contar_excelentes(notas):
    contador = 0
    for nota in notas:
        if 18 <= nota <= 20:
            contador = contador + 1
    return contador

def mostrar_relatorio(notas):
    media = calcular_media(notas)
    positivas = contar_positivas(notas)
    negativas = len(notas) - positivas
    bons = contar_bons(notas)
    excelentes = contar_excelentes(notas)

    print("\nRELATÓRIO DA TURMA")
    print("Lista das classificações:", notas)
    print(f"A média da turma é: {media:.5f}")
    print("A maior classificação é:", max(notas))
    print("A menor classificação é:", min(notas))
    print("O número de classificações positivas é:", positivas)
    print("O número de classificações negativas é:", negativas)
    print("O número de alunos com Bom é:", bons)
    print("O número de alunos com Excelente é:", excelentes)

notas = []

for i in range(10):
    nota = float(input(f"Introduza a classificação do aluno {i + 1}: "))
    notas.append(nota)

mostrar_relatorio(notas)

print("Trabalho realizado por Susana Ferreira Nº24.")
print(" ")
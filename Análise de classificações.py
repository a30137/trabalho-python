
notas = []

for i in range(1, 11):
    nota = float(input(f"Introduza a classificação do aluno {i}: "))
    notas.append(nota)


def calcular_media(notas):
    return sum(notas) / len(notas)


def contar_positivas(notas):
    contador = 0
    for nota in notas:
        if nota >= 10:
            contador += 1
    return contador


def contar_bons(notas):
    contador = 0
    for nota in notas:
        if nota >= 14 and nota <= 17:
            contador += 1
    return contador


def contar_excelentes(notas):
    contador = 0
    for nota in notas:
        if nota >= 18 and nota <= 20:
            contador += 1
    return contador


def mostrar_relatorio(notas):

    media = calcular_media(notas)
    positivas = contar_positivas(notas)
    negativas = 10 - positivas
    bons = contar_bons(notas)
    excelentes = contar_excelentes(notas)

    print("\n------ RELATÓRIO DA TURMA ------")

    print("Lista das classificações:", notas)
    print(f"Média da turma: {media:.2f}")
    print("Maior classificação:", max(notas))
    print("Menor classificação:", min(notas))
    print("Classificações positivas:", positivas)
    print("Classificações negativas:", negativas)
    print("Alunos com Bom:", bons)
    print("Alunos com Excelente:", excelentes)


mostrar_relatorio(notas)


print("\nTrabalho realizado por Pedro Guimarães, nº 20")

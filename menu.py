import os
import random

def limpar_ecra():
    os.system("cls" if os.name == "nt" else "clear")

def maiormenor():
    def maior(a, b):
        return a if a > b else b

    num1 = int(input("Introduza o primeiro número: "))
    num2 = int(input("Introduza o segundo número: "))
    print(f"O maior número é: {maior(num1, num2)}")

def medias():
    print("Calcular Médias")
    print("1 - Média de 3 números (função)")
    print("2 - Média de 4 números")
    print("3 - Média de 10 números (de 1 a 10)")
    print("4 - Média de 10 números (escolha)")
    op = input("Escolha uma opção: ")

    if op == "1":
        def media(a, b, c):
            return float(a + b + c) / 3
        n1 = float(input("Introduza o primeiro número: "))
        n2 = float(input("Introduza o segundo número: "))
        n3 = float(input("Introduza o terceiro número: "))
        print(f"A média é: {media(n1, n2, n3):.2f}")
    elif op == "2":
        soma = 0
        for i in range(1, 5):
            soma += int(input(f"Introduza o {i}º número: "))
        print(f"Média: {soma / 4}")
    elif op == "3":
        soma = sum(range(1, 11))
        print(f"Média dos números de 1 a 10: {soma / 10}")
    elif op == "4":
        soma = 0
        for i in range(1, 11):
            soma += int(input(f"Introduza o {i}º número: "))
        print(f"Média: {soma / 10}")
    else:
        print("Opção inválida.")

def somaproduto():
    def calcular_resultados(n1, n2):
        return n1 + n2, n1 * n2

    n1 = int(input("Introduza o primeiro número: "))
    n2 = int(input("Introduza o segundo número: "))
    soma, produto = calcular_resultados(n1, n2)
    print(f"Soma: {soma}")
    print(f"Produto: {produto}")

def retangulo():
    def calcular_retangulo(comprimento, largura):
        area = comprimento * largura
        perimetro = 2 * (comprimento + largura)
        return area, perimetro

    comp = float(input("Introduza o comprimento: "))
    larg = float(input("Introduza a largura: "))
    area, perimetro = calcular_retangulo(comp, larg)
    print(f"Área: {area} cm²")
    print(f"Perímetro: {perimetro} cm")

def somaate100():
    soma = 0
    while soma <= 100:
        num = float(input("Digite um número: "))
        soma += num
        print(f"Soma atual: {soma}")
    print(f"A soma final é {soma}, que ultrapassou 100.")

def desconto():
    def calcular_preco_final(preco, desconto):
        valor_desconto = preco * desconto / 100
        return preco - valor_desconto

    preco = float(input("Introduza o preço: "))
    desconto = float(input("Introduza a percentagem de desconto: "))
    print(f"O preço final é: {calcular_preco_final(preco, desconto):.2f} €")

def desconto_v2():
    n1 = float(input("Valor da compra: "))
    if n1 < 50:
        percentagem = 0
    elif n1 <= 100:
        percentagem = 5
    else:
        percentagem = 10

    desconto = n1 * (percentagem / 100)
    preco_final = n1 - desconto
    print(f"Valor da compra: {n1:.2f} €")
    print(f"Desconto aplicado: {percentagem}%")
    print(f"Valor do desconto: {desconto:.2f} €")
    print(f"Preço final: {preco_final:.2f} €")

def viagemtaxi():
    distancia = float(input("Distância (km): "))
    if distancia <= 5:
        preco = 5
    elif distancia <= 15:
        preco = 5 + distancia * 0.80
    else:
        preco = 13 + distancia * 0.60
    print(f"A viagem custa {preco:.2f} €.")

def aprovadoreprovado():
    n1 = float(input("Introduza a primeira nota: "))
    n2 = float(input("Introduza a segunda nota: "))
    n3 = float(input("Introduza a terceira nota: "))
    media = (n1 + n2 + n3) / 3
    print(f"Média: {media:.1f}")
    print("Aluno aprovado" if media >= 10 else "Aluno reprovado")

def contarpositivas():
    contador = 0
    for aluno in range(1, 9):
        nota = float(input(f"Classificação do aluno {aluno}: "))
        if nota >= 10:
            contador += 1
    print("Número de classificações positivas:", contador)

def relatorioturma():
    def calcular_media(notas): return sum(notas) / len(notas)
    def contar_positivas(notas): return sum(1 for n in notas if n >= 10)
    def contar_bons(notas): return sum(1 for n in notas if 14 <= n <= 17)
    def contar_excelentes(notas): return sum(1 for n in notas if 18 <= n <= 20)

    notas = []
    for i in range(10):
        nota = float(input(f"Introduza a classificação do aluno {i + 1}: "))
        notas.append(nota)

    media = calcular_media(notas)
    positivas = contar_positivas(notas)
    negativas = len(notas) - positivas

    print("RELATÓRIO DA TURMA")
    print("Lista das classificações:", notas)
    print(f"A média da turma é: {media:.2f}")
    print("A maior classificação é:", max(notas))
    print("A menor classificação é:", min(notas))
    print("Classificações positivas:", positivas)
    print("Classificações negativas:", negativas)
    print("Alunos com Bom:", contar_bons(notas))
    print("Alunos com Excelente:", contar_excelentes(notas))
    print("Trabalho realizado por Susana Ferreira Nº24.")

def classificacoesaleatorias(lista_notas):
    print("\n--- Classificações Geradas Aleatoriamente ---")
    for indice, nota in enumerate(lista_notas, start=1):
        print(f"Aluno {indice}: {nota} valores")

def vitorias_v1():
    jogos = int(input("Número de jogos: "))
    vitorias = int(input("Número de vitórias: "))
    if vitorias > jogos / 2:
        print("Muito bom, campanha positiva!")
    else:
        print("Mau, podes melhorar.")

def vitorias_v2():
    jogos = int(input("Número de jogos: "))
    vitorias = int(input("Número de vitórias: "))
    empates = int(input("Número de empates: "))
    print("Pontos possíveis:", jogos * 3)
    print("Pontos obtidos:", vitorias * 3 + empates)
    print("Muito bom, campanha positiva" if vitorias > jogos / 2 else "Mau, podes melhorar.")

def vitorias_v3():
    jogos = int(input("Número de jogos: "))
    vitorias = int(input("Número de vitórias: "))
    empates = int(input("Número de empates: "))

    if jogos < (vitorias + empates):
        print("Erro: A soma de vitórias e empates excede o número de jogos.")
        return

    pontos_possiveis = jogos * 3
    pontos_obtidos = vitorias * 3 + empates
    derrotas = jogos - vitorias - empates
    pontos_perdidos = pontos_possiveis - pontos_obtidos

    print(f"Derrotas: {derrotas}")
    print(f"Pontos possíveis: {pontos_possiveis}")
    print(f"Pontos obtidos: {pontos_obtidos}")
    print(f"Pontos perdidos: {pontos_perdidos}")
    print("Muito bom, campanha positiva" if vitorias > jogos / 2 else "Mau, podes melhorar.")

def adivinharnumero():
    numero = random.randint(1, 100)
    tentativas = 0
    acertou = False
    while not acertou:
        palpite = int(input("Tenta adivinhar o número entre 1 e 100: "))
        tentativas += 1
        if palpite == numero:
            acertou = True
            print(f"Acertaste! Precisaste de {tentativas} tentativa(s).")
        elif palpite < numero:
            print("O número é maior. Tenta outra vez.")
        else:
            print("O número é menor. Tenta outra vez.")

def mediatemperaturas():
    soma = 0
    for dia in range(1, 8):
        soma += float(input(f"Temperatura do dia {dia}: "))
    print(f"Soma das temperaturas: {soma}")
    print(f"Temperatura média: {soma / 7:.2f}")

def vetores():
    marcas = []
    for i in range(5):
        marcas.append(input(f"Introduza a {i + 1}.ª marca de automóvel: "))
    print("Marcas guardadas no vetor:")
    for marca in marcas:
        print("-", marca)

def ishappy():
    isHappy = True
    print("You are happy!" if isHappy else "You are not happy!")

def menu_matematica():
    while True:
        print("MATEMÁTICA")
        print("1 - Maior de 2 números")
        print("2 - Calcular Médias (3, 4 ou 10 números)")
        print("3 - Soma e Produto de 2 números")
        print("4 - Área e Perímetro de um Retângulo")
        print("5 - Somar números até ultrapassar 100")
        print("0 - Voltar")
        op = input("Escolha uma opção: ")

        if op == "1": maiormenor()
        elif op == "2": medias()
        elif op == "3": somaproduto()
        elif op == "4": retangulo()
        elif op == "5": somaate100()
        elif op == "0": break

def menu_comercio():
    while True:
        print("COMÉRCIO")
        print("1 - Calcular Preço com Desconto (manual)")
        print("2 - Calcular Preço com Desconto (escalões automáticos)")
        print("3 - Calcular Preço de Viagem de Táxi")
        print("0 - Voltar")
        op = input("Escolha uma opção: ")

        if op == "1": desconto()
        elif op == "2": desconto_v2()
        elif op == "3": viagemtaxi()
        elif op == "0": break

def menu_escola(notas_aleatorias):
    while True:
        print("ESCOLA")
        print("1 - Ver lista de classificações aleatórias")
        print("2 - Verificar Aluno Aprovado/Reprovado (3 notas)")
        print("3 - Contar Classificações Positivas (8 alunos)")
        print("4 - Relatório da Turma (10 alunos)")
        print("0 - Voltar")
        op = input("Escolha uma opção: ")
        if op == "1": classificacoesaleatorias(notas_aleatorias)
        elif op == "2": aprovadoreprovado()
        elif op == "3": contarpositivas()
        elif op == "4": relatorioturma()
        elif op == "0": break

def menu_desporto():
    while True:
        print("DESPORTO")
        print("1 - Avaliação de Vitórias (Simples)")
        print("2 - Avaliação de Vitórias (Com pontos)")
        print("3 - Avaliação de Vitórias (Com validação)")
        print("0 - Voltar")
        op = input("Escolha uma opção: ")
        if op == "1": vitorias_v1()
        elif op == "2": vitorias_v2()
        elif op == "3": vitorias_v3()
        elif op == "0": break

def menu_outros():
    while True:
        print("OUTROS")
        print("1 - Jogo: Adivinhar o Número")
        print("2 - Média de Temperaturas (7 dias)")
        print("3 - Vetor de Marcas de Automóveis")
        print("4 - Programa 'isHappy'")
        print("0 - Voltar")
        op = input("Escolha uma opção: ")
        if op == "1": adivinharnumero()
        elif op == "2": mediatemperaturas()
        elif op == "3": vetores()
        elif op == "4": ishappy()
        elif op == "0": break

limpar_ecra()
notas_iniciais = [random.randint(1, 20) for _ in range(10)]
while True:
    print("MENU PRINCIPAL")
    print("1 - Matemática")
    print("2 - Comércio")
    print("3 - Escola")
    print("4 - Desporto (Vitórias)")
    print("5 - Outros")
    print("0 - Sair")
    opcao = input("Escolha uma categoria: ")
    limpar_ecra()
    if opcao == "1": menu_matematica()
    elif opcao == "2": menu_comercio()
    elif opcao == "3": menu_escola(notas_iniciais)
    elif opcao == "4": menu_desporto()
    elif opcao == "5": menu_outros()                    
    elif opcao == "0":
        print("Até à próxima!")
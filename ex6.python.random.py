import random 

numero = random.randint (0,100)
valor_utilizador = int(input("advinhe o numero entre 0 e 100:"))
tentativas=1

while valor_utilizador != numero:
    if valor_utilizador < numero:
        print("O numero é maior")
    else:
        print("O numero é menor")
    valor_utilizador = int(input("tenta de novo:"))
    tentativas += 1
    print(f"Tentativa {tentativas}: {valor_utilizador}.")

print(f"Fim de jogo.")
print(f"Acertou o numero em {tentativas} tentativas.")
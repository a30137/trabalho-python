import os
os.system("cls")

contador = 0 
for aluno in range(1, 9): 
    nota = float(input(f"Classificação do aluno {aluno}: ")) 

    if nota >= 10: 
        contador += 1
        
print("Número de classificações positivas:", contador)
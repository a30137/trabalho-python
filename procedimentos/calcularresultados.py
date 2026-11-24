def CalcularResultados(n1, n2):
    soma = n1 + n2
    produto = n1 * n2
    
    return soma, produto


n1 = int(input("Introduza o primeiro número: "))
n2 = int(input("Introduza o segundo número: "))

    
resultado_soma, resultado_produto = CalcularResultados(n1, n2)

    
print(f"Soma: {resultado_soma}")
print(f"Produto: {resultado_produto}")

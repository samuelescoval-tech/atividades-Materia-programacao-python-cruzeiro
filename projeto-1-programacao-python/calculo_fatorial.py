# Projeto 1 - Cálculo de Fatorial

import math

# Converte o valor digitado pelo usuário de string para inteiro
numero_escolhido = int(input("Digite o número para calcular o fatorial: "))

resultado = math.factorial(numero_escolhido)

print(f"O fatorial de {numero_escolhido}! é {resultado}")
#  DIA 2 – Laços de repetição (while e for), contadores e acumuladores

# 1. Contagem até 10
# Solicite um número inicial e imprima de 1 até 10 usando while.

"""
num = int(input("Digite um número: "))

if num > 10:
    print("O número é maior que 10. Nada a contar.")
else:
    while num <= 10:
        print(num)
        num += 1
"""
# 2. Contagem regressiva
# Solicite um número e mostre a contagem regressiva até 0.

num =  int(input("Digite um número: "))

if num <= 0 :
    print("Digite um número maior que 0")
else:
    print("Contagem regressiva")
    while num >= 0:
        print(num)
        num -= 1

# 3. Soma de números positivos
# Peça números positivos até que o usuário digite 0. Ao final, exiba a soma total.

# 4. Senha com repetição
# Solicite uma senha ao usuário e repita até que ele acerte a senha correta ("1234").

# 5. Média de várias notas
# Peça notas ao usuário até que ele digite -1. Calcule a média das notas inseridas.

# 6. Tabuada personalizada
# Peça um número e exiba sua tabuada de 1 a 10.

# 7. Contagem de pares e ímpares
# Solicite 10 números e diga quantos são pares e quantos são ímpares.

# 8. Soma dos múltiplos de 3 entre 1 e 100
# Use um laço for para somar os múltiplos de 3 de 1 a 100.

# 9. Fatorial de um número
# Peça um número e calcule o seu fatorial com for.

# 10. Contagem de vogais em uma palavra
# Peça uma palavra ao usuário e diga quantas vogais ela contém.

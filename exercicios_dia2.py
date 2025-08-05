# DIA 2 – Laços de repetição (while e for), contadores e acumuladores

# 1. Contagem até 10
# Solicite um número inicial e imprima de 1 até 10 usando while.

num = int(input("Digite um número: "))

if num > 10:
    print("O número é maior que 10. Nada a contar.")
else:
    while num <= 10:
        print(num)
        num += 1

# 2. Contagem regressiva
# Solicite um número e mostre a contagem regressiva até 0.

num = int(input("Digite um número: "))

if num <= 0:
    print("Digite um número maior que 0")
else:
    print("Contagem regressiva")
    while num >= 0:
        print(num)
        num -= 1

# 3. Soma de números positivos
# Peça números positivos até que o usuário digite 0. Ao final, exiba a soma total.

lista = []

while True:
    num = int(input("Digite um número positivo para a soma ou zero para encerrar o cálculo: "))
    if num < 0:
        print("Digite um número positivo")
    elif num > 0:
        lista.append(num)
    else:
        break

soma_total = sum(lista)
print(f"A soma total dos números digitados é {soma_total}")

# 4. Senha com repetição
# Solicite uma senha ao usuário e repita até que ele acerte a senha correta ("1234").

senha_correta = "1234"

while True:
    senha = input("Digite sua senha: ")
    if senha == senha_correta:
        print("Bem-vindo(a)!")
        break
    else:
        print("Senha errada!")

# 5. Média de várias notas
# Peça notas ao usuário até que ele digite -1. Calcule a média das notas inseridas.

notas = []
while True:
    nota = int(input("Digite sua nota ou -1 para calcular a média: "))

    if nota > 10:
        print("Digite uma nota menor ou igual a 10")
    elif nota >= 0:
        notas.append(nota)
    elif nota < -1:
        print("Digite valores positivos!")
    else:
        if len(notas) == 0:
            print("Nenhuma nota válida foi inserida.")
        else:
            print(f"Sua média é {sum(notas)/len(notas):.2f}")
        break

# 6. Tabuada personalizada
# Peça um número e exiba sua tabuada de 1 a 10.

num = int(input("Digite um número: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 7. Contagem de pares e ímpares
# Solicite 10 números e diga quantos são pares e quantos são ímpares.

impar = []
par = []

for i in range(10):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(f"Pares: {sorted(par)}")
print(f"Ímpares: {sorted(impar)}")

# 8. Soma dos múltiplos de 3 entre 1 e 100
# Use um laço for para somar os múltiplos de 3 de 1 a 100.

soma = 0

for i in range(1, 101):
    if i % 3 == 0:
        soma += i

print(f"A soma dos múltiplos de 3 de 1 a 100 é {soma}")

# 9. Fatorial de um número
# Peça um número e calcule o seu fatorial com for.

fatorial = 1

while True:
    num = int(input("Digite um número para calcular seu fatorial: "))
    if num >= 0:
        for i in range(num, 0, -1):
            fatorial *= i
        print(f"Fatorial de {num} é {fatorial}")
        break
    else:
        print("Digite um número maior ou igual a zero")

# 10. Contagem de vogais em uma palavra
# Peça uma palavra ao usuário e diga quantas vogais ela contém.

word = input("Digite uma palavra: ")

vogais = 0

for i in word:
    if i.lower() in "aeiou":
        vogais += 1

print(f"A palavra contém {vogais} vogais.")

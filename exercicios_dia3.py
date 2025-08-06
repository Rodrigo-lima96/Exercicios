
# DIA 3 – Listas, slicing e lógica com coleções
# Foco: criação, manipulação e iteração de listas.

# 1-  Crie uma lista com 5 nomes e exiba todos em maiúsculas.


# lista = []
# for i in range (0,5):
#     nome = input('Digite um nome:')
#     lista.append(nome)

# for i in lista:
#     print(i.upper())

#  2 - Peça 5 números ao usuário e exiba a média.





# 3-  Solicite uma lista de números e mostre o maior e o menor.
# lista = []

# for i in range (0,5):
#     num = int(input("Digite um número: "))
#     lista.append(num)

# print(f'Os números digitados foram {lista}')

# print(f' O menor número digitado foi {min(lista)} e o maior foi {max(lista)}')


# 4 - Remova todos os números pares de uma lista.

# import random
# lista = []
# impares = []

# for i in range(0,100):
#     num = random.randint(0,1000)
#     lista.append(num)

# lista.sort()

# for num in lista:
#     if num % 2 != 0:
#         impares.append(num)
#     else:
#         continue

# print(f"Números ímpares da lista: {impares}")


# 5- Inverta uma lista sem usar reversed().

# import random
# lista = []
# lista_invertida = []

# for i in range(0,25):
#     num = random.randint(0,100)
#     lista.append(num)   

# lista.sort()
# print(f"Lista contendo 25 número criada de forma aleatória: {lista} ")

# for i in lista[::-1]:
#     lista_invertida.append(i)

# print(lista_invertida)


# 6- Verifique se uma palavra existe dentro de uma lista de strings.
import unicodedata

estados = [
    "São Paulo",
    "Minas Gerais",
    "Rio de Janeiro",
    "Bahia",
    "Paraná",
    "Pernambuco",
    "Ceará",
    "Rio Grande do Sul",
    "Goiás",
    "Pará"
]

palavra = input("Digite o nome do seu estado e confira se ele está na lista: ")

palavra_normalizada = ""
for letra in unicodedata.normalize('NFD', palavra):
    if unicodedata.category(letra) != 'Mn':
        palavra_normalizada += letra.upper()

encontrado = False
for estado in estados:
    estado_normalizado = ""
    for letra in unicodedata.normalize('NFD', estado):
        if unicodedata.category(letra) != 'Mn':
            estado_normalizado += letra.upper()
    
    if estado_normalizado == palavra_normalizada:
        encontrado = True
        break

if encontrado:
    print("Seu estado está na lista!")
else:
    print("Seu estado não está na lista.")


# 7- Some os elementos de duas listas de mesmo tamanho, índice por índice.



# 8- Receba nomes até que o usuário digite "fim" e exiba todos em ordem alfabética.

# 9- Peça 10 números e diga quantos são maiores que a média.

# 10- Faça uma lista com os 10 primeiros quadrados perfeitos.

# 🗓️ DIA 1 – Entrada, saída, operadores, if/else

# 1. Solicite um número inteiro e diga se é par ou ímpar.
num = int(input("Digite um número: "))
if num % 2 != 0:
    print(f"{num} é um número ímpar!")
else:
    print(f"{num} é um número par!")

# 2. Peça a idade do usuário e diga se ele é maior de idade.
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# 3. Solicite duas notas e diga se a média é suficiente para aprovação (média ≥ 7).
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 7:
    print(f"Sua média é {media}. Parabéns, você foi aprovado!")
else:
    print(f"Sua média é {media}. Você foi reprovado.")

# 4. Peça um número e diga se ele é positivo, negativo ou zero.
num = int(input("Digite um número: "))
if num > 0:
    print(f"{num} é um número positivo.")
elif num == 0:
    print(f"{num} é igual a zero.")
else:
    print(f"{num} é um número negativo.")

# 5. Peça 3 números e diga qual é o maior.
fnum = int(input("Digite o primeiro número: "))
snum = int(input("Digite o segundo número: "))
tnum = int(input("Digite o terceiro número: "))

if fnum > snum and fnum > tnum:
    print(f"{fnum} é o maior entre os números digitados.")
elif snum > fnum and snum > tnum:
    print(f"{snum} é o maior entre os números digitados.")
elif tnum > fnum and tnum > snum:
    print(f"{tnum} é o maior entre os números digitados.")
elif fnum == snum and fnum == tnum:
    print("Todos os números são iguais.")
elif fnum == snum and fnum > tnum:
    print(f"{fnum} e {snum} empatam como maiores.")
elif snum == tnum and snum > fnum:
    print(f"{snum} e {tnum} empatam como maiores.")
elif fnum == tnum and fnum > snum:
    print(f"{fnum} e {tnum} empatam como maiores.")

# 6. Receba a base e altura de um triângulo e calcule a área.
base = float(input("Digite a base do triângulo em cm: "))
altura = float(input("Digite a altura do triângulo em cm: "))
if base <= 0 or altura <= 0:
    print("Base e altura devem ter valores positivos.")
else:
    area = (base * altura) / 2
    print(f"A área do triângulo é de {area:.2f} cm².")

# 7. Verifique se um número é múltiplo de 5.
num = int(input("Digite um número: "))
if num % 5 == 0:
    print(f"{num} é múltiplo de 5.")
else:
    print(f"{num} não é múltiplo de 5.")

# 8. Verifique se dois números são iguais, diferentes, maior ou menor.
fnum = int(input("Digite o primeiro número: "))
snum = int(input("Digite o segundo número: "))
if fnum == snum:
    print("Os números são iguais.")
else:
    print("Os números são diferentes.")
    if fnum > snum:
        print(f"{fnum} é maior que {snum}.")
    else:
        print(f"{snum} é maior que {fnum}.")

# 9. Peça um número e diga se ele é divisível por 2 e por 3.
num = int(input("Digite um número: "))
if num <= 0:
    print("Digite um número positivo!")
else:
    if num % 2 == 0 and num % 3 == 0:
        print("O número digitado é divisível por 2 e 3.")
    elif num % 2 == 0:
        print("O número digitado é apenas divisível por 2.")
    elif num % 3 == 0:
        print("O número digitado é apenas divisível por 3.")
    else:
        print("O número digitado não é divisível por 2 nem por 3.")

# 10. Receba um ano e diga se ele é bissexto.
ano = int(input("Digite um ano para saber se ele é bissexto: "))
if ano <= 0:
    print("Digite um valor válido!")
elif (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é um ano bissexto!")
else:
    print(f"{ano} não é um ano bissexto!")

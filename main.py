import time
import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

print("\nBem vindo ao criador de senhas")
time.sleep(2)
print("Este programa cria novas senhas inteiras para você! Gostaria de experimentar?")
time.sleep(2)

while True:
    comprimento = input("\nQual será o comprimento da sua senha?")
    
    try:
        IntComprimento = int(comprimento)
        break

    except ValueError:

        try:
            comprimentoFormatado = comprimento.replace(",", ".")
            FloatComprimento = float(comprimentoFormatado)
            print("Isso não é um valor inteiro! Digite um número sem vírgula!")

        except ValueError:
            print("Espere! Isso não é um número! Por favor, digite um número!")

        time.sleep(2)

time.sleep(1)

senha = ""

for _ in range (IntComprimento):
    caractere = random.choice(caracteres)
    senha += caractere

print("Sua senha é...")
time.sleep(1)

print("\n" + "-" * IntComprimento)
print(senha)
print("-" * IntComprimento + "\n")

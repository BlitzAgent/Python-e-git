numero = int(input("Digite um número de 5 dígitos: "))

numero1 = numero // 10000) % 10
numero2 = (numero // 1000) % 10
numero3 = (numero // 100) % 10
numero4 = (numero // 10) % 10
numero5 = numero % 10

print(digito1, " ", numero1)
print(digito2, " ", numero2)
print(digito3, " ", numero3)
print(digito4, " ", numero4)
print(digito5, " ", numero5)
#Leia uma lista de 10 (dez) números inteiros, mostre os números, sua soma e a multiplicação.

lista = []
soma = 0
multiplicação =1
for i in range(10):
    lista.append(int(input()))
    soma += lista[i]
    multiplicação *= lista[i]
print(lista)
print(soma)
print(multiplicação)


                
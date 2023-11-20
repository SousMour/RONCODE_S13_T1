#Escreva um programa que leia um número n. 
# Considere uma lista com n posições, e então: 
# a) preencha com valores reais lidos pelo teclado e imprima na ordem inversa. Considere até 4 (quatro) casas decimais. 
# b) preencha com n notas lidas pelo teclado e imprima as notas e a média na tela. Considere 1 (uma) casa decimal. 
# c) preencha com n letras lidas pelo teclado e imprima quantas vogais foram lidas. Imprima as consoantes.

def ordem_inversa(n):
    lista = []
    if n != 0:
        for _ in range(n):
            valor = round(float(input()), 4)
            lista.insert(0, valor)
        print(lista)
    else: 
        print(lista)
def imprimir_notas(n):
    notas = []
    if n !=0:
        for _ in range(n):
            nota = round(float(input()), 1)
            notas.append(nota)
        media = round(sum(notas) / n, 1)
        print(notas)
        print(media)
    else: 
        print(notas)
        print('SEM NOTAS')

def consoantes(n):
    vogais = ['a','e','i','o','u','A','E','I','O','U']
    letras = []
    num_vogais = 0
    for _ in range(n):
        letra = input().strip()
        letras.append(letra)
        if letra in vogais:
            num_vogais += 1
    print(num_vogais)
    for letra in vogais:
        if letra in letras:
            letras.remove(letra)
    print(letras)

def main():
    n = int(input())

    ordem_inversa(n)
    imprimir_notas(n)
    consoantes(n)

if __name__ == "__main__":
    main()
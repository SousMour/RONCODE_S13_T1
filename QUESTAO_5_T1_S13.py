#Leia duas listas A e B contendo 25 elementos inteiros cada, 
# gerar e imprimir uma lista C de 50 elementos, 
# cujos elementos sejam a intercalação dos elementos de A e B.

lista_a = []
lista_b= []
for _ in range(25):
    numero = int(input())
    lista_a.append(numero)
print(lista_a)
for _ in range(25):
    numero = int(input())
    lista_b.append(numero)
print(lista_b)
lista_c= lista_a + lista_b
lista_c [::2]= lista_a
lista_c[1::2]= lista_b
print(str(lista_c))

#Leia 20 números inteiros e armazene-os numa lista. 
# Separe os números pares na lista PAR e os números 
# ímpares na lista IMPAR. Imprima as três listas.

lista=[]
par = []
impar = []
for _ in range(20):
    numero = int(input())
    lista.append(numero)
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)


print(lista)
print(par)
print(impar)

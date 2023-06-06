# Escreva um algoritmo que leia dois vetores de 10 posições e faça a soma dos elementos de mesmo índice, colocando o resultado em um terceiro vetor. Mostre o vetor resultante.

vector1 = []
vector2 = []
vector_soma = []
i = 0

while i < 10:
    value1 = int(input("Digite um valor para compor o primeiro vetor: "))
    value2 = int(input("Digite um valor para compor o segundo vetor: "))
    vector1.append(value1)
    vector2.append(value2)
    vector_soma.append(value1+value2)
    i += 1

print(vector1)
print(vector2)
print(vector_soma)
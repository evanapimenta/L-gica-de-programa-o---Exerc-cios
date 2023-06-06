## Estruturas de Controle/Repetição
1. Faça um algoritmo que determine o maior entre N números. A condição de parada é a entrada de um valor 0, ou seja, o algoritmo deve ficar calculando o maior até que a entrada seja igual a 0.

		receber entrada
		enquanto entrada != 0 processar
			se entrada > maior então
				maior = entrada
			receber entrada
		escreva "O número maior digitado pelo usuário foi" + maior
		fim

---

2. Faça um algoritmo que conte de 1 a 100 e a cada múltiplo de 10 emita uma mensagem: "Múltiplo de 10"

		para i = 1, enquanto i <= 100 processar
			se (i % 10 == 0) então
				escreva "Múltiplo de 10: " + i

---

3. Elabore um programa que gera e escreve os números ímpares dos números entre 100 e 200.

para i = 100, enquanto i <= 200, processar

	para i = 100, enquanto i <= 200 processar
	se (i % 2 != 0) então
		escreva "Ímpar: " + i

---

4. Construa um algoritmo que leia 10 valores inteiros e positivos e:

- Encontre o maior valor.
- Encontre o menor valor.
- Calcule a média dos números lidos

		maior = 0
		menor = 9999999
		soma = 0
		contador = 1

		para contador = 1, enquanto contador <= 10 processar
			receber n
			se n > maior
				maior = n
			fimSe
			se n < menor
				menor = n
			fimSe
		soma += n
		contador += 1
		media = soma / 10
		escrever "Maior número digitado: " + maior
		escrever "Menor número digitado: " + menor
		escrever "A média da soma de todos os números é: " + media

---

5. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

		escrever "Informe o nome"
		receber usuario
		escrever "Informe a senha"
		receber senha

		enquanto usuario == senha processar
			escreva "A senha não pode ser igual ao nome de usuário. Escolha uma outra senha."
			escrever "Informe o nome"
			receber usuario
			escrever "Informe a senha"
			receber senha

---

6. Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de que número ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50

		escreva "Digite um número de 1 a 10"
		receber numero
		i = 1

		enquanto numero > 10 processar
			escreva "Numero deve estar entre 1 e 10"
			receber numero

		para i = 1, enquanto <= 10 processar
			resultado = numero * i
			escreva "Tabuada do" numero
			escreva numero, "X", i, "=", resultado
			i = i + 1

---

7. Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar. Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse e o tipo de defeito:
	- necessita de esfera
	- necessita de limpeza
	- necessita troca do cabo ou conector
	- mouse quebrado ou inutilizado

Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir um relatório constando a quantidade de mouses verificados, quais possuem cada categoria de defeito e a porcentagem.

	necessita_esfera = 0
	necessita_limpeza = 0
	necessita_cabo = 0
	mouse_quebrado = 0
	numero_mouses = 0

	enquanto codigo_mouse != 0 processar
	escreva "Código do mouse"
	receba codigo_mouse
	numero_mouses = numero_mouses + 1
	escreva "Digite o número correspondente ao estado do mouse: 
	
	1 - Necessita da esfera
	2 - Necessita de limpeza
	3 - Necessita troca do cabo ou conector
	4 - Quebrado ou inutilizado"
	
	receber tipo_defeito
	
	caso tipo_defeito selecione
		caso 1
			necessita_esfera = necessita_esfera + 1
			saia
		caso 2
			necessita_limpeza = necessita_esfera + 1
			saia
		caso 3
			necessita_cabo = necessita_cabo + 1
			saia
		caso 4
			mouse_quebrado = mouse_quebrado + 1
			saia
	
	porc_esfera = (necessita_esfera / numero_mouses) * 100
    porc_limpeza = (necessita_limpeza / numero_mouses) * 100
    porc_cabo = (necessita_cabo / numero_mouses) * 100
    porc_quebrado = (mouse_quebrado / numero_mouses) * 100

	escreva "Quantidade de mouses:" + numero_mouses
	
	escreva "Situação            Quantidade             Percentual       
	1- Necessita de esfera       necessita_esfera       porc_esfera  %   
	2- Necessita de limpeza      necessita_limpeza      porc_limpeza %   
	3- Necessita de troca cabo    necessita_cabo        porc_cabo    %   
	4 - Quebrado ou inutilizado   mouse_quebrado        por_quebrado %   

---
## Variáveis Compostas

1. Faça um algoritmo que carregue um vetor de 5 elementos inteiros e em seguida armazene em um vetor apenas os números pares maiores que 0. No final deve mostrar os elementos do vetor na tela.

		inteiro: vetor[0, 0, 0, 0, 0]
		inteiro: vetor_pares[ ]
		
		para i = 0, enquanto i < 5 processar
		escreva "Adicione um numero ao vetor"
		receber vetor[i]
		se (vetor[i] % 2 == 0) e (vetor[i] > 0) então
			vetor_pares = vetor[i] / adicionar vetor[i] em pares
		escrever vetor_pares

>[!tip]
>Quando os valores não são conhecidos, mas sabemos a quantidade de elementos a serem tratados, é possível apenas declarar o vetor com todos os valores equivalentes a 0. Quando não se sabe qual a quantidade de vetores que resultará (no caso da variável vetor_pares), pode ser declarado um vetor vazio "[  ]".

---

2. Escreva um algoritmo que leia dois vetores de 10 posições e faça a soma dos elementos de mesmo índice, colocando o resultado em um terceiro vetor. Mostre o vetor resultante.

		vector1 = [ ]
		vector2 = [ ]
		vector_soma = [ ]
		
		para i = 0, enquanto i < 10 processar
			escreva "Digite um número para compor o primeiro vetor"
			receber valor1
			escreva "Digite um número para compor o segundo vetor"
			receber valor2
			vetor1[i] = valor1
			vetor2[i] = valor2
			soma = (valor 1 + valor 2)
			i = i + 1
		
		para i = 0, enquanto i < 10 processar
			escrever soma[i]
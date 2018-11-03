#variaveis
idade = 3
nome = "Jose da silva"
salario = 1500.85
lista = ['jose', 'maria', 'nelson']
dic = {1:"banana", 2:"abacate", 3:"morango", 4:"abacaxi"}
print(type(idade))
print(type(nome))
print(type(salario))
print(type(lista))

#blocos de decisoes 
if(idade < 18):
	print("menor de idade")
else:
	print("Maior de idade")

#lacos de repeticao
#imprimir numeros de 0 a 100 com for
for i in range(0,100):
	print(i),

print("")

num = 0
while(num <= 10):
	print(num * 2),
	num = num + 1

print("")

#laco numa lista
for l in lista:
	print(l)

print("")
#outra forma 
for i in range(len(lista)):
	print(lista[i])

#usando chave valor num dicionario
for k,v in dic.items():
	print(v)
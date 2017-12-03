#tomada de decisoes

#funcao que retorna o maior numero de dois numeros

def maior(num1, num2):
	if(num1 >= num2):
		return num1
	if(num2 > num1):
		return num2

print(maior(7,8))
print(maior(15,8))
print(maior(7,-954))

#verifica se a primeira letra numa string e a buscada
def first_leter(nome):
	if(nome[0] == "M"):
		return True
	else:
		return False

print(first_leter("Milton"))
print(first_leter("Bilton"))




def firsts_leters(nome):

	if(nome[0] == "M" or nome[0] == "B"):
		return True
	else:
		return False

print(firsts_leters("Milton"))
print(firsts_leters("Bilton"))








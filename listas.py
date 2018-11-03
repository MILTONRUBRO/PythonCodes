#listas em python

# funcao que retorna quantos dias tem em determinado mes escolhido

#cria uma lista
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# define a procedure, how_many_days,
# that takes as input a number
# representing a month, and returns
# the number of days in that month.

def how_many_days(month_number):
    day = days_in_month[month_number-1]
    return day


print how_many_days(1)
#>>> 31

print how_many_days(9)
#>>> 30

#funcao que retorna diferenca entre maior e menor valor numa lista de numeros
def set_range(a,b,c):
    # Your code here
    lista = [a,b,c]
    
    diferenca =   max(lista) -  min(lista)
    
    return diferenca


print set_range(10, 4, 7)
#>>> 6  # since 10 - 4 = 6

print set_range(1.1, 7.4, 18.7)
#>>> 17.6 # since 18.7 - 1.1 = 17.6


#encontrar um elemento na lista
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")

#inserir elementos na lista
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")

animals.insert(duck_index, "cobra")

print(animals)

#mudando valor de uma string numa lista
lista = ['H', 'e' , 'l','l', 'o']
print(lista)
lista[0] = 'Y'
print(lista)

#mudar  valor de uam lista numa funcao
spy = [0,0,7]

def replace_spy(spy):
    
    spy[2] = spy[2]+1
    return spy

#adicionar elemento ao fim da lista
stooges = ['Moe', 'Larry', 'Curly']
stooges.append('Shemp')
print(stooges)

#funcao len retorna o tamanho de um dado
len(stooges)

p = [1,2]
q = [3,4]

p.append(q)

print(p)

#loops em uma lista usando while

def imprimeLista(p):
	i = 0
	while(i < len(p)):
		print(p[i])
		i = i+1

listaNumeros = [5,8,4,6,8]
imprimeLista(listaNumeros)

#loops em uma lista usando for

def print_all_elements(lista):

	for i in lista:
		print(i)


minha_lista = [1,2 ,[3,4]]

print_all_elements(minha_lista)

#somando todos os elementos de uma lista

def soma_lista(lista):
	soma = 0
	for i in lista:
		soma = soma + i
	return soma


print(soma_lista([5,5,4,85,2,4,544]))


#encontrar  valor numa lista 
def find_element(lista, key):
    i = 0
    while(i < len(lista)):
        if(lista[i] == key):
            return i
        i = i + 1
    return -1
    



print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1

#funcao anterior usando for
def find_element(lista, key):
    
    cont = 0
    
    for l in lista:
        if(l == key):
            return cont
        cont = cont + 1
    return -1



print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1

#usando index 
def find_element(lista, key):
    
    if(key in lista):
        return lista.index(key)
    else:
        return -1

print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1



#somar duas listas retirando os elementos iguais
def union(lista1, lista2):
    
    for l in lista2:
        if l not in lista1:
            lista1.append(l)
    
        
    

a = [1,2,3]
b = [2,4,6]
union(a,b)
print a 
#>>> [1,2,3,4,6]
print b
#>>> [2,4,6]

#metodo pop lista


#maior numero numa lista
def greatest(list_of_numbers):
    num = 0
    if(len(list_of_numbers) > 0):
        num = max(list_of_numbers)
        return num
    return 0



print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0

# sem utilizar funcao max 
def greatest(list_of_numbers):
    maior = 0
    if(len(list_of_numbers) > 0):
        for l in list_of_numbers:
            if l > maior:
                maior = l
        return maior
    return 0



print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0

#dada as listas abaixo, retornar quantidade de alunos e valor pago por cada matricula
udacious_univs = [['Udacity',90000,0]]

usa_univs = [ ['California Institute of Technology',2175,37704],
              ['Harvard',19627,39849],
              ['Massachusetts Institute of Technology',10566,40732],
              ['Princeton',7802,37000],
              ['Rice',5879,35551],
              ['Stanford',19535,40569],
              ['Yale',11701,40500]  ]

def total_enrollment(lista):
    total_alunos = 0
    taxa_matricula = 0
    
    
    for name,student,price in lista:
        total_alunos = total_alunos + student
        taxa_matricula = taxa_matricula + student  * price
        
    
    return total_alunos,taxa_matricula
    
    

print total_enrollment(udacious_univs)
#>>> (90000,0)

print total_enrollment(usa_univs)
#>>> (77285,3058581079)

#calcular media 
def list_mean(lista):
    soma = 0.
    media = 0.
    for l in lista:
        soma = soma+l
    
    media = soma/len(lista)
    
    return media


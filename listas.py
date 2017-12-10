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
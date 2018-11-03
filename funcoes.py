#funcoes 
#funcao que retorna uma string sem a primeira letra
def resto_da_string(s):
	return s[1:]

#chamando a funcao dentro do print passando um argumento
print(resto_da_string("Valhalla"))


#retorna um numero incremetando 1
def inc(num):
	return num+1

print(inc(6))

def sum(a,b):
	a = a+b
	return a


print(sum("maria","joao"))

print(sum(5,87))

# funcao que retorna quadrado de  um numero
def quadrado(num):
    return num*num


print(quadrado(5))

#concatenando string
def abbaize(s1, s2):
	s3 = s1+s2+s2+s1
	return s3

print(abbaize("pao", "batata"))

#funcao que encontra segunda ocorrencia de uma string
def find_second(search, target):
	first = search.find(target)
	second = search.find(target, first+1)
	return second

busca = "ola alo ola alo ola aola ola"
valor = "ola"
print(find_second(busca, valor ))


def udacify(s):
	return 'U' + s

print(udacify("BIRLLL"))

#mediana de tres numeros
def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(a, b, c):
    big =  biggest(a, b, c)
    
    if(big == a):
        return bigger(b,c)
    if(big == b):
        return bigger(a,c)
    else:
        return bigger(a,b)


#verificar se primeiro caractere de uma lista de strings é um U 
def measure_udacity(lista):
    cont = 0
    for i in lista:
        if (i[0] == 'U'):
            cont = cont+1
    return cont
    



print measure_udacity(['Dave','Sebastian','Katy'])
#>>> 0

print measure_udacity(['Umika','Umberto'])
#>>> 2

#funcao pra calcular potencia
def power(base, exponent):  # Add your parameters here!
  result = base ** exponent
  print "%d to the power of %d is %d." % (base, exponent, result)

power(37, 4)  # Add your arguments here!

# funcao que retorna quantidade de dias e horas recebendo determinado inteiro 
def hours2days(num):
    
     
    dias = 0
    horas = 0
     
    dias = num//24
    horas = num % 24
    
    return dias, horas
         

print(hours2days(24))
print(hours2days(25))
print(hours2days(10000))

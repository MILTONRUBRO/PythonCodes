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

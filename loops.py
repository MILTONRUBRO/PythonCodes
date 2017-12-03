#lacos de repeticoes 


#imprime numeros de 0 a 9
i = 0;

while(i < 10):
	print(i)
	i = i +1

print("-----------------------")
#imprime pares de 0 a 100
def num_pares(num):
	i = 0
	while(i <= 100):
		if(i % 2 == 0):
			print(i)
		i = i+1

num_pares(100);

#calculando fatorial de N
def fatorial(num):
	if(num == 0 or num == 1):
		return 1
	i = num-1

	while(num > 1):
		num = num * i
		i = i -1
		return num

print(fatorial(5))

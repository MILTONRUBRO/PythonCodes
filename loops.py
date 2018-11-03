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

#contagem regressiva do lancamento
def countdown(num):
    while(num > 0):
        print(num)
        num = num-1
        

    print("Blastoff!")


countdown(3)


#usando laco numa lista 
start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for i in start_list:
  square_list.append(i**2)

square_list.sort()

print square_list

#laco em um dicinario
webster = {
  "Aardvark" : "A star of a popular children's cartoon show.",
  "Baa" : "The sound a goat makes.",
  "Carpet": "Goes on the floor.",
  "Dab": "A small amount."
}

# laco for 
for key in webster:
  print(webster[key])
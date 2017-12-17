import random
word_file = "words.txt"
word_list = []

# abre o arquivo de texto word_file
with open(word_file,'r') as words:
	for line in words:
		# remove espacoes em brancos e deixa minusculo
		word = line.strip().lower()
		# nao inclue palavras muito grandes ou pequenas
		if 3 < len(word) < 8:
			word_list.append(word)


def generate_password():
    
    cont = 0
    palavra = ""
    senha = ""
    while(cont < 3):
        
        palavra = word_list[random.randint(0,len(word_list))]
        senha = senha + palavra
        
        cont = cont + 1
    
    return senha
        
    
print(generate_password())
#manipulacao de arquivos

#abrindo um arquivo com  a funcao open 

f = open('/my_path/my_file.txt','r')

#acessando conteudo do arquivo
file_data = f.read()

#fechando arquivo
f.close()

#alterando conteudo de um arquivo mudando o parametro para w
f = open('/my_path/my_file.txt','w') 

#escrevendo no arquivo
f.write("Hello World")
f.close()
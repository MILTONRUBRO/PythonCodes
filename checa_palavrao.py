import urllib

def ler_arquivo():
    arquivo = open("C:\Users\maromba\Downloads\movie_quotes.txt")
    conteudo_arquivo = arquivo.read()
    print(conteudo_arquivo)
    arquivo.close
    checa_palavrao(conteudo_arquivo)

def checa_palavrao(texto_para_checar):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + texto_para_checar)
    saida = connection.read()
    print(saida)
    connection.close()

    
ler_arquivo()
    
    

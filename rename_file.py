import os

def renomear_arquivo():
    lista_arquivos = os.listdir(r"C:\Users\maromba\Downloads\prank")
    pasta_salva = os.getcwd()
    
    print(lista_arquivos)
    os.chdir(r"C:\Users\maromba\Downloads\prank")
    for l in lista_arquivos:
        os.rename(l, l.translate(None, "0123456789"))

renomear_arquivo()
    
    

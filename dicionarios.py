#usando dicionarios em python
elements = {"hydrogen" : 1, "helium":2 ,"Carbon":6}

print(elements)

#adicionar um elemento
elements["lithium"] = 3

#retorna true ou false caso um elemento esteja no dicionario
print("helium" in elements )


#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5

population = {"Shanghai":17.8, "Istanbul":13.3, "Karachi":13.0, "Mumbai":12.5, "Sao Paulo":12.1}


print(population["Mumbai"])
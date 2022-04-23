
def convert(list):
    return tuple(i for i in list)
    
print("Por favor introduza 10 numeros inteiros.")
lista = ()
index = 1
for i in range(10):
    lista = lista + (int((input(f" {index} : "))),)
    index +=1
    



print("Os valores  introduzidos foram : ")
index = 1
for valor in lista:
    print(f" Valor [{index}] = {valor}")
    index += 1



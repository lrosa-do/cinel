#Ficha 1

#Ex1
'''
#########################
########################################
##FUNÇÕES
def calcular(frase): #irá devolver resposta
   qtm, qtM, qtd = 0, 0 ,0
   #"Olá Mundo 2022!"
   for simbolo in frase: 
      if simbolo.islower():#'a' <= simbolo <= 'z' não contempla os acentuados
         qtm = qtm + 1
      elif simbolo.isupper():
         qtM = qtM + 1
      elif '0' <= simbolo <= '9': #simbolo>='0' and simbolo <= '9'
         qtd = qtd + 1
      
   return qtm, qtM, qtd
#-------------------#
def conta_esp(frase):
   qtE=0
   for simb in frase:
      if simb == ' ':
         qtE = qtE + 1

   return qtE


####Script inicial
frase = input("Insira qq coisa: ")
resp = calcular(frase) #(qtm, qtM, qtd)
print(f"Quantidade de minúsculas: {resp[0]}")
print(f"Quantidade de maiúsculas: {resp[1]}")
print(f"Quantidade de digitos: {resp[2]}")
x = conta_esp(frase) #recebe 1 número de espaços existentes
print(f"A qt de espaços é {x}")
'''

#Ex2
'''
tuplo = ()
for cont in range(1,11): #{1,2,3,4,5,6,7,8,9,10}
   n = int(input(f"Insira {cont}º número: "))
   tuplo = tuplo + (n,)

print(tuplo)
'''

#Ex3
'''
t1 = (2,5,3)
t2 = (5,0,2)
t3 = ()

qt = len(t1)
i = 0

while i < qt:
   soma = t1[i] + t2[i] # 3 + 2
   t3 = t3 + (soma,)    #(7,5,5)
   i = i + 1
'''

#Ex4
'''
frase1 = "ola mundo"
frase2 = "oi cara"
t = ()

for x in frase1:
   if x in frase2 and x not in t:
      t = t + (x,)

print(f"{frase1}\n{frase2}\n{t}")
'''

#Ex5
'''
def ver_primo(t): #(9,3,7,    19,6,11)
   
   primo = () #para guardar os primos que irá encontrar

   for elem in t:
      #qts divisores tem este "elem"
      qtdiv = 2 # 1 e próprio "elem" são divisores de "elem"
      x = 2
      limite = int(elem ** 0.5)
      while x <= limite:
         if ( (elem % x) == 0 ): #x é divisor
            qtdiv = 3
            break  #pára o ciclo while

         x = x + 1 #passa ao próximo candidato a divisor
        
      #se tiver 2 então guarda o "elem" no tuplo dos primos
      if qtdiv == 2: ##contou 2 divisores para o "elem"
         primo = primo + (elem,)

   return primo

#######################
tuplo = (9,3,7,19,6,11)
resp = ver_primo(tuplo) #tuplo(n1, n2 ,3, ...)

if len(resp) > 0:
   print(f"Do tuplo inicial {tuplo} os primos são {resp}")
else:
   print(f"Não existem elementos primos no tuplo {tuplo}")

'''

#Ex6
'''
def substituir(tuplo, sai, entra):
   t = () ##vai recebendo 1 valor de cada vez do tuplo original
   for elem in tuplo:
      if elem != sai: #guardar o "elem"
         t = t + (elem,)
      else:
         t = t + (entra,)

   return t

#####################################################
tuplo = (1,2,3,2,3,4,1)
print(f"Tuplo -> {tuplo}")
sai = int(input("Qual o valor a substituir? "))
entra = int(input(f"Qual o valor que irá substituir {sai}? "))

resp = substituir(tuplo, sai, entra)

print(f"O tuplo resultante é {resp}")
'''

#Ex7
'''
cidades = []
for x in range(5):
   nome = input("Indique o nome de uma cidade: ").title()
   cidades = cidades + [nome] #cidades.append(nome)

print(f"As cidades inseridas foram: {cidades}")
'''
#Ex8
'''
def remover(cidades):
   elimina = input(f"Das seguintes cidades, qual deseja remover?{cidades}").title().strip()
   
   if elimina not in cidades:
      print(f"Não foi possível remover {elimina}.")
   else:
      cidades.remove(elimina)
      print(f"A nova lista é {cidades}")

   
#########
cidades = ['Porto', 'Braga', 'Beja', 'Aveiro', 'Lisboa']
remover(cidades)
'''
#Ex9
'''
def trocar(cidades, sai, entra):
   #   0         1        2         3         4
   #["Porto", "Braga", "Lisboa", "Faro", "Coimbra"]
   i = 0
   limite = len(cidades) #dá a qt de elementos na variavel cidades
   while i < limite:
      if cidades[i] == sai:
         cidades[i] = entra
         return f"A lista de cidades resultante é {cidades}"
      
      i = i + 1

   return f"Não foi possível substituir {sai} por {entra}"
################################
cidades = ["Porto", "Braga", "Lisboa", "Faro", "Coimbra"]
print(f"Cidades disponíveis: {cidades}")
sai = input("Qual a cidade que deseja substituir?").title().strip()
entra = input(f"Qual a cidade que substitui {sai}?").title().strip()
novalista = trocar(cidades, sai, entra)
print(novalista)
'''

#Ex10
'''
frutos = ['Laranja','Laranja','Banana', 'Morango',  'Maçã', 'Pêra', 'Laranja','Pêssego']

#Ex11
qt = len(frutos)
print(f"Existem {qt} espécies de frutos registados. São eles:" )
for fruto in frutos:
   print(fruto)


#Ex12
novo = input("Adicione um novo fruto: ")
if novo not in frutos:#se ainda não existir então adiciona
   frutos.append(novo)

for fruto in frutos: #Mostrar a nova lista
   print(fruto)

#Ex13

rem = input("Qual o fruto que deseja remover da lista? ")
if rem not in frutos:
   print(f"Não é possível remover o fruto {rem} da lista {frutos}")
else:
   while rem in frutos:
      frutos.remove(rem)

print(frutos)

#Ex14
#frutos.sort() #altera o conteúdo da lista
ordenado = sorted(frutos,reverse=True) #reverse=True    ordena de z para a
print(ordenado)
print(frutos)
'''

#Ex15
'''
lista = [1,2,3,2,3,4,1]
print(lista)
nova = []
for num in lista:
   if num not in nova:
      nova.append(num)
print(nova)
#alternativa utilizando o tipo de variável "set" -> elimina valores repetidos
#lista = list(set(lista))
#print(lista)

'''
#Ex16
'''
lista = [1,2,3,2,1,3,4,1]
#valor = 1
#1 ocorre 3 vezes e nas posições [0, 4, 7]
valor = int(input(f"Qual o valor a procurar na lista {lista}? "))
qt = 0 #quantidade de vezes que encontra ao valor na lista
pos = [] # para guardar os indices onde ocorre o valor

limite = len(lista)

for i in range(limite): # i representa a casota da lista a ser analizada
   if valor == lista[i]: #contar + 1 ocorrência e guardar a posição "i"
      qt +=1 #qt = qt + 1
      pos.append(i)
      
print(f"{valor} ocorre {qt} vezes e nas posições {pos}")
'''
#Ex17
'''
lista = [1,2,3,2,1,3,4,1]
valor = int(input(f"Qual o valor a procurar na lista {lista}? "))
qt = 0 
pos = []

for ind, elem in enumerate(lista): #enumerate devolve tuplo com 2 elementos(indice, valor)
   if valor == elem:
      qt +=1
      pos.append(ind)

print(f"{valor} ocorre {qt} vezes e nas posições {pos}")
'''

#Ex18
'''
def maiores(lista, qtM):
   #[15, 18, 18, 20, 20, 18, 11, 14, 20, 20]
#  resultado = ()
#   for x in range(qtM):
#      maximo = max(lista)
#      resultado = resultado + ( maximo,  )
#      #remover o max encontrado
#      lista.remove(maximo)

#   return resultado


   #utilizando a ordenação
   lista.sort(reverse=True) #ordena a lista de forma descendente
   return tuple( lista[0:qtM] ) ##lista[0:qtM] devolve uma lista
   


############################################################################
#criar lista com 10 elementos aleatorios entre 10 e 20  - randint(v1,v2)
from random import randint as r  #randint(10,20) -> r(10,20)

#lista = sample( range(10,21), 10 )  gera lista com 10 valores entre 10 e 20
lista = []
for x in range(10):
   valor = r(10,20)  
   while valor in lista: #para garantir que nao tem valores repetidos
      valor = r(10,20)   
   lista.append(valor) 

print(f"A lista de 10 valores gerados é: {lista}")

qtM = 0 #para entra no ciclo seguinte 
while qtM < 1 or qtM > 10: #enquanto não inserir um valor válido, pede novamente
   qtM = int(input("Qual a quantidades dos maiores números pretende obter?[1-10] "))

resp = maiores(lista, qtM) #devolve tuplo com 5 valores maiores

print(f"Da lista «{lista}» os {qtM} maiores elementos são «{resp}»")

'''









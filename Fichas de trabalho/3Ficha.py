#Ex1
#dados guardados no ficheiro dados.csv
#Ana,Lisboa,22,Centro
#Pedro,Porto,45,Norte
#Isabel,Coimbra,22,Centro

def elimina(cont):
   #cont=[ "Ana,Lisboa,22,Centro\n", "Pedro,Porto,45,Norte\n", ... ]
   for ind, frase in enumerate(cont):
      novafrase = frase.replace('\n', '')
      cont[ind] = novafrase

   return cont
###############
fich = open("dados.csv", "r", encoding="UTF-8-SIG")
cont = fich.readlines()
fich.close()

#eliminar '\n' de todas as frases
cont = elimina(cont)

'''
#a
num_pessoas = len(cont)
print(f"Estão registadas {num_pessoas} pessoas no ficheiro.")

#b Qts pessoas por zonas
#cont=['Ana,Lisboa,22,Centro','Pedro,Porto,45,Norte', ... ]

qtN, qtC, qtS = 0,0,0
for pessoa in cont: #pessoa = 'Ana,Lisboa,22,Centro'
   dados = pessoa.split(',') #dados = ['Ana','Lisboa','22','Centro']
   zona = dados[3]
   if zona == 'Norte':
      qtN += 1
   elif zona == 'Centro':
      qtC += 1
   else:
      qtS += 1

print(f"Quantidade de pessoas do norte: {qtN}")
print(f"Quantidade de pessoas do centro: {qtC}")
print(f"Quantidade de pessoas do sul: {qtS}")

#c
def calcmed(zona):
   idades = []#guardar as idades das pessoas
   #cont=['Ana,Lisboa,22,Centro','Pedro,Porto,45,Norte', ... ]
   for pessoa in cont: #pessoa = 'Ana,Lisboa,22,Centro'
      dados = pessoa.split(',')#dados = ['Ana','Lisboa','22','Centro']
      if zona == dados[3]:#guardar a idade dados[2]
         idades.append(int(dados[2])) #soma = soma + int(dados[2])

   somaidades = sum(idades)
   qtpessoas = len(idades)
   media = somaidades / qtpessoas
   return media
##########################
zona = input("Diga qual a zona do país que pretende \
obter a média das idades: ").title()
resp = calcmed(zona)
print(f"A média das idade da zona {zona} é {resp:.1f}")#mostra media com 1 casa decimal


#d
nome = input("Qual o nome a procurar? ").title()
for pessoa in cont: #pessoa = 'Ana,Lisboa,22,Centro'
   dados = pessoa.split(',')#dados = ['Ana','Lisboa','22','Centro']
   if nome == dados[0]:
      print(f"{nome} habita em {dados[1]}")
'''

#e
'''
cidade = input("Qual o nome da cidade? ").title()
qt = 0
for pessoa in cont: #pessoa = 'Ana,Lisboa,22,Centro'
   dados = pessoa.split(',')#dados = ['Ana','Lisboa','22','Centro']
   if cidade == dados[1]:
      qt +=1 #qt = qt + 1
print(f"Na cidade {cidade} existem {qt} pessoas.")
'''
#f
'''
#criar lista de cidades sem repetições
cidades = []
for pessoa in cont: #pessoa = 'Ana,Lisboa,22,Centro'
   dados = pessoa.split(',')#dados = ['Ana','Lisboa','22','Centro']
   cidade = dados[1]
   if cidade not in cidades:
      cidades.append(cidade)

print(f"Cidade: {cidades}")

#Cidades: ['Lisboa', 'Porto', 'Coimbra', 'Chaves', 'Beja', 'Cerveira', 'Faro', 'Covilhã']
#  QT   : [   3    ,   2     ,   5     ,     1    , .....                               ]
qts = []

for cidade in cidades:
   qt = 0
   ##fixada uma cidade, iremos contar qts pessoas habitam nela
   for pessoa in cont: #pessoa = 'Ana,Lisboa,22,Centro'
      dados = pessoa.split(',')#dados = ['Ana','Lisboa','22','Centro']
      if cidade == dados[1]: #incrementar + 1 pessoa dessa cidade
         qt = qt + 1
   #qt quantidade de pessoas da cidade fixada
   qts.append(qt)

#cidades=['Lisboa', 'Porto', 'Coimbra', 'Chaves', 'Beja', 'Cerveira', 'Faro', 'Covilhã']
#  qts = [3       ,    2   ,     1    ,     1   ,    1  ,      1    ,    3,        1   ]

print(cidades)
print(qts)

for indice, cidade in enumerate(cidades): #(0,Lisboa) (1,Porto) (2,Coimbra) (3,Chaves) ...
   print(f"{cidade}: {qts[indice]}")   #qts[cidades.index(cidade)]

maximo = max(qts) #maximo de habitantes
#pos = qts.index(maximo) #posição onde ocorre o maximo
#maiorcidade = cidades[pos]
#print(f"Cidade com mais habitantes é {maiorcidade} com {maximo} de habitantes")

lstmax = [] # lista guarda as cidades com o nº maximo de habitantes
for ind, qt in enumerate(qts): #vamos procurar o valor maximo e a posição onde ocorre
   if qt == maximo: #precisa guardar o nome da cidade da posição ind
      lstmax.append(cidades[ind])

if len(lstmax) == 1:
   print(f"Cidade com mais habitantes é {lstmax[0]} com {maximo} de habitantes")
else:
   print(f"Cidades com mais habitantes é {lstmax} com {maximo} de habitantes cada.")   


#g
   
#cidades=['Lisboa', 'Porto', 'Coimbra', 'Chaves', 'Beja', 'Cerveira', 'Faro', 'Covilhã']
#  qts = [3       ,    2   ,     1    ,     1   ,    1  ,      1    ,    3,        1   ]

#total de pessoas = 11
totpessoas = len(cont)

#totpessoas  -   100%
#  qts[ind]  -     x
#x=qts[ind]*100 / totpessoas

for ind, valor in enumerate(qts):
   x = valor * 100 / totpessoas
   print(f"{cidades[ind]} com {valor} de habitantes corresponde a {x:.1f}%")
'''
#h
'''
print("Antes: \n",cont)

novacid = input("Indique o nome da nova cidade: ")

for ind , pessoa in enumerate(cont): #pessoa = 'Ana,Lisboa,22,Centro'
   dados = pessoa.split(',')#dados = ['Ana','Lisboa','22','Centro']
   op = input(f"{dados[0]}:{dados[1]}. Deseja substituir a cidade {dados[1]}? ")[0].lower()
   if op == 's': #precisa trocar a cidade
      dados[1] = novacid #dados = ['Ana','Caldas','22','Centro']
      novapessoa = ','.join(dados) #'Ana,Caldas,22,Centro'
      cont[ind] = novapessoa
      print(f"Substituição resulta em {novapessoa}.")

print("Depois: \n",cont)
'''

#Ex2
#fich.texto.txt
'''
pos = rfind('.') devolve a posição do . mais à direita
nome = substring à esquerda da pos do .
extensao = substring à direita da posição do .

ciclo de 1 ate 10
   nomefich = nome + nº + extensao
   cria ficheiro para write
'''
'''
#fich.txt
nomefich = input("Indique o nome do ficheiro: ")
pos = nomefich.rfind('.')
nome = nomefich[0:pos] #fich
ext = nomefich[pos:] #.txt

for n in range(1,11):
   novonome = nome + str(n) + ext
   open(novonome,"w").close()
'''
#Ex3
'''
dici = {'Preto':'Black', 'Branco':'White', 'Azul':'Blue', 'Verde':'Green',
        'Vermelho':'Red', 'Amarelo':'Yellow', 'Castanho':'Brown',
        'Rosa':'Pink', 'Laranja':'Orange','Cinzento':'Gray'}

cor = input("Qual a cor que deseja ver traduzida? ").title()
print(f"A tradução de {cor} é {dici[cor]}")


#Caso pretendesse dar o nome em Inglês e descobrie a key em PT
#for chave, valor in dici.items():
#   print(f"CHAVE:{chave}\nVALOR:{valor}")
#   if cor == valor:
#      print("Em PT é ", chave)
'''


#Ex4
'''
dici={'a':4, 'b':2, 'c':1, 'd':3}
#obter lista de valores
lista = list(dici.values())
lista.sort() # lista ordenada
newdici={} #construir o dicionário por ordem

#percorre a lista, um de cada vez (1)
for valor in lista: #[1,2,3,4]
   #obter key do nº 1
   for key, value in dici.items():
      if valor == value:
         #adiciona ao newdici
         newdici[key] = valor #{'c':1,'b':2,'d':3.'a':4}
         break
   
print(newdici) #dicionário ordenado pelos valores
         
#By João Coentrão
#dici={'a':4, 'b':2, 'c':1, 'd':3}
#diciord = sorted(dici.items(), key=lambda x: x[1])
#print(dict(diciord))

#By Ricardo Costa
import operator
dici={'a':4, 'b':2, 'c':1, 'd':3}
sorted_list = sorted(dici.items(),key=operator.itemgetter(1))
print(dict(sorted_list))
'''

#Ex5
'''
dici = {'Preto':'Black', 'Branco':'White', 'Azul':'Blue', 'Verde':'Green',
        'Vermelho':'Red', 'Amarelo':'Yellow', 'Castanho':'Brown',
        'Rosa':'Pink', 'Laranja':'Orange','Cinzento':'Gray'}


for key, value in dici.items(): #(Preto,Black)
   print(f"PT:{key}")
   print(f"ING:{value}")
   corf = input(f"Qual a tradução de {key}/{value} para francês: ").title()
   dici[key] = (value,corf) # {Preto:(Black,Noir), ....}

print(dici)
'''


######################################################
####### tradução de cores e acrescentar idiomas ######

def acrescentar(idiomas, idioma):
   global dici
   idiomas = idiomas + [idioma] #idiomas.append(idioma)
   
   for key, value in dici.items(): #(Preto,(Black,Frances))
      print(f"PT:{key}")
      novacor = input(f"Qual a tradução de {key} para {idioma}: ").title()
      dici[key] = (value) + (novacor,) # {Preto:(Black,Noir), ....} 

   return idiomas


def traduz(idiomas,idioma,corpt):
   for key, values in dici.items():  
      if key == corpt:   #values(ING, FR, ESP)
         indice = idiomas.index(idioma) #.index devolve a posição da lista idiomas
                                      # onde ocorre o idioma desejado                                     
         cor = values[indice]  #indice é posição do idioma na lista idiomas
         print(f"{key}(Português) : {cor}({idioma})")
         return


###################
dici = {'Preto': ('Black', 'Noir'), 'Branco': ('White', 'Blanc'),
        'Azul': ('Blue', 'Bleu'), 'Verde': ('Green', 'Vert'),
        'Vermelho': ('Red', 'Rouge'), 'Amarelo': ('Yellow', 'Jeune'),
        'Castanho': ('Brown', 'Marron'), 'Rosa': ('Pink', 'Rose'),
        'Laranja': ('Orange', 'Orange'), 'Cinzento': ('Gray', 'Gris')}

idiomas=['Inglês', 'Francês']

while True:
   corpt = input("Qual a cor que deseja traduzir? ").title()
   idioma = input(f"Para que idioma deseja traduzir a cor {corpt}? ").title()

   if idioma not in idiomas:
      op = input(f"O idioma {idioma} não existe. Deseja acrescentá-lo? (s/n) ").lower()[0]
      if op == 's':
         idiomas = acrescentar(idiomas, idioma) #retornar lista com todos os idiomas
         traduz(idiomas, idioma,corpt)
      else:
         print(f"Não vai ser possível traduzir para {idioma}.")


   else:
         traduz(idiomas,idioma,corpt)   







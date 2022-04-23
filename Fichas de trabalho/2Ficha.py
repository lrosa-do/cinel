#Ficha 2

#Ex 1
'''
#nome capitalizado, sem espaços
nome = ' '.join(input("Qual o seu nome completo? ").title().split() )

fp = open(input("Qual o nome do ficheiro? "), 'w')
fp.write(nome)
fp.close()
'''
#Ex 2
'''
def determina_nome(nome1, nome2):
   
   ##ola.mundo.html    nomes.docx
   pos = nome1.rfind('.') #devolve posição do ponto a partir da (r)ight
   nome1 = nome1[0:pos] # ola.mundo

   pos = nome2.rfind('.') #devolve posição do ponto a partir da (r)ight
   nome2 = nome2[0:pos] # nomes
   ##     ola.mundo  _    nomes    .txt
   nome3 = nome1 + '_' + nome2 + '.txt'
   return nome3


   
   #Trabalhar com indices negativos. Exemplo de nome1 = ola.mundo.html
   k = -1
   while nome1[k] != '.':
      k = k-1
   #k indica a posição do . enquanto indice negativo (direita para esquerda)
   nome1 = nome1[0:len(nome1) - abs(k)] #abs(-5) = 5

   k = -1
   while nome2[k] != '.':
      k = k-1
   #k indica a posição do . enquanto indice negativo (direita para esquerda)
   nome2 = nome2[0:len(nome2) - abs(k)] #abs(-4) = 4   14-4
  
   nome3 = nome1 + '_' + nome2 + '.txt'
   return nome3



def junta_fich(nome1, nome2):
   #criar apontador para cada 1 dos ficheiros
   fich1 = open(nome1, "r")
   fich2 = open(nome2, "r")
   #obter conteúdo
   cont1 = fich1.read() #lê conteúdo como sendo string
   cont2 = fich2.read()
   #fechar os apontadores
   fich1.close()
   fich2.close()

   ##VERIFICA SE CONTEUDO 1 NÃO TERMINA EM '\n'
   if cont1[-1] != '\n': #acrescentar '\n'
      cont1 = cont1 + '\n'

   cont3 = cont1 + cont2 #concatena os 2 conteudos
   #conteudo 3 deve ser gravado no ficheiro de saida

   nome3 = determina_nome(nome1, nome2) #função que retorn o nome de saida

   fich3 = open(nome3, "w")#cria o ficheiro saida.txt
   fich3.write(cont3) 
   fich3.close()#fechar o ficheiro 3

##########################
nome1 = input("insira o nome do 1º ficheiro: ")
nome2 = input("insira o nome do 2º ficheiro: ")
junta_fich(nome1, nome2)
'''

#Ex3
'''

nome = input("insira o nome do 1º ficheiro: ")
pal = input("Qual a palavra a procurar? ")

fich = open(nome, "r")
cont = fich.read()
fich.close()

qt = cont.count(pal)

if qt == 0:
   print(f"A palavra {pal} não ocorre no ficheiro.)
else:
   print(f"A palavra {pal} ocorre {qt} vezes no nosso ficheiro.")
'''
'''
#Procurar palavra dada

nome = input("insira o nome do 1º ficheiro: ")
pal = input("Qual a palavra a procurar? ")
fich = open(nome, "r", encoding="UTF-8")
cont = fich.readlines() #carrega cada linha para uma lista
fich.close()
qt = 0
for frase in cont: #['Falar é fácil. Mostre-me o código. (Linus Torvalds)\n', ...]
   listfrase = frase.split() #['Falar', 'é', 'fácil.', 'Mostre-me', 'o', 'código.', '(Linus', 'Torvalds)']
   for palavra in listfrase:
      if(pal == palavra):      
         qt = qt + 1
      elif(pal in palavra) and (palavra[len(pal)] in ".,!?;:"):  
            qt = qt+1

#https://www.delftstack.com/pt/howto/python/python-count-words-in-string/
'''

#Ex4
'''
fich = open("pensamentos.txt", "r", encoding="UTF-8")
cont = fich.read()
fich.close()

print(f"O conteúdo do ficheiro é:\n{cont}")

#pedir a sequência a substituir
seq_sai = input("Qual a sequência a remover? ")
seq_entra = input(f"Qual a palavra a substituir {seq_sai}? ")

cont = cont.replace(seq_sai, seq_entra)

fich = open("pensamentos2.txt", "w", encoding="UTF-8")
fich.write(cont)
fich.close()
'''
#Ex5
'''
#a
fich = open("pensamentos.txt", "r", encoding="UTF-8")
cont = fich.read()
fich.close()

qtlinhas = cont.count('\n')
if cont[-1] != '\n':
   qtlinhas +=1
  
print(f"Nº de linhas: {qtlinhas}")

listapal = cont.split()
print(f"Nº de palavras: {len(listapal)}")

vogais = "aeiouáàãâéêíóôõú"

qtvog, qtcons = 0, 0
for carater in cont:
   if carater.lower() in vogais:
      #print(f"{carater} é vogal")
      qtvog += 1
   elif 'a' < carater.lower() <= 'z' or carater.lower() == 'ç':
      #print(f"{carater} é consoante")
      qtcons += 1

print(f"Quantidade de vogais: {qtvog}")
print(f"Quantidade de consoantes: {qtcons}")

cont = cont.split('\n') #conteúdo convertido em lista
#print(cont)

#b
qt = 0
numlinha = []
pal = input("Qual a palavra a procurar? ")
for pos, frase in enumerate(cont):
   if pal in frase:
      qt = qt + frase.count(pal)
      numlinha.append(pos+1)

print(f"A palavra {pal} ocorre {qt} vezes nas linhas {numlinha}")
'''

#Ex6

fich1 = open("fich1.txt", "r", encoding="UTF-8")
cont1 = fich1.readlines() #['Olá mundo.\n', 'Hoje chove.\n']
fich1.close()
fich2 = open("fich2.txt", "r", encoding="UTF-8")
cont2 = fich2.readlines() #['Amanhã fará sol.','Palavra.\n']
fich2.close()
fich3 = open("final.txt", "w", encoding="UTF-8")

#última frase, último carater, acrescentar \n
if cont1[-1][-1] != '\n': #'Hoje chove.\n'
   cont1[-1] = cont1[-1] + '\n'

#1ªfrase, eliminar \n pois será a última a ser acrescentada
if cont2[0][-1] == '\n': #'Amanhã fará sol.'
   cont2[0] = cont2[0].replace('\n','')

#última frase, último carater, acrescentar \n
if cont2[-1][-1] != '\n': #'Palavra.\n'
   cont2[-1] = cont2[-1] + '\n'
   
final = cont1 + cont2[::-1] #as frases do 2º conteudo é invertido

fich3.writelines(final)
fich3.close()















texto = input("Escreve uma frase !")#"Luis Miguel Rosa dos Santos 44"

def convert(list):
    return tuple(i for i in list)
    
def calcular(frase):
    nMas,nMin,nDig= 0,0,0
    for f in frase:
        if f.isupper():
            nMas += 1;
        elif f.islower():
            nMin += 1;
        elif f.isnumeric():
            nDig += 1;
    
    return(nMas,nMin,nDig)

tup   = calcular(texto)
count = tup[0]

if count ==0:   
    print("Não encontramos  letras  maiusculas na frase.")
elif  count ==1:   
    print(f"Encontramos {count} letras  maiusculas na frase.")
else:
    print(f"Encontramos {count} letras  maiusculas na frase.")

count = tup[1]
if count ==0:   
    print("Não encontramos  letras  minusculas na frase.")
elif  count ==1:   
    print(f"Encontramos {count} letras  minusculas na frase.")
else:
    print(f"Encontramos {count} letras  minusculas na frase.")

count = tup[2]
   
if count ==0:   
    print("Não encontramos  numeros na frase.")
elif  count ==1:   
    print(f"Encontramos {count} numero na frase.")
else:
    print(f"Encontramos {count} numeros na frase.")




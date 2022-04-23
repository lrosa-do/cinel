def substituir(tuplo, valor_a_subs, valor_substituto):
    result = ()
    for valor in tuplo:
        if valor == valor_a_subs:
            result = result + (valor_substituto,)
        else:
            result = result + (valor,)
    return result
    

res = substituir ( (1,2,3,2,3,4,1), 2, 7) 
#(1,7,3,7,3,4,1)
print(res);
    
    

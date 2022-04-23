'''
Dadas 2 strings, crie uma função que retorne um tuplo com os caracteres comuns de ambas strings.
'''
def convert(list):
    return tuple(i for i in list)
    
def str_comuns(st1,st2):
    len_s1= len(st1)
    len_s2= len(st2)
    result =()
    print(st1)
    print(st2)
    for x in st1:
        if (x in st2) and (x != ' ') and not ( x  in result):
            result = result + (x,)
    return result
            
            
r = str_comuns("ola mundo","oi cara")
print(r)

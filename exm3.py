''''
t1 = (2,5,3), t2 = (5,0,2), o resultado é (2+5, 5+0, 3+2) = (7,5,5)
'''
def convert(list):
    return tuple(i for i in list)
    
def cal_my_tuples(t1,t2):
    len_01 = len(t1)
    len_02 = len(t2)
    if (len_01!=len_02):
        print("As tuplas teem que conter os mesmos valores")
        return None
    lista = ()
    for v in range(0,len_01):
        lista = lista + (( t1[v] + t2[v]),)
    return lista
    
    
    
t1 = (2,5,3) 
t2 = (5,0,2)

t3 = cal_my_tuples(t1,t2)

print(t3)

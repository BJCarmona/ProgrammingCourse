# Funcion que devuelve una lista invertida de manera recurrente
# Se puede utilizar el concat de python + o  [:]
# No es permitido utilizar funciones build in <nombre>(_)
# solo es pormitido utiliar pop()

def reverse_recursive(lista, lista_inv_accum=[]):
    if len(lista) == 0:  # caso base
        return lista_inv_accum
    else:
        lista_inv_accum+=[lista.pop()]
        return reverse_recursive(lista, lista_inv_accum)

# Suma de una lista  ...
def sum_recursive(lista,accum=0):
    try:
        if len(lista) == 0:  # caso base
            return accum
        else:
            accum+=lista.pop()
            return sum_recursive(lista,accum)
    except TypeError:
        print("Tus papás son primos")

# encontrar el maximo  ...
def max_recursive(lista,maximo=0):
    if len(lista) == 0:  # caso base
        return maximo
    else:
        b=lista.pop()
        if b>maximo:
            maximo=b
        return max_recursive(lista,maximo)

# encontrar la posicion de la primera ocurrencia de izquierda a derecha de un numero ...
# input [2,4,5,6,7], 5
# output 2
class MiExcepcion(Exception):
    pass

def find_recursive(lista,num,pos=None,idx=0):
    if isinstance(num, int) and isinstance(lista[idx], int):
        if idx == len(lista):
            return pos
        if lista[idx]==num:
            pos=idx
            return pos
        else:
            return find_recursive(lista,num,pos,idx+1)
    else:
        raise MiExcepcion("pendejo de M*****")



try:
    print(reverse_recursive([1,2,3,4,5,6,7,8,9,0,"hola"]))
except ZeroDivisionError:
    print("No se apene")
  
print(sum_recursive([1,2,3,4,5,6,7,8,9,"hola"]))

try:
    print(max_recursive([1,2,3,-1,5,6,12,8,9,"hola"]))
except TypeError:
    print("No se apene")


try:
    print(find_recursive([1,2,3,-1,5,6,12,8,9,10],"hola"))
except MiExcepcion as e:
    print(e)




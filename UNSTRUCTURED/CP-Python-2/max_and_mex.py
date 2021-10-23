# you are given a set of n distinct non-negative integers initially.
# multiset is a set that may contain repeated elements.
# Over k iterations, perform the following:
# Add (a+b)/2 rounded up into S, where a= mex(S) and b=max(S). Add it even if it is already present in the set.
# mex of a multiset denotes the smallest non-negative integer NOT present in the multiset.

# Task is to calculate the number of DISTINCT eleements in the multiset after k iterations.
import math

def max_mex(mset, n, k):
    # respuesta inicial es longitu de mset
    # incrementa la respuesta cada vez que el nuevo elemento a añadir no exista en mset. y añadirlo a mset
    # usar una lista auxiliar para llevar el multiset (con repeticiones)?

    # Uso de un set basado en arbol -> OrderedDict??
    # TIENES QUE HACER MÁXIMO 1 ESCANEO TIEMPO LINEAL
    # PROFE SUGIERE USO DE C++ POR SER MÁS RÁPIDO Y POR USO DE TREE SET PARA RECORRER EL SET?
    ans = n
    max = -1
    for n in mset:
        if n>max:
            max = n

    mex = 0
    for i in range(max+2):
        if i not in mset:
            mex = i
            break

    for i in range(k):
        new = math.ceil((mex + max) / 2.0)
        if new in mset:
            # max y mex ya no pueden cambiar porque no es un valor nuevo
            return n
        mset.add(new)
        n += 1
        # Find new max
        max = max(max, new)
        # find new mex
        if new==mex:
            pass






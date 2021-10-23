# VARIABLES Y TIPOS DE DATOS
integer = 1    # x es una variable que contiene un 1. Tipo entero
flotante = 1.666   # numero decimal o flotante
string = "Marco"   # string o cadena de texto
var123 = 1
var456 = 2
booleano = True
booleano2 = False

# Sintaxis de Python
lista = [1, 2, 3]

# if (condicion):
#   se corre si es cierto
# else:
#   se corre si no es cierto

# CICLOS
# 1a forma: con ciclo "For", cuando conoces el número de repeticiones
for i in range(3):      # 0, 1 y 2
    print("Numero", i)
    # i se incrementa en cada iteración

# 2a forma: con ciclo "While", cuando NO conoces el número de repeticiones
while (integer < 10):
    integer = integer + 1 # 9 +1 = 10
    print(integer)    # 10

# EXPRESIONES LÓGICAS. devuelven True o False
exp1 = 10 > 100 and 9 < 10
exp2 = 10 > 100 or 9 < 10
my_conjunto = {1, 2, 3}

print(exp2)
mi_conjunto = set()    # le dije a python que mi_conjunto es un conjunto
for i in range(100000000): #999,999
    mi_conjunto.add(i)

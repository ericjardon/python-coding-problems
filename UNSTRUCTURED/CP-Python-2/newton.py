import math
# Declaración de funciones: f y f'
f = lambda x : 10*x**3 - 8*x**2 - (112/x)
df = lambda x : 30*x**2 -16*x + 112/(x**2)

x = 2
epsilon = 0.00001
it = 0      # numero de iteraciones
# nuestra aproximacion f(x) == 0
while (abs( f(x) - 0 ) >= epsilon):
    x = x - (f(x)/df(x))
    it = it + 1

# para cuando la diferencia entre f(x) y 0, sea menor a epsilon
print("Resultado: x=",x)
print("Repeticiones: it=",it)
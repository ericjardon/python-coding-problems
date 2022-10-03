from math import sqrt
from random import random
from typing import Optional

def generateX(R:float) -> Optional[float]:
    # Assumes R is in [0,1]
    if 0<=R<=0.25:
        return 2* sqrt(R) + 2       # produce x en el rango 2 a 3
    elif 0.25< R <= 1:
        return -sqrt(12*(1-R)) + 6  # produce x en el rango 3 a 6
    else: 
        return None

# Generate 1000 random vals
factor = 1.0/1000
randoms = [(i+1)*factor for i in range(1000)]
x_values = [generateX(r) for r in randoms]
#print(x_values)

x_mean = sum(x_values) / 1000
print('Valor promedio:', x_mean)
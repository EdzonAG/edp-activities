import numpy as np
import pandas as pd
# Constantes Default
k = 1e-3
h = 1e-1
r = k/h**2
S = [[]]
# Contantes Definidas
x = 1
j = 25
# Funciones Cond. Iniciales.
u = [lambda x: 2*x, lambda x: 2*(1-x)]
# Vector X
z = int(x/h)
X = np.linspace(0,x,z+1)
# Primer Fila U
for f in X:
    if f <= 0.5:
        S[0].append(u[0](f))
    else:
        S[0].append(u[1](f))
# Filas U
for g in range(j):
    St = []
    for w in range(len(X)-2):
        u = r*S[g][w] + (1-2*r)*S[g][w+1] + r*S[g][w+2]
        St.append(u)
    St.insert(0, 0)
    St.append(0)
    S.append(St)
# Convertir a Tabla
S = np.array(S)
S = np.around(S, decimals=3)
print(S)
# Resultados a CSV
table = pd.DataFrame(S)
table.to_csv('result.csv')
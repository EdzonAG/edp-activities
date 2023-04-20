import numpy as np
import pandas as pd
# Constantes Default
k = 1/200
h = 1e-1
r = k/h**2
S = [[]]
# Contantes Definidas
x = 1
j = int(0.5/k)
# Funciones Cond. Iniciales.
u = lambda x: 100*np.sin(x*np.pi)
U = lambda x: 100*np.exp(-np.pi**2*0.5)*np.sin(np.pi*x)
# Vector X
z = int(x/h)
X = np.linspace(0,x,z+1)
# Primer Fila U
for f in X:
#     if f <= 0.5:
#         S[0].append(u[0](f))
#     else:
#         S[0].append(u[1](f))
    S[0].append(u(f))

# Filas U
for g in range(j):
    St = []
    for w in range(len(X)-2):
        u = r*S[g][w] + (1-2*r)*S[g][w+1] + r*S[g][w+2]
        St.append(u)
    St.insert(0, 0)
    St.append(0)
    S.append(St)
# Comparación
Sol = []
for i in X:
    Sol.append(U(i))
Sol = np.array(Sol)
absoluto = np.linalg.norm(Sol-S[-1])
error = absoluto/np.linalg.norm(Sol) * 100
print(Sol)
print(S[-1])
# Redondear
F = np.around(S, decimals=3)
print(f'{error}%')
# Resultados a CSV
table = pd.DataFrame(F)
table.to_csv('result.csv')
import numpy as np
import pandas as pd

# Constants
h = 1/10
k = 1/100
r = k/h**2
S = [[]]

# Defined Constants
x = 1
j = int(0.5/k)

# Initial Functions
u = [lambda x: 2*x,lambda x: 2*(1-x)]
n = 20

# X vector
z = int(x/h)
X = np.linspace(0,x,z+1)

# First Row

for i in X:
    if i <= 0.5:
        S[0].append(u[0](i))
    else:
        S[0].append(u[1](i))
        
# U Matrix
m = [-r, 2*(1+r)]
M = np.zeros((5,5))
cont = 0
for i in M:
    if cont == 0:
        i[cont] = m[1]
        i[cont+1] = m[0]
    elif cont == len(i)-1:
        i[cont-1] = m[0]*2
        i[cont] = m[1]
    else:
        i[cont-1] = m[0]
        i[cont] = m[1]
        i[cont+1] = m[0]
    cont += 1

for k in range(n):
    MS = np.zeros(5)
    for i in range(len(MS)):
        MS[i] = r*S[k][i] + 2*(1-r)*S[k][i+1] + r*S[k][i+2]

    Sol = np.linalg.solve(M,MS)

    St = []
    for i in range(len(S[0])-2):
        if i < 5:
            St.append(Sol[i])
        else:
            St.append(Sol[-(i-3)])
    St.insert(0, 0)
    St.append(0)
    S.append(St)
    
F = np.around(S, decimals=4)
table = pd.DataFrame(F)
table.to_csv('explicito.csv')
# print(np.round(S, decimals=3))
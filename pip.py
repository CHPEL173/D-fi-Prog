import numpy as np
from random import *


a = np.array([0, 1, 3, 2, 3, 1, 0, 5, 6, 5, 3, 5, 0, 3, 6, 2, 6, 3, 0, 4, 3, 5, 6, 4, 0])
chemins = a.reshape(5, 5)

for k in range(200):
    for i in sample(range(5), 5):
        route = 0
        retour = []
        for j in sample(range(5), 5):
            if i == j:
                route += 0
            elif i != j:
                route += chemins[i][j]
                retour.append([i, j])

                i = j
        print(route)
        print(retour)
    print("Fin de la boucle {}".format(k))




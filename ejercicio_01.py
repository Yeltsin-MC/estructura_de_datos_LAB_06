"""Realizar operaciones de unión, intersección y diferencia
de 3 conjuntos"""

A={4,8,6,2,10,12,17,5}
B={1,8,5,6,12,14,11,22}
C={9,2,7,6,14,12,6,21}

print("De los conjuntos...","A=",A,"B=",B,"C=",C)
#union de conjuntos
print(type(A))
print("La union de los tres conjuntos es: ",A.union(B,C))

#intersección de conjuntos
print("La intersección de los tres conjuntos es :",A.intersection(B,C))

#diferencia de conjuntos
print("la diferencia de los tres conjuntos es :",A.difference(B,C))

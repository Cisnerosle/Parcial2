from modulos_algebra import *

#ejemplos de las definiciones algebraicas 

print("Matrices")
A=[[1,2,3],[4,5,6]]
B=[[7,8],[9,10],[11,12]]

Multiplicacion(A,B)

print("------------")
print("Matriz Transpuesta:")
MatrizAT=Transpuesta(A)
for fila in MatrizAT:
    print(fila)

#########################

G = [[3,-1,2,5],
     [6,-2,1,0],
     [-4,-2,2,6]]

print("------------")
print("Gauss Jordan de la matriz G:")
print(gauss(G))


#########################

D = [[3,-1,2],
     [6,-2,1],
     [-4,-2,2]]

print("------------")
print("Determinante de la matriz D:")
print(determinante(D))


##################################

Vector1=[1,2,3]
Vector2=[7,6,5]

print("------------")
print("Producto vectorial entre ambos:")

Vector3=productoVectorial(Vector1,Vector2)
print(Vector3)

print("------------")
print("Producto escalar entre ambos:")

escalar=productoEscalar(Vector1,Vector2)
print(escalar)

#########################

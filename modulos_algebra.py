#matriz transpuesta

def Transpuesta(Matriz1):
    
    m=len(Matriz1)#filas
    n=len(Matriz1[0])#columnas
    Matriz_Transpuesta=[]#Matriz Vacía

    for i in range(n):
        fila=[]#fila vacía
        for j in range(m):
            fila.append(Matriz1[j][i]) #Agregar a la fila los elementos de la columna [j][i]
        Matriz_Transpuesta.append(fila)

    return Matriz_Transpuesta


#producto vectorial

def productoVectorial(vector1,vector2):
    vector3=[(vector1[1]*vector2[2]-vector1[2]*vector2[1]),
             (vector1[2]*vector2[0]-vector1[0]*vector2[2]),   #para productos vectoriales de 2 o 3 dimensiones
             (vector1[0]*vector2[1]-vector1[1]*vector2[0])]

    return vector3


#producto escalar

def productoEscalar(Vector1,Vector2):
    escalar=0
    for i in range(len(Vector1)):
        escalar+= Vector1[i]*Vector2[i]

    return escalar


#multiplicacion de matrices

def Multiplicacion(A,B):
    print("Matriz A")
    for filas in A:       #muestra la primera matriz
        print(filas)
    print("------------")

    filasA=len(A)
    columnasA=len(A[0])

    print("Matriz B")
    for filas in B:      #muestra la segunda matriz
        print(filas)
    print("------------")

    filasB=len(B)
    columnasB=len(B[0])

    C=[]

    if columnasA == filasB:
        for i in range(filasA):
            fila=[] #
            for j in range(columnasB):
                elemento = productoEscalar(A[i],Transpuesta(B)[j])
                fila.append(elemento)
            C.append(fila)

        print("Matriz C")
        for filas in C:
            print(filas)

    else:
        print("No se pueden multiplicar no tienen dimensiones correctas")
    return C 

#Gauss Jordan

def gauss (n):
    for j, a in enumerate(n):
        if a[j] != 0:
            divisor = a[j]
            for i, b in enumerate(a):
                a[i] = b / divisor 

        lista = [ c for c in range (len(n))]
        lista.remove(j)
        
        for i in lista:
            inverso = -1 * n[i][j]
            for ind, value in enumerate (n[i]):
                n[i][ind] = value + inverso * n[j][ind]
    return n

#Determinante de una matriz

def determinante(A):
    filasA = len(A)
    columnasA = len(A[0])
    determinante_Nuevo=0
    
    if filasA == columnasA:
        if filasA == 1 and columnasA == 1:
            det=A[0][0]
            return det

        else:
            for i in range(columnasA):
                Matriz_Nueva=list(A)

                Matriz_Nueva.remove(Matriz_Nueva[0])
                Matriz_Nueva=Transpuesta(Matriz_Nueva)
                Matriz_Nueva.remove(Matriz_Nueva[i])
                Matriz_Nueva=Transpuesta(Matriz_Nueva)

                determinante_Nuevo += A[0][i]*((-1)**(1+(i+1)))*(determinante(Matriz_Nueva))
                return determinante_Nuevo
    else:
        print("No se puede calcular el determinante")
        return None
        


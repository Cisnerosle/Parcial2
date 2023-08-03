
def codificar(texto):
    texto_Nuevo=''
    for i in texto:
        num=ord(i)
        num+=1
        textoNuevo+=chr(num)
    
    return textoNuevo

def decodificar(texto):
    texto_Nuevo=''
    for i in texto:
        num=ord(i)
        num-=1
        texto_Nuevo+=chr(num)
    
    return texto_Nuevo

############################

texto1 = input("frase a codificar: ")

texto2=codificar(texto1)
print(texto2)

print("texto decodificado:")
print(decodificar(texto2))


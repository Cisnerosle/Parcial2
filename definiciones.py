#Validacion de numeros enteros

def ValInt(num,lista=0):
    
    if isinstance(num,int) and lista==0:
        print(True)
        return True

    elif isinstance(num,float):
        print(False)
        return False

    elif isinstance(num,int) and isinstance(lista,list):
        if lista[0]<lista[1]:
            if num>=lista[0] and num<=lista[1]:
                print(True)
                return True

            else:
                print(False)
                return False
        else:
            print("Value Error")
            return "Value Error"

    elif isinstance(num,int) and isinstance(lista,tuple):
        if num>lista[0] and num<lista[1]:
            print(True)
            return True

        else:
            print(False)
            return False
    
    elif isinstance(num,int) and isinstance(lista,int):
        print("TypeError")
        return "TypeError"
    
    #Validacion de numeros flotantes (con decimales)

    def ValFloat(num,lista=0):
        if isinstance(num,float) and lista==0:
            print(True)
            return True

        elif isinstance(num,int):
            print(False)
            return False

        elif isinstance(num,float) and isinstance(lista,list):
            if lista[0]<lista[1]:
                if num>=lista[0] and num<=lista[1]:
                    print(True)
                    return True

            else:
                print(False)
                return False
        else:
            print("Value Error")
            return "Value Error"
    
#Validacion de numeros complejos

def valComplex(num,lista=0):
    if isinstance(num,complex) and lista==0:
        print(True)
        return True

    elif isinstance(num,float) or isinstance(num,int):
        print(False)
        return False

    elif isinstance(num,complex) and isinstance(lista,list):
        if lista[0]<lista[1]:
            if (num.real**2+num.imag**2)**(1/2)>=lista[0] and (num.real**2+num.imag**2)**(1/2)<=lista[1]:
                print(True)
                return True

            else:
                print(False)
                return False
        else:
            print("Value Error")
            return "Value Error"

    elif isinstance(num,complex) and isinstance(lista,tuple):
        if (num.real**2+num.imag**2)**(1/2)>lista[0] and (num.real**2+num.imag**2)**(1/2)<lista[1]:
            print(True)
            return True

        else:
            print(False)
            return False

    elif isinstance(num,complex) and isinstance(lista,int):
        print("TypeError")
        return "TypeError"
    
#Validacion de Listas de Numeros

def valList(lista1,lista2=0,instruccion=''):

#Casos True
    if isinstance(lista1,list) and lista2==0 and instruccion=="":
        print(True)
        return True

    elif instruccion=='value' and (isinstance(lista1,list) and isinstance(lista2,list)) and (lista1==lista2):
        print(True)
        return True

    elif instruccion=="len" and (isinstance(lista1,list) and isinstance(lista2,int)) and (len(lista1)==lista2):
        print(True)
        return True

#casos False
    elif isinstance(lista1,int) or isinstance(lista1,float) or isinstance(lista1,complex) or isinstance(lista1,tuple):
        print(False)
        return False

    elif instruccion=='value' and (isinstance(lista1,list) and isinstance(lista2,list)) and (lista1!=lista2):
        print(False)
        return False

    elif instruccion=="len" and (isinstance(lista1,list) and isinstance(lista2,int)) and (len(lista1)!=lista2):
        print(False)
        return False

#casos TypeError
    elif (isinstance(lista2,str) or isinstance(lista2,list) or isinstance(lista2,float)) or (isinstance(instruccion,int) or isinstance(instruccion,float) or isinstance(instruccion,list) ):
        print("TypeError")
        return "TypeError"

    elif (isinstance(lista2,str) or isinstance(lista2,int) or isinstance(lista2,float)) or (isinstance(instruccion,int) or isinstance(instruccion,float) or isinstance(instruccion,list) ):
        print("TypeError")
        return "TypeError"
    


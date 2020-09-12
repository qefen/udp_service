import random

#Bandera para saber cuando usuario escribio un numero valido para el intervalo
num_rigth=True

#Bandera para saber cuando el usario acerto el numero
bandera=True

#Contador de Intentos para adivinar
attempts=1

while num_rigth:

    #Tomando datos del usuario
    first = input ("Numero Inicial :")
    last = input ("Numero Final :") 

    
    if int(first)>int(last):
        print("El numero inicial debe ser mayor que el numero final")
    else:
        print("Adivina el numero entre "+str(first)+" y "+str(last))
        
        #Generando un numero aleatorio entre los numeros del usuario
        num_aleatorio = random.randint(int(first),int(last))
        num_rigth=False

print(num_aleatorio)

while bandera: 
    val = input("Entra un numero : ")

    #Si el numero ingresado es menor  
    if int(val)<num_aleatorio:
        print("Un poco mas")

    #Si el numero ingresado es mayor    
    elif int(val)>num_aleatorio:
        print("Un poco menos")   

    #Si el numero es igual
    if int(val)==num_aleatorio:
        print("Acertaste :)")
        print("Total de intentos :"+str(attempts))
        bandera=False

    #Si el numero no es igual 
    # entonces aumenta el contador de inentos    
    else:
        attempts=attempts+1    
    
        
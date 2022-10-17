import random
import sys


def adivina_numero():
    #mediante la función opciones definimos el nivel de dificultad
    minimo, maximo, intento_maximo = opciones()
    #generamos aleatoriomente un numero a adivinar
    numero=random.randint(minimo, maximo)
    
    n_intentos=0
    #Bucle para evaluar el intento
    while n_intentos!=intento_maximo:
    
        n_intentos+=1
        #llamamos a la funcion solicitar intentos.
        intento= solicitar_intento(minimo, maximo, intento_maximo)

        if intento<numero:
            print("demasiado pequeño", "\n")
            #Acortara el rango
            minimo=intento+1
            print("Intento={}".format(n_intentos))
            victoria=False

        elif intento>numero:
            print("demasiado grande", "\n")
            print("Intento={}".format(n_intentos))
            #Acortara el rango
            maximo=intento-1
            victoria=False
               
        else: 
            print("Has ganado")
            print("Has adivinado el número en {} intento/s!".format(n_intentos))
            victoria=True
            break

    #en caso de no adivinar se mostara el  numero por pantalla
    if numero!=intento:
        print("El numero pensado era {}".format(numero))
         
        


    return   victoria, minimo, maximo, n_intentos, intento_maximo
    

#Funcion para evaluar que el numero dado por pantalla es un numero
def pedir_numero():
    while True:
        #Bucle infinito
        valor=input("Introduce un valor: ")
        try:
            valor=int(valor)
        except:
            print("Valor no numérico", file=sys.stderr)
        else:
            break
            sys.exit()
    return valor

#Funcion para evaluar  que el numero dado por pantalla esta en el rango dado
def solicitar_intento(minimo, maximo, intento_maximo):
    invitacion="Adivine un número"
    while True:
        #nucle infinito 


        invitacion= "{} entre {} y {} incluídos. Tiene como maximo {} intentos".format(invitacion, minimo, maximo, intento_maximo)
        print(invitacion)
        dato= pedir_numero()
        try:
            minimo<=dato<=maximo
        except:
            print("{} no está entre {} y {}".format(dato,minimo,maximo))
            pass
        else:
            break 
            sys.exit()
    
    return dato       

""""
def IA(minimo, maximo, intento_maximo):
    dato=random.randint(minimo,maximo)
    print("El numero elegido es el {}".format(dato))
    return dato


def jugador(minimo, maximo, intento_maximo):
    while True:
        jugador=input("¿Quién juega? \n A.Persona \n B.IA \n")
        for letra in jugador:
            if letra=="a" or "A":
                dato=solicitar_intento(minimo, maximo, intento_maximo)
                break
    
            if letra=="b" or "B":
                dato=IA(minimo, maximo, intento_maximo)
                break
        
        break
        break
    

    return dato     
"""
#Funciones que nos permite definir la cantidad de veces que queremos jugar
SI=('si', 'Si', 'Yes', 'yes', 'verdadero', 'true', '1', 'YES', 'SI', 'VERDADERO', 'TRUE')
def desea_jugar(invite):
    if input(invite) in SI:
        return True
    else:
        return False 

import pickle
from tabulate import tabulate

#funcion responsable de cada juego
def jugar_partida():
    usuario=input("Usuario: ")
    tabla=[["Usuario","Intentos"]]

    while True:

        #Nos permite jugar varias veces
        #bucle infinito

        #llamamos a la funcion que nos permite jugar

        victoria, minimo, maximo, n_intentos, intento_maximo = adivina_numero()

        #Intento de crear una tabla con los intentos
        tabla.append([usuario, n_intentos])
    

        ArchivoBinario=open("ArchivoLista", "wb")

        pickle.dump(tabla, ArchivoBinario)


        ArchivoBinario.close()


        

        #El bucle solo se rompera si se adivina el numero dentro de los intentos establecidos
        #o se acaban los intentos

        if n_intentos==intento_maximo or victoria==True:
            break
    print(tabulate(tabla))       
    return  minimo, maximo, victoria    
            
#Funcion principal
def jugar():
    while desea_jugar("Desea jugar: ")==True: #Bucle inifinito hasta que se quiera dejar de jugar
        jugar_partida() #Llamamos a la segundo funcion principal
    return "FIN DEL JUEGO"#Senal que de que se terminado el programa

#Funciones que nos permite determinar la dificultad de la actividad.
 
def opciones():
    print(
        "Opción 1. Nivel 1",
        "Opción 2. Nivel 2",
        "Opción 3. Nivel 3",
        "Opción 4. Nivel 4"
    )

    opcion=input("INTRODUZCA OPCIÓN: ")

    #Dependiendo de la opcion elegida, variara el valor maximo del ramngo y el numero maximo de intentos
    if opcion=="1":
        MIN=0
        MAX1=100
        minimo=MIN
        maximo=MAX1
        intento_maximo=10
        

    elif opcion=="2":
        MIN=0
        MAX2=1000
        minimo=MIN
        maximo=MAX2
        intento_maximo=15
        

    elif opcion=="3":
        MIN=0
        MAX3=10**6
        minimo=MIN
        maximo=MAX3 
        intento_maximo=20

        
         
    else:
        MIN=0
        MAX4=10**12 
        minimo=MIN
        maximo=MAX4  
        intento_maximo=25
        
    
    return minimo, maximo, intento_maximo
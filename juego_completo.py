import pickle
import random


def adivina_numero():
    minimo, maximo, intento_maximo = opciones()
    numero=random.randint(minimo, maximo)
    n_intentos=0
    while n_intentos!=intento_maximo:
    
        n_intentos+=1
        intento= solicitar_intento(minimo, maximo, intento_maximo)

        if intento<numero:
            print("demasiado pequeño", "\n")
            minimo=intento+1
            print("Intento={}".format(n_intentos))
            victoria=False

        elif intento>numero:
            print("demasiado grande", "\n")
            print("Intento={}".format(n_intentos))
            maximo=intento-1
            victoria=False
               
        else: 
            print("Has ganado")
            print("Has adivinado el número en {} intento/s!".format(n_intentos))
            victoria=True
            break
        
    if numero!=intento:
        print("El numero pensado era {}".format(numero)) 
        no_intento=True 


    return   victoria, minimo, maximo, n_intentos, intento_maximo
    


def pedir_numero():
    while True:
        valor=input("Introduce un valor: ")
        try:
            valor=int(valor)
        except:
            print("Valor no numérico", file=sys.stderr)
        else:
            break
            sys.exit()
    return valor

def solicitar_intento(minimo, maximo, intento_maximo):
    invitacion="Adivine un número"
    while True:
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
import sys

SI=('si', 'Si', 'Yes', 'yes', 'verdadero', 'true', '1', 'YES', 'SI', 'VERDADERO', 'TRUE')
def desea_jugar(invite):
    if input(invite) in SI:
        return True
    else:
        return False 




from tabulate import tabulate

def jugar_partida():
    usuario=input("Usuario: ")
    tabla=[["Usuario","Intentos"]]
    while True:
        victoria, minimo, maximo, n_intentos, intento_maximo = adivina_numero()

        tabla.append([usuario, n_intentos])
    

        ArchivoBinario=open("ArchivoLista", "wb")

        pickle.dump(tabla, ArchivoBinario)


        ArchivoBinario.close()


        



        if n_intentos==intento_maximo or victoria==True:
            break
    print(tabulate(tabla))       
    return  minimo, maximo, victoria    
            

def jugar():
    while desea_jugar("Desea jugar: ")==True:
        jugar_partida()
    return "FIN DEL JUEGO"

def opciones():
    print(
        "Opción 1. Nivel 1",
        "Opción 2. Nivel 2",
        "Opción 3. Nivel 3",
        "Opción 4. Nivel 4"
    )

    opcion=input("INTRODUZCA OPCIÓN: ")

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
        intento_maximo=8
        

    elif opcion=="3":
        MIN=0
        MAX3=10**6
        minimo=MIN
        maximo=MAX3 
        intento_maximo=6
        
         
    else:
        MIN=0
        MAX4=10**12 
        minimo=MIN
        maximo=MAX4  
        intento_maximo=4
        
    
    return minimo, maximo, intento_maximo
    
print(jugar())
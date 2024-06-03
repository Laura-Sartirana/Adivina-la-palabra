print ("Bienvenidos al juego")
nombre_jugador = input("Ingrese su nombre:  ")
print (f"Hola {nombre_jugador}! El juego consiste en adivinar la palabra secreta. Recuerde que tiene 5 vidas.")
print ("¡Vamos a jugar!")
print ("========================================================================")
from random import choice
palabras = ["playa", "patria", "bandera", "atardecer", "futbol", "familia", "amigos"]
palabra_oculta = choice (palabras)
for letra in palabra_oculta: 
    print ("_")
letras_adivinar = set (palabra_oculta)
print("=============================================================================")
entrada = 5
entrada = letras_adivinar 
entrada = input("Ingrese una letra: ")
if entrada in palabra_oculta:
    print ("¡Bien hecho! Sigue adelante")
else:
    print ("¡No es correcto! Vuelve a intentarlo")
print ("==============================================================================")
letra_incorrecta = entrada != palabra_oculta
if entrada in palabra_oculta:
    print (f"_ \n {entrada}")
else:
    letra_incorrecta = [entrada]
    print (letra_incorrecta)
    print ("cantidad de intentos pendientes: 4")
print("=============================================================================")
entrada = input("Ingrese una letra: ")
if entrada in palabra_oculta:
    print ("¡Bien hecho! Sigue adelante")
else:
    print ("¡No es correcto! Vuelve a intentarlo")
if entrada in palabra_oculta:
    print (f"_ \n {entrada}")
else:
    letra_incorrecta = [entrada]
    print (letra_incorrecta)
    print ("cantidad de intentos pendientes: 3")
print("=============================================================================")
entrada = input("Ingrese una letra: ")
if entrada in palabra_oculta:
    print ("¡Bien hecho! Sigue adelante")
else:
    print ("¡No es correcto! Vuelve a intentarlo")
if entrada in palabra_oculta:
    print (f"_ \n {entrada}")
else:
    letra_incorrecta.append (entrada)
    print (letra_incorrecta)
    print ("cantidad de intentos pendientes: 2")
print("=============================================================================")
entrada = input("Ingrese una letra: ")
if entrada in palabra_oculta:
    print ("¡Bien hecho! Sigue adelante")
else:
    print ("¡No es correcto! Vuelve a intentarlo")
if entrada in palabra_oculta:
    print (f"_ \n {entrada}")
else:
    letra_incorrecta.append (entrada)
    print (letra_incorrecta)
    print ("cantidad de intentos pendientes: 1")
print("=============================================================================")
entrada = input("Ingrese una letra: ")
if entrada in palabra_oculta:
    print ("¡Bien hecho!")
else:
    print ("¡No es correcto!")
print("=============================================================================")
palabra = input ("Ingrese la palabra secreta: ")
if  palabra == palabra_oculta:
    print ("Felicitaciones! Ganaste el juego")
else:
    print (f"No es correcto. La palabra oculta era: {palabra_oculta}")
    print ("Lo siento, perdiste el juego")
print("=============================================================================")

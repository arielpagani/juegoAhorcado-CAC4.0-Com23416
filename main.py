# Importamos modulos de los archivos palabraRandom, esqueleto y registro_puntos dentro de la carpeta resources
import resources.modules.palabraRandom as palabraRandom
import resources.modules.esqueleto as esqueleto
import resources.modules.registro_puntos as registro_puntos

nueva_partida = "S"

while nueva_partida != "N":                         # Bucle para iniciar y volver a comenzar partida

    palabra = palabraRandom.palabra_elegida()       # Elección de la palabra
    longitud = len(palabra)                         # Cantidad de letras que tiene la palabra
    lista = list(palabra)                           # La convertimos en una lista cuyos elementos son las letras 
                                                    #de la palabra ordenadas, para trabajarlo con más opciones
    letras_ingresadas = list()                      # Lista de letras ingresadas mientras el juego está activo
    palabra_adivinando = list(("_" * len(lista)))   # Lista que creamos con "_". Tantos guiones como letras tenga 
                                                    #la palabra. Serán reemplazados con las letras que el usuario
                                                    #vaya acertando.
    errores = 0                                     # El usuario comienza una nueva partida con 0 errores,
    acumulador = 0                                  # y con 0 letras encontradas (luego el acumulador indicará 
                                                    #la cantidad de letras encontradas)

    print("""                                       
           *** JUEGO DEL AHORCADO ***
        Bienvenido a una nueva partida!!!
    """)                                            # Imprimimos un mensaje al comenzar el juego
    esqueleto.figura(errores)                       # Y debajo la figura que se irá completando a medida que el 
                                                    #usuario no acierte las letras
    print(f"""         
       La palabra a adivinar tiene {longitud} letras:
       PALABRA: {" ".join(palabra_adivinando)}
          
    """)                                            # Convertimos la lista de guiones en un string de guiones para 
                                                    #que se visualice en pantalla con el formato tradicional. 
    print("       **************************************************************") 
                                                    # Se imprime un separador para darle un diseño más ordenado
    while errores < 6 and lista != palabra_adivinando:  
                                                    # Bucle principal del juego. Validamos que no se llegue al 
                                                    #máximo de errores y la palabra no este completa para entrar
        letra = input(f"       Introduce una letra o '1' si quieres arriesgar la palabra: ")
                                                    # El usuario en todo momento puede indicar una letra  
                                                    #o arriesgar la palabra ingresando "1".
        
        print("       **************************************************************")
        letra = letra.lower()
        if len(letra) == 1 and letra.isalpha():     # Validamos si tiene más de una letra o ingresa un caracter que 
                                                    #no sea letra.

            while letra in letras_ingresadas:       # Si ingresa una letra ya ingresada anteriormente, el programa le 
                                                    #avisará y volverá al paso anterior.
                print("       Letra ya ingresada, pruebe con otra: ")
                print(f'       Letras ya ingresadas: {" ".join(letras_ingresadas)}')
                letra = input(f"       Introduce una letra o '1' si quieres arriesgar la palabra: ")
                print("       **************************************************************")
                                                    # Las letras ya ingresadas se pasan a string y se muestran al 
                                                    #usuario
            key = 0                                 # Usamos esta variable para obtener el índice de la lista.
                                                                       

            if letra in lista:                      # El programa buscará la letra ingresada en la lista.
                for i in lista:                     # Buscará en cada una de las posiciones (i) de la lista, 
                                                    #la letra ingresada.
                    if letra == i:                  # Si la encuentra, añadirá un valor al acumulador 
                        acumulador += 1
                        palabra_adivinando.pop(key)  # Borrará el guión ubicado en la posición key (donde está la letra 
                                                     #en la palabra) de la lista de guiones
                        palabra_adivinando.insert(key, i)  # Y agregará la letra (desde la posición i de la lista) en su lugar
                        if letra in letras_ingresadas: # Si la letra ya había sido ingresada
                            key += 1                   #aumenta en uno el índice para buscar en la posición siguiente.
                            continue                   # Y continúa 
                        else:                          # Si la letra no había sido ingresada, la agrega a la lista de letras 
                                                       #ingresadas

                            letras_ingresadas.append(letra)
                    key += 1                           # Y aumenta en uno el índice para buscar en la posición siguiente.

                print(f"""       Ya encontraste {acumulador} letras de la palabra!!!
                   PALABRA: {" ".join(palabra_adivinando)}
                """)
                print(f'       Letras ya ingresadas: {" ".join(letras_ingresadas)}')
                esqueleto.figura(errores)
                print("       **************************************************************")
                                                       # Mostrará en pantalla la cantidad de letras encontradas
                                                       #y el string de la lista que se fue completando con las 
                                                       #letras acertadas ya ubicadas en su posición. Y guiones 
                                                       #en las que aún falta descubrir
            else:                                      # Si no encuentra la letra en la lista, añadirá un error
                errores += 1

                if letra in letras_ingresadas:         # Si la letra ya había sido ingresada, aunque no esté en 
                                                       #la palabra, sale del bucle
                    continue
                else:
                    letras_ingresadas.append(letra)  # Si no había sido ingresada, se agregan a la lista de ya 
                                                     #ingresadas
                print(f'       Letras ya ingresadas: {" ".join(letras_ingresadas)}') #y se imprimen
                esqueleto.figura(errores)            # Muestra el esqueleto según el número de errores
                print(f"""       La letra ingresada no está en la palabra. Cometiste {errores} error/es,
                   PALABRA: {" ".join(palabra_adivinando)}
                Vuelve a intentarlo!!!
                """)                                 #e imprime la cantidad de errores cometidos y vuelve a 
                                                     #mostrar la palabra con guiones
                print("       **************************************************************")
        elif letra == "1":                           # Si el usuario presiona "1" 
           palabra_arriesga=input("       ¿Cuál es la palabra a descubrir?: ") # El programa le pide que ingrese
                                                     #la palabra arriesgada y la convierte en una lista cuyos 
                                                     #elementos son las letras de la palabra ordenadas
           palabra_arriesga=palabra_arriesga.lower()  # Se convierten los elementos de la lista en minúsculas                        
           palabra_arriesga= " ".join(palabra_arriesga) # Convertimos la lista a string para compararla con el 
                                                        #string de la palabra a adivinar 
           if " ".join(lista) == palabra_arriesga:   # Si son iguales  
              palabra_adivinando=lista               #convertimos la lista de guiones en la lista de la palabra
                                                     #a adivinar para que el programa entienda que el usuario ganó
              print("       **************************************************************")
                                                     # Y sale del bucle  
              break
           else:                                     # Si no son iguales
            errores = 6                              #llevamos los errores al máximo para que el programa entienda
                                                     #que el usuario perdió
            if letra in letras_ingresadas:       # Si la letra ya fue ingresada, continúa
                continue
            else:                                # Si no, agrega la letra a la lista de letras ingresadas
                letras_ingresadas.append(letra)

            esqueleto.figura(errores)            # Y muestra el esqueleto según el número de errores
            print(f"""       La palabra ingresada no es la correcta!!
                             Volvé a jugar!!!
            """)
            print("       **************************************************************")
            break                                # Le avisa al usuario que la palabra es incorrecta y sale del 
                                                 #bucle
        else:                                    # Si el usuario ingresa más de una letra o ingresa un caracter
                                                 #que no sea letra
            print("       No ingresaste una letra.") # le indica al usuario que no ingresó una letra y vuelve 
                                                     #al bucle
            print("       **************************************************************")

    if lista == palabra_adivinando:  # Si la lista de la palabra a adivinar y la lista generada con las letras
                                     #que el usuario fue acertando son iguales 
        print(f'       Felicitaciones *** GANASTE *** la palabra era: {" ".join(palabra_adivinando)}')
        registro_puntos.puntaje(errores,acumulador)    
        print(f"       *** Tuvo {errores} error/es ***")
        print("       **************************************************************")
                                     # Le indica al usuario que ganó, le muestra la palabra, los puntos obtenidos
                                     #y la cantidad de errores
    else:                            #Si la lista de la palabra a adivinar y la lista generada con las letras
                                     #que el usuario fue acertando no son iguales     
        print(f"       ***PERDISTE*** la palabra era: {palabra}")
        registro_puntos.puntaje(errores, acumulador)
        print(f"       *** Tuvo {errores} error/es o no acertó la palabra***")
        print("       **************************************************************")
                                     # Le indica al usuario que perdió, le muestra la palabra, los puntos obtenidos
                                     #y la cantidad de errores
    nueva_partida = input(""" 
           --- ¿Quieres jugar de nuevo? ---
        Ingresa N para salir o cualquier carácter
                para volver a empezar.  
    """)                             # Le da la opción al usuario de jugar una nueva partida ingresando cualquier 
                                     #letra excepto "N" y convirtiéndola en una lista
    nueva_partida = nueva_partida.upper() # Convierte el elemento ingresado en mayúscula para validar si jugará 
                                     #una nueva partida. Si el nuevo elemento es cualquier caracter distinto de "N"
                                     #vuelve al while de la línea 8 para comenzar una nueva partida.

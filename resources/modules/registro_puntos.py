
def puntaje(errores, aciertos):
  match errores :
    case 0: return print("       *** Ganó, Puntaje Perfecto, 100 PUNTOS ***") # sin errores
    case 1: return print("       *** Ganó, 90 Puntos ***")    #suben errores bajan puntos
    case 2: return print("       *** Ganó, 80 Puntos ***")
    case 3: return print("       *** Ganó, 70 Puntos ***")
    case 4: return print("       *** Ganó, 60 Puntos ***")
    case 5: return print("       *** Ganó, 50 Puntos ***")
    case 6: return print(f"       *** Usted perdió, obtuvo: {5 * aciertos} Puntos ***")
                          #en este punto tenemos se completo la figura del ahorcado y obtenemos el puntaje por letra acertada.- 
    #qaciertos es la cantidad de letras adivinadas.

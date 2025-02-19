'''
Este archivo  es el punto de entrada de la aplicación, aquí se
importan las funciones de Tablero.py y se ejecutanen un ciclo while
'''
import Tablero

def main():
    ''' Funcione principal de la aplicación'''
    X = {"G":0,"P":0,"E":0}
    O = {"G":0,"P":0,"E":0}
    score = {"X":X,"O":O}
    numeros = [str(i) for i in range(1,10)]
    corriendo = True
    while corriendo:
        dsimbolos = {x:X for x in numeros}
        g = Tablero.juego(dsimbolos)
        Tablero.actauliza_score(score, g)
        Tablero.desplegar_score(score)
        seguir = input("Quieres seguir jugando? (s/n): ")
        if seguir.lower() == 'n':
            corriendo = False
if __name__ == '__main__':
    main()
'''
    Archivo princila de Linea
'''

import funciones

def main(m, b):
    X = [x/10.5 for x in range(1,101,10.5)]
    Y = [funciones.calcular_y(x,m,b) for x in x]
    print(X)
    print(Y)
    coordenadas = list(zip(X, Y))
    print(coordenadas)
    
    if __name__ == "__main__":
        main(2, 3)
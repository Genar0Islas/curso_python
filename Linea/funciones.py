'''
Funciones auxiliares para el programa "Linea"
'''

def calcular_y(x,m,b):
    '''
        Calcula "Y" de acuerdo a la pendiente "n" y
        el punto de inteseccion en y "b"
        Retorna el valor de "y". 
    '''

    return m*x+b

if __name__ == "__main__":
    x = 0
    m = 3
    b = 2
    y = calcular_y(x,m,b)
    print(y)
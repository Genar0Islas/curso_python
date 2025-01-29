'''
Funciones auxiliares para el programa "Linea"
'''
import matplotlib.pyplot as plt

def calcular_y(x:float,m:float,b:float)->float:
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

    def test_linea():
        '''
        Comprobamos calcular y
        '''

        y = calcular_y(0.0, 2.0, 3.0)
        return y
    
    if __name__ == '__main__':
        if test_linea() == 3.0:
            print('Exitoso')
        else:
            print('Test fallido')

    def grafica_linea(X: list, Y:list,m:float, b:float):
        plt.plot(X, Y)
        plt.title(f'Linea con pendiente {m} y ordenada al origen {b}')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()
if __name__ == '__main__':
    if test_linea() == 3.0:
        print('Todo bien')
    else:
        print('Todo mal')
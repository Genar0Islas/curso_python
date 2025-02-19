'''
funciones auxiliares del juego Ahorcado
'''
import string
import unicodedata
from random import choice

def carga_archivo_texto(archivo:str)->list:
    '''Carga un archivo de texto y regresa una lista con las palabras'''
    with open(archivo, 'r', encoding='utf-8') as file:
        oraciones = file.readlines()
    return oraciones


def carga_pantillas(nombre_plantilla:str)->dict:
    '''Carga una plantilla y regresa una lista con las palabras'''
    plantillas = {}
    for i in range(6):
        plantillas[i] = carga_archivo_texto(f'./plantillas/{nombre_plantilla}-{i}.txt')
    return plantillas



def despliega_plantila(diccionario:list, nivel:int):
    '''Despliega una plantilla del juego'''
    if nivel in diccionario:
        template = diccionario[nivel]
        for renglon in template:
            print(renglon)
            
def obten_palabras(lista_oraciones:list)->list:
    '''Obtiene las palabras de un texto'''
    texto = ' '.join(lista_oraciones[120:])
    palabra = texto.split()
    minusculas = [palabras.lower() for palabras in palabra]
        #convertimos a minusculas
    set_palabra = set(minusculas)
        #removemos signos de puntuacion y caracteres especiales
    set_palabra = {palabra.strip(string.punctuation) for palabra in set_palabra}
        #removemos numero, parentesis, corchetes y otros caracteres
    set_palabra = {palabra for palabra in set_palabra if palabra.isalpha()}
        #removemos acentos
    set_palabra = {unicodedata.normalize('NFKD', palabra).encode('ASCII', 'ignore').decode('ASCII') for palabra in set_palabra}
    return list(set_palabra)

def adivina_letra(abc:dict, palabra:str, letras_adivinadas:set, turnos:int)-> int:
    '''     
    Adivina una letra de una palabra
    '''
    palabra_oculta = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            palabra_oculta += letra
        else:
            palabra_oculta += "_"
    print(f'Tienes {turnos} oportunidades de fallar')
    abcd = ' '.join(abc.keys())
    print(f'El abecedario es {abcd}')
    print(f'La palabra es {palabra_oculta}')
    letra = input("Dame una letra: ")
    letra = letra.lower()
    if letra in abc:
        if abc [letra] == "*":
            print('Ya ingresaste esa letra')
        else:
            abc[letra] = "*"
            if letra in palabra:
                letras_adivinadas.add(letra)
            else:
                turnos -= 1
    return turnos

if __name__ == '__main__':
    plantillas = carga_pantillas('plantilla')
    despliega_plantila(plantillas, 5)
    lista_oraciones = carga_archivo_texto('./datos/pg15532.txt')
    lista_palabras = obten_palabras(lista_oraciones)
    print(len(lista_palabras))
    p = choice(lista_palabras)
    print(p)
    abcdario = {letra:letra for letra in string.ascii_lowercase}
    adivinadas = set()
    t = 5 # oportunidades
    t = adivina_letra(abcdario, p, adivinadas, t)
    print(t)
    t = adivina_letra(abcdario, p, adivinadas, t)
    print(t)
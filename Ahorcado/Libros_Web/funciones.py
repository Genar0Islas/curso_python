''' Archivo con las funciones necesarias de la Apliación Libro Web'''
import csv

def lee_archivo_csv(archivo:str) ->list:
    '''Lee un archivo CSV y la convierte en una lista de diccionarios'''
    with open(archivo, "r", encoding="utf-8") as f:
        return list(x for x in csv.DictReader(f))
    
def crea_diccionario(lista:list, llaves:str)->dict:
    '''Crea un diccionario con los valores de una llave como llaves'''
    return {x[llaves].lower():x for x in lista}

def busca_diccionario(diccionario:dict, palabra:str)->list:
    '''Busca una palabra en el diccionario y devuelve una lista con los valores que la contienen'''
    lista = []
    palabra = palabra.lower()
    for llave, libro in diccionario.items():
        if palabra in llave.lower():
            lista.append(libro)
    return lista

def libro_empiesa_por(lista:list, letra:str)->dict:
    '''Busca los libros que empiezan con una letra'''
    return [x for x in lista if x["title"].lower().startswith(letra.lower())]

    
    

if __name__ == "__main__":
    archivo_csv = "booklist2000.csv"
    lista_libros = lee_archivo_csv(archivo_csv)
    diccionario_libros = crea_diccionario(lista_libros, "title")
    resultado = busca_diccionario(diccionario_libros, "rebels")
    print(resultado)
    diccionario_autores = crea_diccionario(lista_libros, "author")
    resultado = busca_diccionario(diccionario_autores, "Sandra")
    print(resultado)
    resultado = libro_empiesa_por(lista_libros, "a")
    print(f"Libros empiezan con la letra 'a': {len(resultado)}")
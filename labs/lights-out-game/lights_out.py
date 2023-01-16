# -*- coding: utf-8 -*-
import random


def construir_tablero(casillas: int)-> list:
    """ Construye un nuevo tablero de casillas x casillas,
        donde cada casilla está prendida o apagada aleatoriamente
    Parámetros:
        casillas (int) : el ancho y alto del tablero
    Retorno:
        (list) : una matriz (lista de listas) con valores booleanos
    """
    tablero = []
    for f in range(casillas):
        fila = []
        for c in range(casillas):
            fila.append(random.random() >= 0.5)
        tablero.append(fila)
    return tablero

def cargar_tablero(nombre_archivo: str) -> list:
    """ Carga un tablero inicial del archivo indicado
    Parámetros:
        nombre_archivo (str): El nombre del archivo que se va a cargar
    Retorno:
        (list) : El tablero de juego que se cargó del archivo
    """
    archivo = open(nombre_archivo, "r")
    lineas = archivo.readlines()
    archivo.close()
    tablero = []
    casillas = len(lineas[0].strip())
    for f in range(casillas):
        fila = []
        for casilla in lineas[f].strip():
            fila.append('*' == casilla)
        tablero.append(fila)
    return tablero


def contar_iluminadas_en_filas(tablero: list) -> list:
    """ Cuenta cuántas casillas hay iluminadas en cada fila del tablero
        y retorna una lista con las cantidades respectivas.
    Parámetros:
        tablero (list): el tablero representado como una matriz de valores booleanos
    Retorno:
        (list) : una lista que tiene tantos enteros como filas hay en el tablero;
                 cada entero en la lista indica la cantidad de casillas iluminadas en la fila correspondiente
    """
    filas = len(tablero)
    columnas = len(tablero[0])
    casillas = []
    for i in range(columnas):
        iluminadas = 0
        for j in range(filas):
            if tablero[i][j] == True:
               iluminadas += 1
        casillas.append(iluminadas)       
    return casillas


def contar_iluminadas_en_columnas(tablero: list) -> list:
    """ Cuenta cuántas casillas hay iluminadas en cada columna del tablero
        y retorna una lista con las cantidades respectivas.
    Parámetros:
        tablero (list): el tablero representado como una matriz de valores booleanos
    Retorno:
        (list) : una lista que tiene tantos enteros como columnas hay en el tablero;
                 cada entero en la lista indica la cantidad de casillas iluminadas en la columna correspondiente
    """

    filas = len(tablero)
    columnas = len(tablero[0])
    casillas = []
    for j in range(filas):
        iluminadas = 0
        for i in range(columnas):
            if tablero[i][j] == True:
               iluminadas += 1
        casillas.append(iluminadas)       
    return casillas


def jugar(tablero: list, fila: int, columna: int) -> None:
    """ Realiza una jugada en la posición indicada con los parámetros fila y columna.
        Al hacer una jugada, tanto la posición indicada como hasta sus 8 vecinos cambian de estado:
            Si estaban prendidos se apagan
            Si estaban apagados se prenden
        La función no debe retornar nada pero debe cambiar el estado de tablero
    Parámetros:
        tablero (list): el tablero representado como una matriz de valores booleanos
        fila (int): la fila donde está la casilla en la que se va a jugar
        columna (int): la columna donde está la casilla en la que se va a jugar
    """
    for df in range(-1,2):
        if fila + df >= 0 and fila + df < len(tablero):
           for dc in range(-1,2):
               if columna + dc >= 0 and columna + dc < len(tablero[0]):
                  tablero[fila + df][columna + dc] = not(tablero[fila + df][columna + dc])  

def revisar_final(tablero: list) -> bool:
    """ Revisa si con el estado actual del tablero el juego terminó.
    Parámetros:
        tablero (list): el tablero representado como una matriz de valores booleanos
    Retorno:
        (bool): Retorna True si todas las casillas del tablero están encendidas
    """
    filas = len(tablero)
    columnas = len(tablero[0])
    termino = True
    i = 0
    while i < filas and termino == True:  
        j = 0
        while j < columnas and termino == True:
           if tablero[i][j] == False:
              termino = False 
           j += 1   
        i += 1   
    return termino

def recorrer_matriz(matriz: list)-> None:
    filas = len(matriz)
    columnas = len(matriz[0])
    i = 0
    while i < filas:
        j = 0
        while j < columnas:
           print(matriz[i][j])
           j += 1   
        i += 1   
        
        
tablero = cargar_tablero("tablero.lights")

matriz = [[3, 3, 4], [1, 3, 3], [5, 3, 3]]




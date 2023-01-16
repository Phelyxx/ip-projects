# -*- coding: utf-8 -*-
"""
Ejemplo Nivel 4: Visor de imágenes

Temas:

* Matrices

@author: Cupi2
"""
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


def cargar_imagen(ruta_imagen: str)-> list:
    """ Carga la imagen que se encuentra en la ruta dada.
    Parámetros:
        ruta_imagen (str) Ruta donde se encuentra la imagen a cargar.
    Retorno:
        list: Matriz de MxN con tuplas (R,G,B).
    """
    matriz = mpimg.imread(ruta_imagen).tolist()
    alto = len(matriz)
    ancho = len(matriz[0])
    imagen = []
    for i in range(alto):
        fila = []
        for j in range(ancho):
            r = matriz[i][j][0]
            g = matriz[i][j][1]
            b = matriz[i][j][2]
            tupla = (r, g, b)
            fila.append(tupla)
        imagen.append(fila)
    return imagen


def visualizar_imagen(imagen: list) -> None:
    """ Muestra la imagen recibida
    Parámetros:
        imagen (list): Matriz de MxN con tuplas (R,G,B) que representan la imagen a visualizar.
    """
    alto = len(imagen)
    ancho = len(imagen[0])
    matriz = []
    for i in range(alto):
        fila = []
        for j in range(ancho):
            r, g, b = imagen[i][j]
            fila.append([r, g, b])
        matriz.append(fila)
    plt.imshow(matriz)
    plt.show()


def convertir_negativo(imagen: list) -> list:
    """  Convierte la imagen en negativo.
    El negativo se calcula cambiando cada componente RGB, tomando el valor absoluto de restarle al componente 1.0.
    Parámetros:
        imagen (list) Matriz de MxN con tuplas (R,G,B) que representan la imagen a convertir a negativo.
    """
    alto = len(imagen)
    ancho = len(imagen[0])

    for i in range(alto):
        for j in range(ancho):
            r, g, b = imagen[i][j]
            nuevo = (abs(r-1), abs(g-1), abs(b-1))
            imagen[i][j] = nuevo
    return imagen


def reflejar_imagen(imagen: list)->list:
    """Refleja la imagen.
    Consiste en intercambiar las columnas enteras de la imagen, de las finales a la iniciales.
    Parámetros:
        imagen (list) Matriz de MxN con tuplas (R,G,B) que representan la imagen a reflejar.
    """
    alto = len(imagen)
    ancho = len(imagen[0])
    for i in range(alto):
        nuevo = []
        for j in range(ancho-1,-1,-1):
            nuevo.append(imagen[i][j])
        imagen[i] = nuevo           
    return imagen


def binarizar_imagen(imagen: list, umbral: float)->list:
    """ Binariza la imagen.
    Consiste en llevar cada pixel de una imagen a negro o blanco.
    Para ello se requiere un umbral: si el promedio de los componentes RGB del pixel está por encima o igual se lleva a blanco y si está por debajo se lleva a negro.
    Parámetros:
        imagen (list) Matriz de MxN con tuplas (R,G,B) que representan la imagen a binarizar.
        umbral (float) Umbral de la binarización.
     """
    alto = len(imagen)
    ancho = len(imagen[0])

    for i in range(alto):
        for j in range(ancho):
            r, g, b = imagen[i][j]
            promedio = (r + g + b) / 3
            if promedio >= umbral:                   
               nuevo = (1.0, 1.0, 1.0)
            elif promedio < umbral:
               nuevo = (0, 0, 0) 
            imagen[i][j] = nuevo
    return imagen 


def convertir_a_grises(imagen: list)->list:
    """ Convierte la imagen a escala de grises.
    Para ello promedia los componentes de cada pixel y crea un nuevo color donde cada componente (RGB) tiene el valor de dicho promedio.
    Parámetros:
        imagen (list) Matriz de MxN con tuplas (R,G,B) que representan la imagen a convertir a grises.
    """
    alto = len(imagen)
    ancho = len(imagen[0])

    for i in range(alto):
        for j in range(ancho):
            r, g, b = imagen[i][j]
            promedio = (r + g + b) / 3              
            nuevo = (promedio, promedio, promedio)
            imagen[i][j] = nuevo
    return imagen 



def suma_individual(imagen:list, alto:int, ancho:int, convolucion:list)->int:
    rojo = 0
    verde = 0
    azul = 0
    totales = 0
    for dal in range(-1, 2):
        if alto + dal > 0 and alto + dal < len(imagen):
            for dan in range(-1, 2):
                if ancho + dan > 0 and ancho + dan < len(imagen[0]):
                    r,g,b = imagen[alto + (dal)][ancho + (dan)]
                    rojo += (r*convolucion[dal+1][dan+1])
                    verde += (g*convolucion[dal+1][dan+1])
                    azul += (b*convolucion[dal+1][dan+1])
                    totales += convolucion[dal+1][dan+1]
    if totales != 0:
        nuevor = rojo/totales
        nuevog = verde/totales
        nuevob = azul/totales
        nuevo = (nuevor,nuevog,nuevob)
        print(nuevo)
        return nuevo
    
def convolucion_imagen(imagen: list, convolucion:list)->list:
    alto = len(imagen)
    ancho = len(imagen[0])
    for i in range(0, alto):
        for j in range(0, ancho):
            r, g, b = imagen[i][j]
            nuevo = suma_individual(imagen,i,j,convolucion)
            imagen[i][j] = nuevo
    return imagen
random = [(0.7,0.2,0.3)]



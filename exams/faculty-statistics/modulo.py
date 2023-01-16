# -*- coding: utf-8 -*-
"""
Ejercicio nivel 4: Boletin Estadistico
Esqueleto del examen
"""


def cargar_matriz_estadisticas(ruta_archivo: str)->list:
    """
    Esta funcion carga la informacion de la matriz de estadisticas
    de las facultades a partir de un archivo CSV.
        ruta_archivo (str): la ruta del archivo que se quiere cargar
    Retorno: list
        La matriz con las estadisticas por facultad
    """
    archivo = open(ruta_archivo)
    linea = archivo.readline()
    facultades = 11
    elementos = 9
    estadisticas = []
    for i in range(0, facultades+1):
        estadisticas.append([0]*(elementos+1))

    i = 0
    while len(linea) > 0:
        datos = linea.split(",")
        for j in range(0, elementos+1):
            estadisticas[i][j] = datos[j].strip()
        i += 1
        linea = archivo.readline()
    archivo.close()

    return estadisticas


def cargar_matriz_puestos(ruta_archivo: str) -> list:
    """
    Esta funcion carga la informacion de la matriz de puestos estudiante
    a partir de un archivo CSV.
        ruta_archivo (str): la ruta del archivo que se quiere cargar
    Retorno: list
        La matriz con los puestos estudiante de cada facultad
    """
    archivo1 = open(ruta_archivo)
    linea = archivo1.readline()
    oferentes = 11
    ocupantes = 12
    puestos = []
    for i in range(0, oferentes+1):
        puestos.append([0] * (ocupantes+1))

    i = 0
    while len(linea) > 0:
        datos = linea.split(",")
        for j in range(0, ocupantes+1):
            puestos[i][j] = datos[j].strip()
        i += 1
        linea = archivo1.readline()
    archivo1.close()

    return puestos


def cargar_matriz_dobles(ruta_archivo: str) -> list:
    """
    Esta funcion carga la informacion de la matriz de dobles programas
    a partir de un archivo CSV.
        ruta_archivo (str): la ruta del archivo que se quiere cargar
    Retorno: list
        La matriz con los dobles programas
    """
    archivo1 = open(ruta_archivo)
    linea = archivo1.readline()
    dobles = []
    i = 0

    while len(linea) > 0:
        nueva_linea = []
        datos = linea.split(",")
        for j in range(0, len(datos)):
            nueva_linea.append(datos[j].strip())
        dobles.append(nueva_linea)
        i += 1
        linea = archivo1.readline()
    archivo1.close()

    return dobles

def contar_profesores(estadisticas:list, facultad:str)->int:
    i = 1
    encontre = False
    suma = 0
    while i < len(estadisticas) and encontre == False:
        if estadisticas[i][0] == facultad:
           suma += int(estadisticas[i][1])
           suma += int(estadisticas[i][2])           
           encontre = True
        i += 1 
    return suma    

def calcular_puestos_por_profesor(estadisticas:list, puestos: list)->list:
    facultades = []
    i = 0
    j = 0
    for i in range(0, 1):
        for j in range(1, len(puestos[0])):
            facultades.append(puestos[i][j])
            j += 1
        i += 1    
    puestos_profesor = [facultades]  
    for facultad in facultades:
        i = 0
        j = 0
        encontre = False
        while i < 1 and encontre == False:
            while j < len(puestos[0]):
                if puestos[i][j] == facultad:
                   num_facultad = j
                   encontre = True
                j += 1
            i += 1
        lista = [facultad]    
        for i in range(1, len(puestos)):
            atiende = int(puestos[i][num_facultad])
            profes = contar_profesores(estadisticas,puestos[i][0])
            if profes != 0:
               promedio = atiende / profes
            else:
               promedio = 0
            lista.append(round(promedio,3))
        puestos_profesor.append(lista)
    return puestos_profesor

estadisticas = cargar_matriz_estadisticas("estadisticas_facultades.csv")
puestos = cargar_matriz_puestos("matriz_puestos.csv")
resultado = calcular_puestos_por_profesor(estadisticas, puestos)

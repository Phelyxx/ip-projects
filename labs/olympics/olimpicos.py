# -*- coding: utf-8 -*-
"""
Created on Tue May  5 18:56:53 2020

@author: usuario
"""
# Función 1 -
def cargar_atletas(nombre_archivo: str)->list:
    archivo = open(nombre_archivo, "r")
    datos = archivo.readlines()
    archivo.close()
    notas = []
    for i in range(1, len(datos)):
        registro = datos[i]
        columnas = registro.split(",")
        nombre = columnas[0]
        genero = columnas[1].strip()
        edad = int(columnas[2].strip())
        pais = columnas[3].strip()
        anio = int(columnas[4].strip())
        evento = columnas[5].strip()
        medalla = columnas[6].strip()
        d = crear_diccionario_atletas(nombre, genero, edad, pais, anio, evento, medalla)
        notas.append(d)
    return notas    

def crear_diccionario_atletas(nombre: str, genero: str, edad: int, pais: str, anio: int, evento: str, medalla: str)->dict:
    diccionario = {}
    diccionario["nombre"] = nombre
    diccionario["genero"] = genero
    diccionario["edad"] = edad
    diccionario["pais"] = pais
    diccionario["anio"] = anio
    diccionario["evento"] = evento
    diccionario["medalla"] = medalla

    return diccionario
# Función 2 -
def atletas_por_anio(atletas: list, anio: str)->dict:
    dicc = {}
    lista_eventos = []
    for atleta in atletas:
        if anio == atleta["anio"] and atleta["evento"] not in lista_eventos:
           lista_eventos.append(atleta["evento"])
           dicc[atleta["evento"]] = [atleta["nombre"]]
        elif anio == atleta["anio"] and atleta["evento"] in lista_eventos:
           dicc[atleta["evento"]] += [atleta["nombre"]] 
    return dicc       
# Función 3 -
def medallas_en_rango(atletas: list, anio_inicio: int, anio_final: int, nombre: str)->list:
    lista = []
    for atleta in atletas:
        if atleta["anio"] in range(anio_inicio, anio_final + 1) and atleta["nombre"] == nombre:
           dicc = {"evento":atleta["evento"], "anio":atleta["anio"], "medalla":atleta["medalla"] } 
           lista.append(dicc)  
    return lista     
# Función 4 -
def atletas_por_pais(atletas: list, pais: str)->list:
    lista = []
    for atleta in atletas:
        if atleta["pais"].lower() == pais.lower():
           dicc = {"nombre":atleta["nombre"], "evento":atleta["evento"], "anio":atleta["anio"]} 
           lista.append(dicc)
    return lista       
# Función 5 -
def pais_con_mas_atletas(atletas:list)->dict:
    dicc = {}
    lista_paises = []
    mejor = ""
    mayor = 0
    for atleta in atletas:
        if atleta["pais"] not in lista_paises and atleta["medalla"] != "na":
           lista_paises.append(atleta["pais"])     
    for pais in lista_paises:
        medallas = 0
        for atleta in atletas:
            if atleta["pais"] == pais and atleta["medalla"] != "na":
               medallas += 1
        if medallas > mayor:
           mayor = medallas
           mejor = pais
    dicc[mejor] = mayor  
    return dicc
# Función 6 -
def medallistas_por_evento(atletas:list, evento: str)->list:
    lista = []
    for atleta in atletas:
        if atleta["medalla"] != "na" and atleta["evento"] == evento and atleta["nombre"] not in lista:
           lista.append(atleta["nombre"]) 
    return lista
## Función 7 -
def atletas_con_mas_medallas_que(atletas:list, mas_medallas: int)->dict:
    dicc = {}
    lista = []
    for atleta in atletas:
        if atleta["medalla"] != "na":
           lista.append(atleta["nombre"])
    for ganador in lista:
        medallas = 0
        for atleta in atletas:
            if atleta["nombre"] == ganador and atleta["medalla"] != "na":
               medallas += 1
        if medallas > mas_medallas and atleta["nombre"] not in dicc:
           dicc[ganador] = medallas
    return dicc      
## Función 8 - 
def atleta_estrella(atletas:list)->dict:
    campeones = {}
    dicc_medallas = {}
    for atleta in atletas:
        nombre = atleta["nombre"]
        if atleta["medalla"] != "na" and atleta["nombre"] not in dicc_medallas:
            dicc_medallas[nombre] = 1
        elif atleta["medalla"] != "na" and atleta["nombre"] in dicc_medallas:
            cantidad = dicc_medallas[nombre] + 1
            dicc_medallas[atleta["nombre"]] = cantidad
    medallas = 0
    for medallista in dicc_medallas:
        if dicc_medallas[medallista] > medallas: medallas = dicc_medallas[medallista]
    for medallista in dicc_medallas:
        if dicc_medallas[medallista] >= medallas: campeones[medallista] = dicc_medallas[medallista]
    return campeones
## Función 9 -
def mejor_pais_en_un_evento(atletas:list, evento: str)->dict:
    lista_paises = []
    mayor_oro = 0
    mayor_bronce = 0
    mayor_plata = 0
    for atleta in atletas:
        if atleta["pais"] not in lista_paises and atleta["medalla"] != "na" and atleta["evento"] == evento:
           lista_paises.append(atleta["pais"])     
    for pais in lista_paises:
        medallas_oro = 0
        medallas_plata = 0
        medallas_bronce = 0
        for atleta in atletas:
            if atleta["pais"] == pais and atleta["evento"] == evento:
               if atleta["medalla"] == "gold" :
                  medallas_oro += 1
               elif atleta["medalla"] == "silver":
                  medallas_plata += 1
               elif atleta["medalla"] == "bronze":
                  medallas_bronce += 1
        if medallas_oro > mayor_oro:
           mayor_oro = medallas_oro  
           mayor_plata = medallas_plata
           mayor_bronce = medallas_bronce
           dicc = {pais: [medallas_oro, medallas_plata, medallas_bronce]}   
        elif medallas_oro == mayor_oro and medallas_plata > mayor_plata:
           mayor_plata = medallas_plata
           mayor_bronce = medallas_bronce
           dicc = {pais: [medallas_oro, medallas_plata, medallas_bronce]}
        elif medallas_oro == mayor_oro and medallas_plata == mayor_plata and medallas_bronce > mayor_bronce:
           mayor_bronce = medallas_bronce
           dicc = {pais: [medallas_oro, medallas_plata, medallas_bronce]}     
    return dicc
## Función 10 -
def todoterreno(atletas:list)->str:
    lista = []
    mayor = 0
    for atleta in atletas:
        if atleta["evento"] not in lista:
           lista.append(atleta["nombre"])
    for participante in lista:
        participaciones = 0
        for atleta in atletas:
            if atleta["nombre"] == participante:
               participaciones += 1
        if participaciones > mayor:
           mayor = participaciones
           mejor = participante                
    return mejor
## Función 11 -
def medallistas_por_nacion_y_genero(atletas:list, pais: str, genero: str)->dict:
    resultado = {}
    for atleta in atletas:
        dicc = {}
        info_medallistas = []
        if atleta["pais"] == pais and atleta["genero"] == genero and atleta["medalla"] != "na" and atleta["nombre"] not in resultado:
           dicc["evento"] = atleta["evento"]
           dicc["anio"] = atleta["anio"]
           dicc["medalla"] = atleta["medalla"]
           info_medallistas.append(dicc)
           resultado[atleta["nombre"]] = info_medallistas  
        elif atleta["pais"] == pais and atleta["genero"] == genero and atleta["medalla"] != "na" and atleta["nombre"] in resultado:   
           dicc["evento"] = atleta["evento"]
           dicc["anio"] = atleta["anio"]
           dicc["medalla"] = atleta["medalla"]
           info_medallistas.append(dicc)
           resultado[atleta["nombre"]] += info_medallistas  
    return resultado        
## Función 12 -
def porcentaje_medallistas(atletas: list)->float:
    campeones = []
    perdedores = []
    ganadores = 0
    jugadores = 0
    for atleta in atletas:
        if atleta["medalla"] != "na" and atleta["nombre"] not in campeones and atleta["nombre"] not in perdedores:
           campeones.append(atleta["nombre"]) 
        elif atleta["medalla"] != "na" and atleta["nombre"] not in campeones and atleta["nombre"] in perdedores: 
            perdedores.remove[atleta["nombre"]]
    for atleta in atletas:
        if atleta["medalla"] == "na" and atleta["nombre"] not in campeones and atleta["nombre"] not in perdedores:
           perdedores.append(atleta["nombre"]) 
    for campeon in campeones:
        ganadores += 1
    for perdedor in perdedores:
        jugadores += 1
    porcentaje = ganadores / jugadores
    return round(porcentaje, 2)         

        
    
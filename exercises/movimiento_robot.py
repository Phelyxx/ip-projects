# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 21:13:34 2020

@author: usuario
"""

def movimiento_robot(orientacion_actual: str, giro: str)->str:
    """ Movimiento robótico
    Parámetros:
      orientacion_actual (str): La orientación actual del robot
      giro (str): La acción a ejecutar a partir de la orientación inicial del robot. Debe ser un valor de
                  los siguientes: {"L","H","R","."}
    Retorno:
      str: La orientación final del robot, debe ser un valor de los siguientes:  {"W","N","S","D"}
    """
    pass
    if giro == "L" :
        if orientacion_actual == "S":    
           or_final = "E"
        if orientacion_actual == "N":
           or_final = "W"
        if orientacion_actual == "W":
           or_final = "S"
        if orientacion_actual == "E":
           or_final = "N"   
    if giro == "R":
       if orientacion_actual == "S":
         or_final = "W"
       if orientacion_actual == "N":
         or_final = "E"
       if orientacion_actual == "W":
         or_final = "N"
       if orientacion_actual == "E":
          or_final = "S"
    if giro == "H":
        if orientacion_actual == "S": or_final = "N"
        if orientacion_actual == "N": or_final = "S"
        if orientacion_actual == "W": or_final = "E"
        if orientacion_actual == "E": or_final = "W"
    if giro == ".":
       or_final = orientacion_actual 
        
                
          
    return or_final      
        
        
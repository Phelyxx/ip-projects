# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 14:07:54 2020

@author: fs.rojas
"""

import calculadora_modelos as calc

def ejecutar_distribucion_masa()->None:
    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en metros: "))
    edad = float(input("Edad en años: "))
    constante_genero = float(input("Ingrese el valor 10.8 en caso de ser hombre y 0 en caso de ser mujer: "))
    diametro_bi_munieca = float(input("Diámetro muñeca en metros: "))
    diametro_bi_femur = float(input("Diámetro fémur en metros: "))
    constante_residual= float(input("Ingrese el valor 0.241 en caso de ser hombre y 0 en caso de ser mujer: "))
                                   
    masa_grasa = round(calc.calcular_masa_grasa(peso, altura, edad, constante_genero), 2)
    masa_osea = round(calc.calcular_masa_osea(altura,diametro_bi_munieca,diametro_bi_femur), 2)
    masa_residual = round(calc.calcular_masa_residual(peso,constante_residual), 2)
    masa_muscular = round(calc.calcular_masa_muscular(peso,altura,edad,diametro_bi_munieca,
                         diametro_bi_femur, constante_genero, constante_residual), 2)
    masa_grasa1 = "Masa grasa " + str(masa_grasa)
    masa_osea1 = "Masa osea " + str(masa_osea)
    masa_residual1 = "Masa residual " + str(masa_residual)
    masa_muscular1 = "Masa muscular " + str(masa_muscular) 
    print (masa_grasa1, masa_osea1,masa_residual1, masa_muscular1)
    
def iniciar_aplicacion()->None:
    ejecutar_distribucion_masa()

iniciar_aplicacion()    

round(3.87762)
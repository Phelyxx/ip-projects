# -*- coding: utf-8 -*-
"""
Examen Nivel 1: Modelos de masa corporales
"""

# ------------------------------------------------------
# Funciones
# ------------------------------------------------------


def calcular_IMC(peso: float, altura: float)->float:
    """ Calcula el índice de masa corporal de una persona a partir de la 
        información recibida.
    Parámetros:
        peso (float) peso de la persona, en kilogramos.
        altura (float) altura de la persona, en metros.
    Retorna:
        float: El índice de masa corporal de la persona en kg/m^2.
    """
    imc = peso/((altura)**2)
    return imc


def calcular_porcentaje_grasa(peso: float, altura: float, edad: int, constante_genero: float)->float:
    """ Calcula el porcentaje de grasa de una persona.
    Parámetros:
        peso (float) peso de la persona, en kilogramos.
        altura (float) altura de la persona, en metros.
        edad (int) edad de la persona, en años.
        constante_genero (float) constante que toma valor según el género de la
            persona. En caso de ser masculino toma el valor de 10.8 y en caso de ser
            femenino toma el valor de 0.
    Retorna:
        float: El porcentaje de grasa de la persona. Es un número entre 0 y 1.
    """
    porcentaje_gc = ((1.2*calcular_IMC(peso,altura))+(0.23*edad)-5.4-constante_genero) /100
    return porcentaje_gc


def calcular_masa_residual(peso: float, constante_residual: float)->float:
    """ Calcula la masa residual, es decir, la masa compuesta por los organos, aparatos y diferentes 
    componentes corporales.
    Parámetros:
        peso (float) peso de la persona, en kilogramos.
        constante_genero (float) constante que toma valor según el género de la
            persona. En caso de ser masculino toma el valor de 0.241 y en caso de ser
            femenino toma el valor de 0.209.
    Retorna:
        float: La cantidad de masa residual, en kilogramos.
    """
    mr = peso*constante_residual
    return mr




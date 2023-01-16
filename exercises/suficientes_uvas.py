# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 14:30:22 2020

@author: usuario
"""

def suficientes_uvas(cantidad_ivan: int, cantidad_nicolas: int, cantidad_adriana: int, cantidad_verde: int, cantidad_morada: int, cantidad_negra: int)->str:
    """ ¿Suficientes Uvas?
    Parámetros:
      cantidad_ivan (int): La cantidad de uvas que Iván desea comer
      cantidad_nicolas (int): La cantidad de uvas que Nicolás desea comer
      cantidad_adriana (int): La cantidad de uvas que Adriana desea comer
      cantidad_verde (int): La cantidad de uvas verdes de las que disponen los amigos
      cantidad_morada (int): La cantidad de uvas moradas de las que disponen los amigos
      cantidad_negra (int): La cantidad de uvas negras de las que disponen los amigos
    Retorno:
      str: La función retorna "felices", si todos los amigos pueden comer la cantidad de uvas que quieren;
           "casi", si dos de los 3 amigos pueden comer la cantidad de uvas que quieren; "fallamos", si
           solamente 1 amigo puede comer la cantidad de uvas que quiere; "al menos somos amigos", si ninguno de
           los amigos puede comer la cantidad de uvas que quiere.
    """
    cantidad = 0
    cantidad_total = cantidad_verde + cantidad_morada + cantidad_negra
    verdes = cantidad_verde
    if cantidad_verde - cantidad_ivan >= 0:
        verdes = cantidad_verde - cantidad_ivan
        cantidad_total = cantidad_verde + cantidad_morada + cantidad_negra - cantidad_ivan
        cantidad += 1
    else:
        cantidad_total = cantidad_verde + cantidad_morada + cantidad_negra
        
    if (verdes + cantidad_morada) - cantidad_nicolas >= 0:
        cantidad_total = ((verdes + cantidad_morada) - cantidad_nicolas)  + cantidad_negra
        cantidad += 1
    else:
        cantidad_total = verdes + cantidad_morada + cantidad_negra
        
    if cantidad_total - cantidad_adriana >= 0:
        cantidad += 1
    if cantidad_ivan >= cantidad_nicolas + cantidad_adriana and cantidad_morada < cantidad_nicolas and cantidad_negra < cantidad_adriana:
       cantidad += 1 
    if cantidad ==3:
        resultado = "felices"
    elif cantidad == 2:
        resultado = "casi"
    elif cantidad == 1:
        resultado = "fallamos"
    else:
        resultado = "al menos somos amigos"
        
    return resultado
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 11:23:30 2020

@author: usuario
"""

def calcular_costo_boletas(cantidad_boletas: int, tipo_sala: str, hora_pico: bool, pago_tarjeta_cinema: bool, reserva: bool)->int:
    """ Boletas de Cine
    Parámetros:
      cantidad_boletas (int): La cantidad de boletas que se van a comprar
      tipo_sala (str): El tipo de sala en que se proyecta la película. Puede ser '2D', '3D' o 'Dinamix'
      hora_pico (bool): Indica si el horario en que se proyecta la película es una hora pico o no
      pago_tarjeta_cinema (bool): Indica si el pago de las boletas se hará con la tarjeta del cinema
      reserva (bool): Indica si se van a reservar las boletas antes de comprarlas
    Retorno:
      int: El costo total de las boletas, redondeado al número entero más cercano.
    """
    pass
    descuento = 0
    desc = 0
    desc_cinema = 0
    recargo = 0
    incremento = 0
    if tipo_sala == "2D":
       coste = cantidad_boletas * 11300
       if hora_pico == True:
          incremento = coste * 0.25
    if tipo_sala == "3D":
       coste = cantidad_boletas * 15500
       if hora_pico == True:
          incremento = coste * 0.25       
    if tipo_sala == "Dinamix":
       coste = cantidad_boletas * 18800
       if hora_pico == True:
          incremento = coste * 0.5      
    if hora_pico == False:
       descuento = coste * 0.10
       if cantidad_boletas >= 3:
          desc = cantidad_boletas * 500          
    if pago_tarjeta_cinema == True:
       desc_cinema = coste * 0.05
    if reserva == True:
       recargo = cantidad_boletas * 2000
    res = coste - descuento - desc_cinema + recargo + incremento - desc
    return res   
     
       
           
       
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 11:43:35 2020

@author: usuario
"""def altura_en_mts(pies: int, pulgadas: int)->float:
    """ Altura de una persona
    Parámetros:
      pies (int): Número de pies que componen la altura de la persona
      pulgadas (int): Número de pulgadas que componen la altura de la persona
    Retorno:
      float: Altura en metros de la persona, la cual debe estar redondeada a dos cifras decimales.
    """
    pass
    pies_pulg = pies * 12
    pulg_cm = (pies_pulg + pulgadas) * 2.54
    res = pulg_cm / 100
    return round(res, 2)
        


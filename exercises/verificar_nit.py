# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 16:02:14 2020

@author: usuario
"""
def verificar_nit(NIT: int, digito: int)->bool:
    """ Verificar NIT
    Parámetros:
      NIT (int): NIT de una empresa, sin dígito de verificación
      digito (int): Dígito de verificación
    Retorno:
      bool: Retorna True si el dígito de verificación era correcto y False de lo contrario
    """
    pass
    digito1 = (NIT // 100000000) % 10
    digito2 = (NIT // 10000000) % 10
    digito3 = (NIT // 1000000) % 10
    digito4 = (NIT // 100000) % 10
    digito5 = (NIT // 10000) % 10
    digito6 = (NIT // 1000) % 10
    digito7 = (NIT // 100) % 10
    digito8 = (NIT // 10) % 10
    digito9 = NIT % 10
    multi1 = digito1 * 41
    multi2 = digito2 * 37
    multi3 = digito3 * 29
    multi4 = digito4 * 23
    multi5 = digito5 * 19
    multi6 = digito6 * 17
    multi7 = digito7 * 13
    multi8 = digito8 * 7
    multi9 = digito9 * 3
    suma = multi1+multi2+multi3+multi4+multi5+multi6+multi7+multi8+multi9
    calc = suma % 11
    if calc == 1 and calc == digito:
       res = True   
    elif calc == 0 and calc == digito:
       res = True
    elif 11 - calc == digito:
        res = True
    else: res = False
    return res


    
    
        
    

# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 19:17:10 2020

@author: usuario
"""

def calcular_IMC(peso:float,altura:float) ->float:  
    
    """ Calcula el indice de masa corporal en base
    al peso y a la altura.
    Parámetros:
        peso(float) Peso de la persona en kilogramos.
        altura(float) Altura de la persona en metros.
    Retorno:
        float: El índice de masa corporal de la persona. 
    """    
    # Las siguientes instrucciones permiten calcular
    # el IMC, siendo este la razón entre el peso en
    # kilogramos y el cuadrado de la altura en metros
    # de la persona:
    imc = peso / (altura ** 2)
    return imc
    
def calcular_porcentaje_grasa(peso: float,altura: 
    float,edad:int,valor_genero:float) ->float:                           
    imc = calcular_IMC (peso,altura)
    
    """ Calcula el porcentaje de grasa de una
    persona a partir de la ecuación definida
    anteriormente.
    Parámetros:
        peso(float) Peso de la persona en kilogramos.
        altura(float) Altura de la persona en metros.
        edad (int) Edad de la persona en años.
        valor_genero(float) Valor que varía según el
        género de la persona: en caso de ser masculino
        debe ser 10.8 y en caso de ser femenino debe
        ser 0.
    Retorno:
        float: El porcentaje de grasa que tiene el
        cuerpo de la persona. 
    """    
    # Las siguientes instrucciones permiten calcular
    # el porcentaje de grasa con los datos del usuario
    gc = 1.2 * imc + 0.23 * edad - 5.4 - valor_genero
    return gc
    
def calcular_calorias_en_reposo(peso:float, altura:float,
    edad:int, valor_genero:float) ->float:
    
    """ Calcula la cantidad de calorías que una 
    persona quema estando en reposo (esto es, su tasa
    metabólica basal), a partir de la ecuación 
    definida anteriormente.
    Parámetros:
        peso(float) Peso de la persona en kilogramos.
        altura(float) Altura de la persona en centímetros.
        edad (int) Edad de la persona en años.
        valor_genero(float) Valor que varía según el 
        género de la persona: en caso de ser masculino
        debe ser 5 y en caso de ser femenino debe ser
        -161.
    Retorno:
        float: La cantidad de calorías que la persona
        quema en reposo. 
    """    
    # Las siguientes instrucciones permiten calcular
    # la tasa metabólica basal con los datos del usuario
    tmb = (10 * peso) + (6.25 * altura) - (5 * edad) \
    + valor_genero
    return tmb

def calcular_calorias_en_actividad(peso:float, altura:float,
    edad:int, valor_genero: float, valor_actividad:float)\
    -> float:
    """ Calcula la cantidad de calorías que una 
    persona quema al realizar algún tipo de actividad
    física (esto es, su tasa metabólica basal según
    actividad física), a partir de la ecuación 
    definida anteriormente.
    Parámetros:
        peso(float) Peso de la persona en kilogramos.
        altura(float) Altura de la persona en centímetros.
        edad (int) Edad de la persona en años.
        valor_genero(float) Valor que varía según el 
        género de la persona: en caso de ser masculino
        debe ser 5 y en caso de ser femenino debe ser
        -161.
        valor_actividad(float) Valor que depende de 
        la actividad física semanal: 
        1.2: poco o ningún ejercicio
        1.375: ejercicio ligero 
        (1 a 3 días a la semana)
        1.55: ejercicio moderado 
        (3 a 5 días a la semana)
        1.725: deportista 
        1.9: atleta (entrenamientos mañana y tarde)
    Retorno:
        float: La cantidad de calorías que una persona
        quema, al realizar algún tipo de actividad
        física semanalmente. 
    """    
    # Las siguientes instrucciones permiten calcular
    # la TMB en actividad. Llama a la función de
    # calorías en reposo y lo multiplica por el valor
    # de actividad física.
    tmb_actividad = calcular_calorias_en_reposo(peso,altura,
    edad,valor_genero) * valor_actividad
    return tmb_actividad

def consumo_calorias_recomendado_para_adelgazar(peso:float,
    altura:float, edad:int, valor_genero:float ) -> str:
    tmb = calcular_calorias_en_reposo(peso,altura,
    edad,valor_genero)
    """ Calcula el rango de calorías recomendado, 
    que debe consumir una persona diariamente en
    caso de que desee adelgazar, a partir de la
    ecuación definida anteriormente.
    Parámetros:
       peso(float) Peso de la persona en kilogramos.
       altura(float) Altura de la persona en centímetros.
       edad (int) Edad de la persona en años.
       valor_genero(float) Valor que varía según el 
       género de la persona: en caso de ser masculino
       debe ser 5 y en caso de ser femenino debe ser
        -161.
    Retorno:
        str: Una cadena indicando el rango de calorías
        que una persona debe consumir si desea
        adelgazar. El formato de la cadena debe ser
        : "Para adelgazar es recomendado que consumas
        entre: XXX y ZZZ calorías al día.". Siendo 
        XXX el rango inferior y ZZZ el rango superior.
    """    
    # Las siguientes instrucciones permiten calcular
    # las calorías para adelgazar. Arroja un valor
    # del 80% y 85% de las calorías de la TMB.
    ingerir20menos = tmb * 0.8
    ingerir15menos = tmb * 0.85
    recomendacion = "Para adelgazar es recomendado que\
 consumas entre: "+str((round(ingerir20menos, 2)))+" y "+str((round(ingerir15menos, 2)))\
    +" calorías al día"
    return recomendacion                                                
        

    
    
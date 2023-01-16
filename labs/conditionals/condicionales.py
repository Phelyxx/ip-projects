import math

def bisiesto(anio: int) -> bool:
    if anio % 4 != 0:
       a_bisiesto = False
    elif anio % 100 != 0:
        a_bisiesto = True
    elif anio % 400 != 0:
        a_bisiesto = False
    else: a_bisiesto = True
    return a_bisiesto    

def clasificar(a1:float, a2:float, a3:float) ->str:
    """Retorna "Equilatero si el triángulo es equilatero,
    "Isósceles" si es isósceles y "Escaleno si es escaleno"""
    isosceles = "Isósceles"
    escaleno = "Escaleno"
    equilatero = "Equilatero"
    if a1 == a2 and a2 == a3 and a1 == a3:
       triangulo = equilatero
    elif a1 == a2 or a2 == a3 or a1 == a3:
        triangulo = isosceles     
    else: triangulo = escaleno    
    return triangulo
      
def solucionar(a:float, b:float, c:float)->str:
    """Retorna una cadena con la(s) soluciones de la 
    ecuación o una cadena diciendo que no tiene
    solución."""
    if a == 0:
       return "No tiene solución"
    elif (b ** 2 - 4*a*c) > 0: 
        primera = (-b + math.sqrt(b ** 2 - 4*a*c)) / 2*a
        segunda = (-b - math.sqrt(b ** 2 - 4*a*c)) / 2*a 
    else:return "No tiene solución" 
    return (primera, segunda)
       
       
        
        
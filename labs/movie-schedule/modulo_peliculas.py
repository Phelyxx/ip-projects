"""
Ejercicio nivel 2: Agenda de peliculas.
Módulo de cálculos.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.
@author: Cupi2

NOTA IMPORTANTE PARA TENER EN CUENTA EN TODAS LAS FUNCIONES DE ESTE MODULO:
        Los diccionarios de pelicula tienen las siguientes parejas de clave-valor:
            - nombre (str): Nombre de la pelicula agendada.
            - genero (str): Generos de la pelicula separados por comas.
            - duracion (int): Duracion en minutos de la pelicula
            - anio (int): Anio de estreno de la pelicula
            - clasificacion (str): Clasificacion de restriccion por edad
            - hora (int): Hora de inicio de la pelicula
            - dia (str): Indica que día de la semana se planea ver la película
"""

def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int, 
                  clasificacion: str, hora: int, dia: str) -> dict:
    """Crea un diccionario que representa una nueva película con toda su información 
       inicializada.
    Parámetros:
        nombre (str): Nombre de la pelicula agendada.
        genero (str): Generos de la pelicula separados por comas.
        duracion (int): Duracion en minutos de la pelicula
        anio (int): Anio de estreno de la pelicula
        clasificacion (str): Clasificacion de restriccion por edad
        hora (int): Hora a la cual se planea ver la pelicula, esta debe estar entre 
                    0 y 2359
        dia (str): Dia de la semana en el cual se planea ver la pelicula.
    Retorna:
        dict: Diccionario con los datos de la pelicula
    """    
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    pelicula = {"nombre":nombre, "genero":genero, "duracion":duracion, "anio":anio,
"clasificacion":clasificacion,"hora":hora,"dia":dia}
    return pelicula

def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict,  p5: dict) -> dict:
    """Encuentra en cual de los 5 diccionarios que se pasan por parametro esta la 
       pelicula cuyo nombre es dado por parametro.
       Si no se encuentra la pelicula se debe retornar None.
    Parametros:
        nombre_pelicula (str): El nombre de la pelicula que se desea encontrar.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: Diccionario de la pelicula cuyo nombre fue dado por parametro. 
        None si no se encuentra una pelicula con ese nombre.
    """
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    nombre1 = p1["nombre"]
    nombre2 = p2["nombre"]
    nombre3 = p3["nombre"]
    nombre4 = p4["nombre"]
    nombre5 = p5["nombre"]
    peli = None
    if nombre_pelicula == nombre1:
       peli = p1
    elif nombre_pelicula == nombre2:
       peli = p2
    elif nombre_pelicula == nombre3:
       peli = p3
    elif nombre_pelicula == nombre4:
       peli = p4
    elif nombre_pelicula == nombre5:
       peli = p5 
    return peli

def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    """Encuentra la pelicula de mayor duracion entre las peliculas recibidas por
       parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: El diccionario de la pelicula de mayor duracion
    """
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    duracion1 = p1["duracion"]
    duracion2 = p2["duracion"]
    duracion3 = p3["duracion"]
    duracion4 = p4["duracion"]
    duracion5 = p5["duracion"]
    mayor = max(duracion1, duracion2, duracion3, duracion4, duracion5)
    if duracion1 == mayor:
       peli = p1 
    elif duracion2 == mayor:
       peli = p2 
    elif duracion3 == mayor:
       peli = p3 
    elif duracion4 == mayor:
       peli = p4 
    elif duracion5 == mayor:
       peli = p5    
    return peli
    return None

def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> str:
    """Calcula la duracion promedio de las peliculas que entran por parametro. 
       Esto es, la duración total de todas las peliculas dividida sobre el numero de peliculas. 
       Retorna la duracion promedio en una cadena de formato 'HH:MM' ignorando los posibles decimales.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        str: la duracion promedio de las peliculas en formato 'HH:MM'
    """
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    promedio1 = p1["duracion"]
    promedio2 = p2["duracion"]
    promedio3 = p3["duracion"]
    promedio4 = p4["duracion"]
    promedio5 = p5["duracion"]
    promediof = (promedio1 + promedio2 + promedio3 + promedio4 + promedio5) / 5
    horas_prom = promediof / 60
    horas = int(horas_prom)
    minutos_prom = (horas_prom - horas) * 60
    horas = int(horas_prom)
    minutos = round(minutos_prom)
    res = str(horas)+":"+str(minutos)
    return res

def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, anio: int) -> str:
    """Busca entre las peliculas cuales tienen como anio de estreno una fecha estrictamente
       posterior a la recibida por parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
        anio (int): Anio limite para considerar la pelicula como estreno.
    Retorna:
        str: Una cadena con el nombre de la pelicula estrenada posteriormente a la fecha recibida. 
        Si hay mas de una pelicula, entonces se retornan los nombres de todas las peliculas 
        encontradas separadas por comas. Si ninguna pelicula coincide, retorna "Ninguna".
    """
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    anio1 = p1["anio"]
    anio2 = p2["anio"]
    anio3 = p3["anio"]
    anio4 = p4["anio"]
    anio5 = p5["anio"]
    peli = ""
    if anio < anio1:
       peli += p1["nombre"]
    if anio < anio2:
       peli += ", "+p2["nombre"]
    if anio < anio3:
       peli += ", "+p3["nombre"] 
    if anio < anio4:
       peli += ", "+p4["nombre"]  
    if anio < anio5:
       peli += ", "+p5["nombre"]
    if peli =="":
       peli = "Ninguna"
    return peli      
   
def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> int:
    """Indica cuantas peliculas de clasificación '18+' hay entre los diccionarios recibidos.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        int: Numero de peliculas con clasificacion '18+'
    """
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    clasi1 = p1["clasificacion"]
    clasi2 = p2["clasificacion"]
    clasi3 = p3["clasificacion"]
    clasi4 = p4["clasificacion"]
    clasi5 = p5["clasificacion"]    
    res = 0
    if clasi1 == "18+":
       res += 1
    if clasi2 == "18+":
       res += 1
    if clasi3 == "18+":
       res += 1
    if clasi4 == "18+":
       res += 1
    if clasi5 == "18+":
       res += 1       
    return res

def reagendar_pelicula(peli:dict, nueva_hora: int, nuevo_dia: str, 
                       control_horario: bool, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->bool: 
    """Verifica si es posible reagendar la pelicula que entra por parametro. Para esto verifica
       si la nueva hora y el nuevo dia no entran en conflicto con ninguna otra pelicula, 
       y en caso de que el usuario haya pedido control horario verifica que se cumplan 
       las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula a reagendar
        nueva_hora (int): Nueva hora a la cual se quiere ver la pelicula
        nuevo_dia (str): Nuevo dia en el cual se quiere ver la pelicula
        control_horario (bool): Representa si el usuario quiere o no controlar
                                el horario de las peliculas.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        bool: True en caso de que se haya podido reagendar la pelicula, False de lo contrario.
    """
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    duracion_nueva = peli["duracion"]
    genero = peli["genero"]
    hora1 = p1["hora"]
    hora2 = p2["hora"]
    hora3 = p3["hora"]
    hora4 = p4["hora"]
    hora5 = p5["hora"]
    dia1 = p1["dia"]
    dia2 = p2["dia"]
    dia3 = p3["dia"]
    dia4 = p4["dia"]
    dia5 = p5["dia"]  
    duracion1 = p1["duracion"]
    duracion2 = p2["duracion"]
    duracion3 = p3["duracion"]
    duracion4 = p4["duracion"]
    duracion5 = p5["duracion"]
    agendar = False
    if nuevo_dia == dia1 or nuevo_dia == dia2 or nuevo_dia == dia3 or nuevo_dia == dia4 or nuevo_dia == dia5:
       if nueva_hora + duracion_nueva <= hora1 and nueva_hora - duracion1 <= hora1:
          agendar = True
       if nueva_hora + duracion_nueva <= hora2 and nueva_hora - duracion2 <= hora2:
          agendar = True
       if nueva_hora + duracion_nueva <= hora3 and nueva_hora - duracion3 <= hora3:
          agendar = True
       if nueva_hora + duracion_nueva <= hora4 and nueva_hora - duracion4 <= hora3:
          agendar = True
       if nueva_hora + duracion_nueva <= hora5 and nueva_hora - duracion5 <= hora5:
          agendar = True   
    if control_horario == True:
        if genero.count("Documental") >= 1 and nueva_hora >= 2200:
          agendar = False
        if genero.count("Drama") >= 1 and nuevo_dia == "Viernes":
          agendar = False 
        if nuevo_dia == "Lunes" or nuevo_dia == "Martes" or nuevo_dia == "Miercoles" or nuevo_dia == "Jueves" \
or nuevo_dia == "Viernes" :
           if nueva_hora >= 2300 or nueva_hora < 600:
              agendar = False
    if agendar == False:
       peli["hora"] = peli["hora"]
       peli["dia"] = peli["dia"]        
    return agendar
   
def decidir_invitar(peli: dict, edad_invitado: int, autorizacion_padres: bool)->bool:
    """Verifica si es posible invitar a la persona cuya edad entra por parametro a ver la 
       pelicula que entra igualmente por parametro. 
       Para esto verifica el cumplimiento de las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula que se desea ver con el invitado
        edad_invitado (int): Edad del invitado con quien se desea ver la pelicula
        autorizacion_padres (bool): Indica si el invitado cuenta con la autorizacion de sus padres 
        para ver la pelicula
    Retorna:
        bool: True en caso de que se pueda invitar a la persona, False de lo contrario.
    """
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    invitar = False
    genero = peli["genero"]
    clasificacion = peli["clasificacion"]
    if edad_invitado >= 18:
       invitar = True
    elif edad_invitado < 15 and genero == "Terror":
       invitar = False
    elif edad_invitado <= 10 and genero != "Familiar":
       invitar = False 
    elif edad_invitado < 18 and clasificacion == "18+":
       if genero == "Documental": invitar = True
       if autorizacion_padres == True:
          invitar = True 
    elif edad_invitado < 16 and clasificacion == "16+":
       if genero == "Documental": invitar = True
       if autorizacion_padres == True:
          invitar = True 
    elif edad_invitado < 13 and clasificacion == "13+":
       if genero == "Documental": invitar = True
       if autorizacion_padres == True:
          invitar = True 
    elif edad_invitado < 7 and clasificacion == "7+":
       if genero == "Documental": invitar = True
       if autorizacion_padres == True:
          invitar = True    
    return invitar









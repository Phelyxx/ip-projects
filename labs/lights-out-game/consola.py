# -*- coding: utf-8 -*-

from IPython.display import SVG, display
import lights_out as juego


# **************************************
# Funciones para mostrar el juego
# ***************************************

ANCHO = 300


def agregar_luz(figura, casillas, fila, columna, prendida):
    ancho_casilla = ANCHO // (casillas+2)
    pos_x = (columna+1) * ancho_casilla
    pos_y = (fila+1) * ancho_casilla
    fondo_luz = "#ecfc03"
    borde_luz = "#f3fa98"
    fondo_apagado = "#888888"
    borde_apagado = "#999999"
    if prendida:
        agregar_rectangulo(figura, ancho_casilla * 0.9, ancho_casilla * 0.9, pos_x, pos_y, fondo_luz, borde_luz, 2, 2, 2)
    else:
        agregar_rectangulo(figura, ancho_casilla * 0.9, ancho_casilla * 0.9, pos_x, pos_y, fondo_apagado, borde_apagado, 2, 2, 2)

def agregar_jugada(figura, casillas, fila, columna):
    ancho_casilla = ANCHO // (casillas+2)
    pos_x = (columna+1) * ancho_casilla
    pos_y = (fila+1) * ancho_casilla
    borde = "red"
    fondo = "none"
    agregar_rectangulo(figura, ancho_casilla * 0.9, ancho_casilla * 0.9, pos_x, pos_y, fondo, borde, 3, 2, 2)


def agregar_fondo(figura, casillas):
    agregar_rectangulo(figura, ANCHO - 4, ANCHO - 4, 2, 2, "black", "grey", 2, 2, 2)


def agregar_etiquetas_columnas(figura, casillas):
    total_espacios = casillas + 2
    ancho_casilla = ANCHO // total_espacios
    tamano_fuente = 22
    for i in range(1, total_espacios-1):
        num_columna = i - 1
        pos_x = int((i * ancho_casilla) + (ancho_casilla * 0.35))
        pos_y = int(ancho_casilla - (tamano_fuente*0.7))
        agregar_texto(figura, pos_x, pos_y, "sans-serif", tamano_fuente, "teal", "green", str(num_columna))


def agregar_etiquetas_filas(figura, casillas):
    total_espacios = casillas + 2
    ancho_casilla = ANCHO // total_espacios
    tamano_fuente = 22
    for i in range(1, total_espacios-1):
        num_fila = i - 1
        pos_x = int(ancho_casilla * 0.5)
        pos_y = int((i * ancho_casilla) + (ancho_casilla * 0.5) + (tamano_fuente * 0.4))
        agregar_texto(figura, pos_x, pos_y, "sans-serif", tamano_fuente, "teal", "green", str(num_fila))


def agregar_totales_columnas(figura, casillas, totales):
    total_espacios = casillas + 2
    ancho_casilla = ANCHO // total_espacios
    tamano_fuente = 18
    for i in range(1, total_espacios-1):
        pos_x = int((i * ancho_casilla) + (ancho_casilla * 0.35))
        pos_y = int(ancho_casilla*(casillas + 2) - (tamano_fuente))
        agregar_texto(figura, pos_x, pos_y, "sans-serif", tamano_fuente, "white", "grey", totales[i-1])


def agregar_totales_filas(figura, casillas, totales):
    total_espacios = casillas + 2
    ancho_casilla = ANCHO // total_espacios
    tamano_fuente = 18
    for i in range(1, total_espacios-1):
        pos_x = int(ancho_casilla*(casillas + 2) - ancho_casilla * 0.6)
        pos_y = int((i * ancho_casilla) + (ancho_casilla*0.5) + (tamano_fuente*0.4))
        agregar_texto(figura, pos_x, pos_y, "sans-serif", tamano_fuente, "white", "grey", totales[i-1])


def dibujar_tablero(tablero: list, fila = None, columna = None, victoria: bool = False) -> list:
    casillas = len(tablero)
    figura = iniciar_svg(casillas)
    agregar_fondo(figura, casillas)
    for i in range(casillas):
        for j in range(casillas):
            agregar_luz(figura, casillas, i, j, tablero[i][j])

    agregar_etiquetas_filas(figura, casillas)
    agregar_etiquetas_columnas(figura, casillas)

    cantidades_filas = juego.contar_iluminadas_en_filas(tablero)
    agregar_totales_filas(figura, casillas, cantidades_filas)

    cantidades_columnas = juego.contar_iluminadas_en_columnas(tablero)
    agregar_totales_columnas(figura, casillas, cantidades_columnas)

    if fila is not None and columna is not None:
        agregar_jugada(figura, casillas, fila, columna)


    if victoria:
        texto = "¡Ganaste!"
        agregar_texto_anuncio(figura, texto)


    cerrar_svg(figura)
    data = figuras_a_str(figura)
    mostrar_svg(data)



# **************************************
# Funciones para construir la imagen SVG
# ***************************************

def iniciar_svg(casillas):
    ancho_casilla = ANCHO // casillas
    ancho_real = ANCHO
    plantilla_inicio = "<svg width='{}px' height='{}px' xmlns='http://www.w3.org/2000/svg' version='1.1' xmlns:xlink='http://www.w3.org/1999/xlink'>\n"
    return [ plantilla_inicio.format(ancho_real, ancho_real) ]

def cerrar_svg(figura):
    plantilla_fin =  "</svg>"
    figura.append(plantilla_fin)

def agregar_rectangulo(figura, width, height, x, y, fill, stroke, strokewidth, radiusx, radiusy):
    plantilla_rect = "    <rect fill='{}' stroke='{}' stroke-width='{}px' width='{}' height='{}' y='{}' x='{}' ry='{}' rx='{}' />\n"
    rectangulo = plantilla_rect.format(fill, stroke, strokewidth, width, height, y, x, radiusy, radiusx)
    figura.append(rectangulo)

def agregar_texto(figura, x, y, fontfamily, fontsize, fill, stroke, mensaje):
    plantilla_texto ="    <text x='{}' y = '{}' font-family='{}' stroke='{}' fill='{}' font-size='{}px'>{}</text>\n"
    texto = plantilla_texto.format(x, y, fontfamily, stroke, fill, fontsize, mensaje)
    figura.append(texto)

def agregar_texto_anuncio(figura, mensaje):
    fontfamily = "sans-serif"
    fontsize = 48
    x = (ANCHO // 2) - (len(mensaje) * fontsize * 0.25)
    y = ANCHO // 2
    fill = "#1111DD"
    stroke = "#4444FF"
    plantilla_texto = "    <text x='{}' y = '{}' font-weight='bold' font-family='{}' stroke='{}' fill='{}' text-anchor='start' transform='rotate(-10,256,256)' font-size='{}px'>{}</text>\n"
    texto = plantilla_texto.format(x, y, fontfamily, stroke, fill, fontsize, mensaje)
    figura.append(texto)

    stroke = '#1111DD'
    fill = 'none'
    strokewidth = 4
    x -= 20
    y -= 60
    width = 275
    height = 80

    plantilla_rect = "    <rect fill='{}' stroke='{}' stroke-width='{}px' width='{}' height='{}' y='{}' x='{}' ry='{}' rx='{}'  transform='rotate(-10,256,256)' />\n"
    rectangulo = plantilla_rect.format(fill, stroke, strokewidth, width, height, y, x, 0, 0)
    figura.append(rectangulo)


def figuras_a_str(figura):
    return "".join(figura)


def mostrar_svg(data: str):
    display(SVG(data=data))

# **************************************
# Funciones para controlar el juego
# ***************************************

def mostrar_menu() -> None:
    display(SVG(filename="logo.svg"))
    print("1. Juego aleatorio")
    print("2. Cargar Juego")
    print("3. Salir")

def iniciar_aplicacion() -> None:
    seguir = True
    while seguir:
        mostrar_menu()
        opcion = input("Seleccione la opción deseada: ")
        try:
            num_opcion = int(opcion)
            if num_opcion == 1:
                tablero = ejecutar_random()
                ejecutar_jugar(tablero)
            elif num_opcion == 2:
                tablero = ejecutar_cargar()
                ejecutar_jugar(tablero)
            elif num_opcion == 3:
                seguir = False
            else:
                print("La opción seleccionada no es válida")
        except ValueError as e:
            print("La opción seleccionada no es un número válido", e)


def ejecutar_random():
    tablero = juego.construir_tablero(5)
    return tablero


def ejecutar_cargar():
    archivo = input("Indique el nombre del archivo que desea cargar (tablero.lights): ")
    if len(archivo) == 0:
        archivo = "tablero.lights"
    tablero = juego.cargar_tablero(archivo)
    return tablero


def ejecutar_jugar(tablero: list) -> None:
    dibujar_tablero(tablero)
    numero_jugada = 0
    fin_del_juego = False
    error = True
    fila = None
    columna = None
    while not fin_del_juego:
        numero_jugada += 1
        if error:
            jugada = input(str(numero_jugada) + ": ¿En qué casilla quiere jugar? Indique la fila y la columna o '*' para salir: ")
        else:
            jugada = input(str(numero_jugada) + ": ¿En qué casilla quiere jugar? Indique la fila y la columna ({} {}) o '*' para salir: ".format(fila, columna))
            if len(jugada.strip()) == 0:
                jugada = str(fila) + " " + str(columna)
        if jugada.strip() != "*" and jugada.strip() != "'*'":
            jugada = jugada.replace(" ", " ")
            partes = jugada.split(",")
            if len(partes) != 2:
                partes = jugada.split(" ")
            try:
                fila = int(partes[0].strip())
                columna = int(partes[1].strip())
                error = False
                juego.jugar(tablero, fila, columna)
                fin_del_juego = juego.revisar_final(tablero)
            except (IndexError, ValueError):
                error = True
                print("\nError:")
                print("La fila y la columna deben ser dos enteros.")
                print("Por favor vuelva a intentarlo.")
                fila = None
                columna = None
        else:
            fin_del_juego = True
            
        dibujar_tablero(tablero, fila, columna, victoria=juego.revisar_final(tablero))
        if fin_del_juego:
            print("\nSe hicieron", numero_jugada, "jugadas")


iniciar_aplicacion()

def picas_y_fijas(numero_secreto:int, intento:int) -> dict:
    """
    El juego de las Picas y Fijas es un juego matemático muy sencillo, que consiste en adivinar un número de 4 cifras (distintas) y de todos los dígitos diferentes. Para esto el jugador que intenta adivinar deberá decir el número que cree está escondiendo el otro, y este deberá responder el número de picas y fijas que tiene ahora el jugador.
    """
    secreto_list = [int(x) for x in str(numero_secreto)]
    intento_list = [int(x) for x in str(intento)]
    picas = 0
    fijas = 0
    for i, num in enumerate(intento_list):
        if num in secreto_list:
            if num == secreto_list[i]:
                fijas += 1
            else:
                picas += 1
    return {'PICAS': picas, 'FIJAS': fijas}
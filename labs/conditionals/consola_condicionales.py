
import condicionales

def ejecutar_bisiesto()->None:
    print("Vamos a decidir si un año es bisiesto o no")
    #TODO: completar
    anio = int(input("Digite el año: "))
    bisiesto = condicionales.bisiesto(anio)
    if bisiesto == True:
       print("El año es bisiesto")
    else: print ("El año no es bisiesto")
def ejecutar_clasificar()->None:
    print("Vamos a determinar de qué tipo es un triángulo dados sus ángulos")
    #TODO: completar
    a1 = float(input("Digite el ángulo del primer lado: "))
    a2 = float(input("Digite el ángulo del segundo lado: "))
    a3 = float(input("Digite el ángulo del tercer lado: "))
    resultado = condicionales.clasificar(a1,a2,a3)
    print (resultado)
    
def ejecutar_solucionar()->None:
    print("Vamos a tratar de hallar las soluciones de una ecuación cuadrática")
    #TODO: completar
    a = float(input("Digite el valor de a: "))
    b = float(input("Digite el valor de b: "))
    c = float(input("Digite el valor de c: "))
    res = condicionales.solucionar(a,b,c)
    print(res)

def mostrar_menu()->None:
    print ("Menu principal")
    print ("(1) Año bisiesto")
    print ("(2) Tipo de triángulo")
    print ("(3) Solución ecuación cuadrática")

    x = input("Seleccione su opción: ")
    #TODO: ejecuatar una funcionalidad dada la opción seleccionada
    if x == "1":
       ejecutar_bisiesto()
    elif x == "2":
       ejecutar_clasificar()
    elif x == "3":
       ejecutar_solucionar()


def iniciar_aplicacion()->None:
    print("Bienvenido al laboratorio de condicionales")
    mostrar_menu()

#PROGRAMA PRINCIPAL
iniciar_aplicacion()

    
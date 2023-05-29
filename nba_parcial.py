import re
import json



def parse_json(nombre_archivo: str) -> list:
    """
    esta funcion recibe la ubicacion del archivo json
    crea un diccionario
    abre el archivo y le carga todos lo datos
    
    """
    dic_json = {}
    with open(nombre_archivo, "r", encoding='utf-8') as archivo:
        dic_json = json.load(archivo)

    return dic_json["jugadores"]

lista_jugadores = parse_json("dt.json")
lista_auxiliar = lista_jugadores[:]



def jugadores_con_posicion(lista_auxiliar: list) -> str:
    '''
    recibe como parametro la lista auxiliar
    y la convierte en una cadena de
    nombres de los jugadores y sus respectivas posiciones
    '''
    lista_jugadores_posicion = []
    for jugador in lista_auxiliar:
        nombre = jugador["nombre"]
        posicion = jugador["posicion"]
        lista_jugadores_posicion.append(f"{nombre} - {posicion}")

    return '\n'.join(lista_jugadores_posicion)

    

def indice_jugadores(lista_auxiliar: list) -> str:
    '''
    recibe como parametro la lista auxiliar creada anteriormente
    crea una cadena de texto con los nombres de los jugadores y sus indices
    retorna la cadena de los nombres con sus indices
    
    '''
    lista_jugadores = []
    for i in range(len(lista_auxiliar)):
        nombre = lista_auxiliar[i]["nombre"]
        lista_jugadores.append(f"{i+1}- {nombre}")
    return '\n'.join(lista_jugadores)



def estadisticas_completas(lista_auxiliar: list, indice_seleccionado: int)->str:
    '''
    recibe como parametro la lista auxiliar creada anteriormente
    y un indice seleccionado por el usuario
    muestra la lista de todos los jugadores con sus indices
    y retorna el nombre del jugador con sus estadisticas elegido por el usuario
    '''
    if indice_seleccionado <= 0 or indice_seleccionado > len(lista_auxiliar):
        return "Opcion no valida"
    else:
        jugador = lista_auxiliar[indice_seleccionado - 1]
        nombre = jugador["nombre"]
    
    estadisticas = jugador["estadisticas"]
    jugador_con_estadisticas = f"{nombre}: {estadisticas}"

    return jugador_con_estadisticas



def exportar_csv(lista_auxiliar:list, indice_seleccionado:int, nombre_archivo:str)->None:
    '''
    recibe como parametro la lista auxiliar creada anteriormente,
    un indice seleccionado por el usuario y el nombre del archivo csv a crear
    muestra la lista de todos los jugadores con sus indices
    el usuario elige un jugador por el indice y crea un archivo
    csv con la informacion del jugador seleccionado
    
    '''
    with open(nombre_archivo, "w") as archivo:
        jugador = lista_auxiliar[indice_seleccionado-1]
        linea = "{0},{1},{2}\n"
        linea = linea.format(jugador["nombre"], jugador["posicion"], str(jugador["estadisticas"]))
        archivo.write(linea)




def mostrar_logros(lista_auxiliar: list, jugador_seleccionado: str) -> str:
    '''
    recibe como parametro la lista auxiliar creada anteriormente
    y el nombre de un jugador seleccionado
    la funcion compara si el nombre ingresado coincide con algun jugador de la lista
    y si lo encuentra retorna el jugador con sus logros
    '''
    for jugador in lista_auxiliar:
        if jugador["nombre"].lower() == jugador_seleccionado.lower():
            nombre = jugador["nombre"]
            logros = jugador["logros"]
            jugador_con_logros = f"{nombre}: {logros}"
            return jugador_con_logros
    return "Opción no válida, ingrese nombre completo"




def calcular_promedio(lista_auxiliar: list) -> str:
    '''
    recibe como parametro solamente la lista creada anteriormente
    la funcion saca el promedio de puntos por partido de todo el equipo,
    ordena por nombre los jugadores de manera ascendente.
    y retorna los nombres ordenados y el total del promedio

    '''
    lista_promedios = []
    lista_nombres = []
    
    for jugador in lista_auxiliar:
        nombre = jugador["nombre"]
        promedio_cada_jugador = jugador["estadisticas"]["promedio_puntos_por_partido"]
        lista_nombres.append(nombre)
        lista_promedios.append(promedio_cada_jugador)
        
    promedio_total = sum(lista_promedios) / len(lista_promedios)

    flag_continuar = True

    while(flag_continuar == True):
        flag_continuar = False
        for i in range(len(lista_nombres)- 1):
            if(lista_nombres[i] > lista_nombres[i + 1]):
                aux = lista_nombres[i]
                lista_nombres[i] = lista_nombres[i + 1]
                lista_nombres[i+1] = aux
                flag_continuar = True

    print("\n".join(lista_nombres))

    return promedio_total 





def miembro_salon_fama(lista_auxiliar: list, jugador_seleccionado: str) -> str:
    '''
    recibe como parametro la lista auxiliar creada anteriormente
    y el nombre de un jugador seleccionado
    lo que hace la funcion es comparar si el nombre ingresado coincide con algun
    nombre de la lista
    y ver si es miembro del salon de la fama
    si lo es, retorna un texto afirmandolo
    '''
    for jugador in lista_auxiliar:
            if jugador["nombre"].lower() == jugador_seleccionado.lower():
                if "Miembro del Salon de la Fama del Baloncesto" in jugador["logros"]:
                    nombre = jugador["nombre"]
                    jugador_miembro = f"{nombre}: Es Miembro del Salon de la Fama del Baloncesto"
                    return jugador_miembro
                else:
                    nombre = jugador["nombre"]
                    jugador_no_miembro = f"{nombre}: No Es Miembro del Salon de la Fama del Baloncesto"
                    return jugador_no_miembro
            else:
                return "Opcion no valida, ingrese nombre completo"
        
    


def calcular_y_mostrar(lista_auxiliar: list,opcion: str) -> str:
    '''
    recibe como parametro la lista auxiliar creada anteriormente
    y una opcion que es una estadistica a elegir.
    lo que hace la funcion es descubrir el jugador con mayor cantidad en
    la estadistica elegida
    y retorna su nombre y su estadistica total

    '''
    lista_aux = []
    nombre_max= ""
    max = 0

    for jugador in lista_auxiliar:
        nombre = jugador["nombre"]
        estadistica = jugador["estadisticas"][opcion]
        lista_aux.append(estadistica)
        
        if estadistica > max:
            max = estadistica
            nombre_max = nombre


    return f"El jugador con mayor cantidad es {nombre_max} con un total de {max}"

def calcular_y_mostrar_promedio(lista_auxiliar: list, opcion: str) -> str:
    '''
    recibe como parametro la lista auxiliar creada anteriormente
    y una opcion que es una estadistica a elegir.
    la funcion saca el promedio de el equipo entero en la estadistica elegida,
    menos el peor jugador en la estadistica elegida,
    y retorna el total del promedio sin el peor jugador

    '''
    lista_aux = []
    lista_aux_nombres = []
    lista_aux_sin_min = []
    
    for jugador in lista_auxiliar:
        estadistica = jugador["estadisticas"][opcion]
        nombre = jugador["nombre"]
        lista_aux.append(estadistica)
        lista_aux_nombres.append(nombre)

    menor = min(lista_aux)


    for estadistica in lista_aux:
        if estadistica != menor:
            lista_aux_sin_min.append(estadistica)
    
    promedio_sin_min = sum(lista_aux_sin_min) / len(lista_aux_sin_min)

    mensaje = f"el promedio de puntos por partido del equipo excluyendo al jugador con menos promedio es: {promedio_sin_min}"

    return mensaje





def calcular_y_mostrar_mayor_logros(lista_auxiliar: list) -> str:
    '''
    recibe como parametro la lista auxiliar creada anteriormente
    la funcion busca el jugador con mayor cantidad de logros
    y retorna el nombre, su total de logros y cuales logros
    '''
    nombre_max_cantidad_logros = ""
    max_logros = 0
    lista_logros = []

    for jugador in lista_auxiliar:
        cantidad_logros = len(jugador["logros"])
        if cantidad_logros > max_logros:
            max_logros = cantidad_logros
            nombre_max_cantidad_logros = jugador["nombre"]
            lista_logros.append(jugador["logros"])
        
    
    mensaje = f"El jugador con mayor cantidad de logros es {nombre_max_cantidad_logros} con un total de {max_logros} logros: \n{lista_logros}"
    
    
    return mensaje




def jugadores_promedio_porcentaje_mayor(lista_auxiliar: list, valor_ingresado: float, opcion: str) -> str:
    '''
    recibe como parametro la lista auxiliar creada anteriormente, un numero ingresado por
    el usuario  y una opcion a una estadistica a eleccion.
    la funcion busca los jugadores con mejor porcentaje al numero ingresado
    y retorna el nombre de los jugadores con sus porcentajes

    '''
    lista_jugadores_mayor = []

    for jugador in lista_auxiliar:
        if jugador["estadisticas"][opcion] > valor_ingresado:
            nombre = jugador["nombre"]
            estadistica = jugador["estadisticas"][opcion]
            lista_jugadores_mayor.append(f"{nombre} - {estadistica}")
    
    if len(lista_jugadores_mayor) == 0:
        return "No hay jugadores"
    
    return "\n".join(lista_jugadores_mayor)


            
def jugadores_ordenados_porcentaje_tiros(lista_auxiliar: list,valor_porcentaje: float) -> str:
    '''
    recibe como parametro la lista auxiliar creada anteriormente y
    un numero ingresado por el usuario.
    la funcion busca los jugadores con mejor porcentaje al numero ingresado y los ordena
    en orden de posicion en la cancha
    y retorna el nombre de los jugadores con sus posiciones y sus porcentajes ordenados
    ordenados por sus respectivas posiciones
    '''
    jugadores_mayor_porcentaje = []

    for jugador in lista_auxiliar:
        if jugador["estadisticas"]["porcentaje_tiros_de_campo"] > valor_porcentaje:
            jugadores_mayor_porcentaje.append(jugador)
            
    posiciones = ["Base", "Escolta", "Alero", "Ala-Pívot", "Pívot"]

    for posicion in posiciones:
        for jugador in jugadores_mayor_porcentaje:
            if jugador["posicion"] == posicion:
                print(f"Nombre: {jugador['nombre']}")
                print(f"Posición: {jugador['posicion']}")
                print(f"Porcentaje de tiros de campo: {jugador['estadisticas']['porcentaje_tiros_de_campo']}%")
                



def opciones_menu(lista_auxiliar: list) -> str:
    """
    Esta función muestra el menu, le permite al usuario
    ingresar una opcion e imprime por consola
    la opcion elegida
    """
    
    opcion_elegida_por_usuario = input("\n\n1- Mostrar lista de jugadores del Dream Team\n"
                        "2- Seleccionar un jugador por su indice y mostrar sus estadisticas completas,luego guarda toda la informacion de ese jugador en un archivo CSV\n"
                        "3- Permite exportar los datos del jugador elegido a un archivo csv\n"
                        "4- Selecione un jugador por su nombre y muestra sus logros\n"
                        "5- Promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre de manera ascendente\n"
                        "6- Seleccione un jugador por su nombre y muestra si ese jugador es miembro del Salón de la Fama del Baloncesto\n"
                        "7- El jugador con la mayor cantidad de rebotes totales.\n"
                        "8- El jugador con el mayor porcentaje de tiros de campo.\n"
                        "9- El jugador con la mayor cantidad de asistencias totales.\n"
                        "10- Ingrese un valor y muestra los jugadores que han promediado más puntos por partido que ese valor.\n"
                        "11- Ingrese un valor y muestra los jugadores que han promediado más rebotes por partido que ese valor.\n"
                        "12- Ingrese un valor y muestra los jugadores que han promediado más asistencias por partido que ese valor.\n"
                        "13- El jugador con la mayor cantidad de robos totales.\n"
                        "14- El jugador con la mayor cantidad de bloqueos totales\n"
                        "15- Ingrese un valor y muestra los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.\n"
                        "16- El promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.\n"
                        "17- El jugador con la mayor cantidad de logros obtenidos\n"
                        "18- Ingrese un valor y muestra los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.\n"
                        "19- El jugador con la mayor cantidad de temporadas jugadas\n"
                        "20- Ingrese un valor y muestra los jugadores, ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor.\n\nIngrese un número: ")
        

    if opcion_elegida_por_usuario == "1":
        print("Nombre Jugador - Posición:\n")
        print(jugadores_con_posicion(lista_auxiliar))
    elif opcion_elegida_por_usuario == "2":
        print(indice_jugadores(lista_auxiliar))
        indice_seleccionado = int(input("Seleccione un jugador por su indice: "))
        print(estadisticas_completas(lista_auxiliar, indice_seleccionado))
    elif opcion_elegida_por_usuario == "3":
        print(indice_jugadores(lista_auxiliar))
        indice_seleccionado = int(input("Seleccione un jugador por su indice: "))
        exportar_csv(lista_auxiliar, indice_seleccionado, "jugador.csv")
    elif opcion_elegida_por_usuario == "4":
        print(indice_jugadores(lista_auxiliar))
        jugador_seleccionado = input("Seleccione un jugador por su nombre: ")
        print(mostrar_logros(lista_auxiliar,jugador_seleccionado))
    elif opcion_elegida_por_usuario == "5":
        print(f"El promedio de puntos por partido de todo el equipo del Dream Team es: {calcular_promedio(lista_auxiliar)}")
    elif opcion_elegida_por_usuario == "6":
        print(indice_jugadores(lista_auxiliar))
        jugador_seleccionado = input("Seleccione un jugador por su nombre: ")
        print(miembro_salon_fama(lista_auxiliar,jugador_seleccionado))
    elif opcion_elegida_por_usuario == "7":
        print(calcular_y_mostrar(lista_auxiliar,opcion = "rebotes_totales"))
    elif opcion_elegida_por_usuario == "8":
        print(calcular_y_mostrar(lista_auxiliar,opcion = "porcentaje_tiros_de_campo"))
    elif opcion_elegida_por_usuario == "9":
        print(calcular_y_mostrar(lista_auxiliar,opcion = "asistencias_totales"))
    elif opcion_elegida_por_usuario == "10":
        valor_ingresado = float(input("Ingrese un valor: "))
        print(jugadores_promedio_porcentaje_mayor(lista_auxiliar,valor_ingresado,opcion="promedio_puntos_por_partido"))
    elif opcion_elegida_por_usuario == "11":
        valor_ingresado = float(input("Ingrese un valor: "))
        print(jugadores_promedio_porcentaje_mayor(lista_auxiliar,valor_ingresado,opcion="promedio_rebotes_por_partido"))
    elif opcion_elegida_por_usuario == "12":
        valor_ingresado = float(input("Ingrese un valor: "))
        print(jugadores_promedio_porcentaje_mayor(lista_auxiliar,valor_ingresado,opcion="promedio_asistencias_por_partido"))
    elif opcion_elegida_por_usuario == "13":
        print(calcular_y_mostrar(lista_auxiliar,opcion = "robos_totales"))
    elif opcion_elegida_por_usuario == "14":
        print(calcular_y_mostrar(lista_auxiliar,opcion = "bloqueos_totales"))
    elif opcion_elegida_por_usuario == "15":
        valor_ingresado = float(input("Ingrese un valor: "))
        print(jugadores_promedio_porcentaje_mayor(lista_auxiliar,valor_ingresado,opcion="porcentaje_tiros_libres"))
    elif opcion_elegida_por_usuario == "16":
        print(calcular_y_mostrar_promedio(lista_auxiliar,opcion="promedio_puntos_por_partido"))
    elif opcion_elegida_por_usuario == "17":
        print(calcular_y_mostrar_mayor_logros(lista_auxiliar))
    elif opcion_elegida_por_usuario == "18":
        valor_ingresado = float(input("Ingrese un valor: "))
        print(jugadores_promedio_porcentaje_mayor(lista_auxiliar,valor_ingresado,opcion="porcentaje_tiros_triples"))
    elif opcion_elegida_por_usuario == "19":
        print(calcular_y_mostrar(lista_auxiliar,opcion = "temporadas"))
    elif opcion_elegida_por_usuario == "20":
        valor_porcentaje = float(input("Ingresa el valor del porcentaje de tiros de campo: "))
        jugadores_ordenados_porcentaje_tiros(lista_auxiliar,valor_porcentaje)
    else:
        print("Opción no válida\nIngrese la opcion correcta")

opciones_menu(lista_auxiliar)





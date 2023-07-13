import json
import re

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




#1) Determinar la cantidad de jugadores que hay por cada posición.
#Ejemplo:
#Base: 2
#Alero: 3
def calcular_jugadores_por_posicion(lista_auxiliar: list) -> str:
    '''
    recibe un unico parametro, la lista auxiliar creada anteriormente
    lo que hace la funcion es crea un diccionario vacio y le mete como clave
    la posicion y como valor el contador de cuantos jugadores hay en esa posicion
    y retorna las posiciones y su cantidad
    '''

    dic_contador_posiciones  = {}
    
    for jugador in lista_auxiliar:
        posicion = jugador['posicion']

        if posicion in dic_contador_posiciones:
            dic_contador_posiciones[posicion] += 1
        else:
            dic_contador_posiciones[posicion] = 1
    
    for posicion in dic_contador_posiciones:
        contador = dic_contador_posiciones[posicion]
        print(f"{posicion}: {contador}")
            


#2)Mostrar la lista de jugadores ordenadas por la cantidad de All-Star de forma descendente.
#La salida por pantalla debe tener un formato similar a este:
#Michael Jordan (14 veces All Star)
#Magic Johnson (12 veces All-Star)

#------------------------------------MOSTRAR AL PROFE--------------------------------------------

def mostrar_jugadores_cantidad_allstar(lista_auxiliar):
    dic_jugadores_allstar = {}
    for jugador in lista_auxiliar:
        nombre = jugador["nombre"]
        for logro in jugador["logros"]:
            match = re.search(r"(\d+) veces All-Star", logro)
            if match:
                veces_allstar = int(match.group(1))
                if nombre in dic_jugadores_allstar:
                    dic_jugadores_allstar[nombre] += veces_allstar
                else:
                    dic_jugadores_allstar[nombre] = veces_allstar
    
    for nombre, contador in dic_jugadores_allstar.items():
        print(f"{nombre} ({contador} veces All-Star)")



#------------------------------------MOSTRAR AL PROFE--------------------------------------------



#3) Determinar qué jugador tiene las mejores estadísticas en cada valor. La salida por pantalla debe tener un formato similar a este:
#Mayor cantidad de temporadas: Karl Malone (19)
#Mayor cantidad de puntos totales: Karl Malon (36928)

def encontrar_maximo_valor(lista_auxiliar, opcion):
    max_valor = 0
    max_nombre = ""
    for jugador in lista_auxiliar:
        nombre = jugador["nombre"]
        valor = jugador["estadisticas"][opcion]
        if valor > max_valor:
            max_valor = valor
            max_nombre = nombre
    mensaje = f"{max_nombre} ({max_valor})"

    return mensaje



# #4) Determinar qué jugador tiene las mejores estadísticas de todos.

def jugador_mejor_estadistica(lista_auxiliar: list) -> str:
    nombre_mejor_jugador = ""
    estadistica_mejor_jugador = 0
    for jugador in lista_auxiliar:
        estadisticas = jugador["estadisticas"]
        puntos_totales = estadisticas["puntos_totales"]
        promedio_puntos_por_partido = estadisticas["promedio_puntos_por_partido"]
        rebotes_totales = estadisticas["rebotes_totales"]
        promedio_rebotes_por_partido = estadisticas["promedio_rebotes_por_partido"]
        asistencias_totales = estadisticas["asistencias_totales"]
        promedio_asistencias_por_partido = estadisticas["promedio_asistencias_por_partido"]
        robos_totales = estadisticas["robos_totales"]
        bloqueos_totales = estadisticas["bloqueos_totales"]
        porcentaje_tiros_de_campo = estadisticas["porcentaje_tiros_de_campo"]
        porcentaje_tiros_libres = estadisticas["porcentaje_tiros_libres"]
        porcentaje_tiros_triples = estadisticas["porcentaje_tiros_triples"]

        puntuacion = (puntos_totales + puntos_totales + promedio_puntos_por_partido
                        + rebotes_totales + promedio_rebotes_por_partido + asistencias_totales
                        + promedio_asistencias_por_partido + robos_totales + bloqueos_totales
                        + porcentaje_tiros_de_campo + porcentaje_tiros_libres
                        + porcentaje_tiros_triples)

        if puntuacion > estadistica_mejor_jugador:
            estadistica_mejor_jugador = puntuacion
            nombre_mejor_jugador = jugador["nombre"]
        
    print(f"El jugador con las mejores estadisticas es {nombre_mejor_jugador} sumando todas sus estadisticas con un total de {estadistica_mejor_jugador}")
        

def opciones_menu(lista_auxiliar: list) -> str:
    """
    Esta función muestra el menu, le permite al usuario
    ingresar una opcion e imprime por consola
    la opcion elegida
    """
    
    opcion_elegida_por_usuario = input("\n\n1- Determinar la cantidad de jugadores que hay por cada posición. Ejemplo: Base: 2 Alero: 3\n"
                        "2- Mostrar la lista de jugadores ordenadas por la cantidad de All-Star de forma descendente. La salida por pantalla debe tener un formato similar a este: Michael Jordan (14 veces All Star) Magic Johnson (12 veces All-Star)\n"
                        "3- Determinar qué jugador tiene las mejores estadísticas en cada valor. La salida por pantalla debe tener un formato similar a este: Mayor cantidad de temporadas: Karl Malone (19) Mayor cantidad de puntos totales: Karl Malon (36928)\n"
                        "4- Determinar qué jugador tiene las mejores estadísticas de todos.\n\nIngrese un número: ")
        

    if opcion_elegida_por_usuario == "1":
        calcular_jugadores_por_posicion(lista_auxiliar)
    elif opcion_elegida_por_usuario == "2":
        mostrar_jugadores_cantidad_allstar(lista_auxiliar)
    elif opcion_elegida_por_usuario == "3":
        mensaje_temporadas = "Mayor cantidad de temporadas: " + encontrar_maximo_valor(lista_auxiliar, opcion="temporadas")
        print(mensaje_temporadas)
        mensaje_puntos_totales = "Mayor cantidad de puntos_totales: " + encontrar_maximo_valor(lista_auxiliar, opcion="puntos_totales")
        print(mensaje_puntos_totales)
        mensaje_promedio_puntos_por_partido = "Mayor cantidad de promedio_puntos_por_partido: " + encontrar_maximo_valor(lista_auxiliar, opcion="promedio_puntos_por_partido")
        print(mensaje_promedio_puntos_por_partido)
        mensaje_rebotes_totales = "Mayor cantidad de rebotes_totales: " + encontrar_maximo_valor(lista_auxiliar, opcion="rebotes_totales")
        print(mensaje_rebotes_totales)
        mensaje_promedio_rebotes_por_partido = "Mayor cantidad de promedio_rebotes_por_partido: " + encontrar_maximo_valor(lista_auxiliar, opcion="promedio_rebotes_por_partido")
        print(mensaje_promedio_rebotes_por_partido)
        mensaje_asistencias_totales = "Mayor cantidad de asistencias_totales: " + encontrar_maximo_valor(lista_auxiliar, opcion="asistencias_totales")
        print(mensaje_asistencias_totales)
        mensaje_promedio_asistencias_por_partido = "Mayor cantidad de promedio_asistencias_por_partido: " + encontrar_maximo_valor(lista_auxiliar, opcion="promedio_asistencias_por_partido")
        print(mensaje_promedio_asistencias_por_partido)
        mensaje_robos_totales = "Mayor cantidad de robos_totales: " + encontrar_maximo_valor(lista_auxiliar, opcion="robos_totales")
        print(mensaje_robos_totales)
        mensaje_bloqueos_totales = "Mayor cantidad de bloqueos_totales: " + encontrar_maximo_valor(lista_auxiliar, opcion="bloqueos_totales")
        print(mensaje_bloqueos_totales)
        mensaje_porcentaje_tiros_de_campo = "Mayor cantidad de porcentaje_tiros_de_campo: " + encontrar_maximo_valor(lista_auxiliar, opcion="porcentaje_tiros_de_campo")
        print(mensaje_porcentaje_tiros_de_campo)
        mensaje_porcentaje_tiros_libres = "Mayor cantidad de porcentaje_tiros_libres: " + encontrar_maximo_valor(lista_auxiliar, opcion="porcentaje_tiros_libres")
        print(mensaje_porcentaje_tiros_libres)
        mensaje_porcentaje_tiros_triples = "Mayor cantidad de porcentaje_tiros_triples: " + encontrar_maximo_valor(lista_auxiliar, opcion="porcentaje_tiros_triples")
        print(mensaje_porcentaje_tiros_triples)
    elif opcion_elegida_por_usuario == "4":
        jugador_mejor_estadistica(lista_auxiliar)
    else:
        print("Opción no válida\nIngrese la opcion correcta")

opciones_menu(lista_auxiliar)
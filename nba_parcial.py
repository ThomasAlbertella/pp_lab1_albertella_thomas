import re
import json

def parse_json(nombre_archivo:str)->list:
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


#Mostrar la lista de todos los jugadores del Dream Team. Con el formato:
#Nombre Jugador - Posición. Ejemplo:
#Michael Jordan - Escolta


def jugadores_con_posicion(lista_auxiliar:list)->str:
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

    
    return ('\n'.join(lista_jugadores_posicion))

    




    
def indice_jugadores(lista_auxiliar: list) -> str:
    lista_jugadores = []
    for i in range(len(lista_auxiliar)):
        nombre = lista_auxiliar[i]["nombre"]
        lista_jugadores.append(f"{i+1}- {nombre}")
    return ('\n'.join(lista_jugadores))


#Permitir al usuario seleccionar un jugador por su índice y
# mostrar sus estadísticas completas, incluyendo temporadas jugadas,
# puntos totales, promedio de puntos por partido, rebotes totales,
# promedio de rebotes por partido, asistencias totales, promedio de asistencias por partido,
# robos totales, bloqueos totales, porcentaje de tiros de campo, porcentaje de tiros libres y
# porcentaje de tiros triples.

def estadisticas_completas(lista_auxiliar:list):
    indice_seleccionado = int(input("Seleccione un jugador por su indice: "))
    if indice_seleccionado <= 0 or indice_seleccionado > len(lista_auxiliar):
        return "Opcion no valida"
    else:
        jugador = lista_auxiliar[indice_seleccionado - 1]
        nombre = jugador["nombre"]
        estadisticas = jugador["estadisticas"]
        jugador_con_estadisticas = f"{nombre}: {estadisticas}"
    return jugador_con_estadisticas


#Después de mostrar las estadísticas de un jugador seleccionado por el usuario,
#  permite al usuario guardar las estadísticas de ese jugador en un archivo CSV.
#  El archivo CSV debe contener los siguientes campos: nombre, posición, temporadas,
#  puntos totales, promedio de puntos por partido, rebotes totales, promedio de rebotes
#  por partido, asistencias totales, promedio de asistencias por partido, robos totales
# , bloqueos totales, porcentaje de tiros de campo, porcentaje de tiros libres y
#  porcentaje de tiros triples.

def exportar_csv(lista_auxiliar:list , nombre_archivo:str):
    """
    
    """

    archivo = open(nombre_archivo, "w+")
    for jugador in lista_auxiliar:
        linea = jugador["nombre"] + "," + jugador["posicion"] + "," + str(jugador["estadisticas"]) + "\n"
        archivo.write(linea)

    archivo.close()   



#Permitir al usuario buscar un jugador por su nombre y mostrar sus logros,
#  como campeonatos de la NBA, participaciones en el All-Star y pertenencia
#  al Salón de la Fama del Baloncesto, etc.

def mostrar_logros(lista_auxiliar:list):
    jugador_seleccionado = input("Seleccione un jugador por su nombre: ")
    for jugador in lista_auxiliar:
        if re.findall(r"[a-zA-Z ]+", jugador_seleccionado):
            if jugador["nombre"].lower() == jugador_seleccionado.lower():
                nombre = jugador["nombre"]
                logros = jugador["logros"]
                jugador_con_logros = f"{nombre}: {logros}"
        else:
            return "Opcion no valida"
    return jugador_con_logros


#Calcular y mostrar el promedio de puntos por partido de todo el equipo
#  del Dream Team, ordenado por nombre de manera ascendente. 

def calcular_promedio(lista_auxiliar:list):
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


#Permitir al usuario ingresar el nombre de un jugador y mostrar si ese
#  jugador es miembro del Salón de la Fama del Baloncesto.

def miembro_salon_fama(lista_auxiliar:list):
    jugador_seleccionado = input("Seleccione un jugador por su nombre: ")

    for jugador in lista_auxiliar:
        if re.findall(r"[a-zA-Z ]+", jugador_seleccionado):
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
            return "Opcion no valida"
        
    return jugador_miembro,jugador_no_miembro


#Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.
def jugador_mas_rebotes_totales(lista_auxiliar:list):
    lista_rebotes = []
    nombre_max_rebotes = ""
    rebote_max = 0

    for jugador in lista_auxiliar:
        nombre = jugador["nombre"]
        rebotes_totales = jugador["estadisticas"]["rebotes_totales"]
        lista_rebotes.append(rebotes_totales)
        
        if rebotes_totales > rebote_max:
            rebote_max = rebotes_totales
            nombre_max_rebotes = nombre
            
    return f"El jugador con mas rebotes es {nombre_max_rebotes} con un total de {rebote_max} rebotes"

#Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.
def jugador_mayor_porcentaje_tiros(lista_auxiliar:list):
    lista_porcentajes = []
    nombre_max_porcentaje = ""
    porcentaje_max = 0

    for jugador in lista_auxiliar:
        nombre = jugador["nombre"]
        porcentajes_tiros = jugador["estadisticas"]["porcentaje_tiros_de_campo"]
        lista_porcentajes.append(porcentajes_tiros)
        
        if porcentajes_tiros > porcentaje_max:
            porcentaje_max = porcentajes_tiros
            nombre_max_porcentaje = nombre
            
    return f"El jugador con mas porcentaje de tiro es {nombre_max_porcentaje} con un total de {porcentaje_max}"


        

        

     

    


    
    

    


    

def opciones_menu(lista_auxiliar):
    """
    Esta función muestra el menu, le permite al usuario
    ingresar una opcion e imprime por consola
    la opcion elegida
    """
    
    opcion_elegida_por_usuario = input("\n\n1- Mostrar lista de jugadores del Dream Team\n"
                                        "2- Obtener nombre y dato \n"
                                        "3- el superhéroe más alto de género F\n"
                                        "4- el superhéroe más bajo de género M \n"
                                        "5- el superhéroe más bajo de género F\n"
                                        "6- la altura promedio de los superhéroes de género M\n"
                                        "7- salir\n"
                                        "8- el superhéroe más bajo de género M \n"
                                        "9- el superhéroe más bajo de género F\n"
                                        "10- la altura promedio de los superhéroes de género M\n\nIngrese un número: ")
        

    if opcion_elegida_por_usuario == "1":
        print("Nombre Jugador - Posición:\n")
        print(jugadores_con_posicion(lista_auxiliar))
    elif opcion_elegida_por_usuario == "2":
        print(indice_jugadores(lista_auxiliar))
        print(estadisticas_completas(lista_auxiliar))
    elif opcion_elegida_por_usuario == "3":
        exportar_csv(estadisticas_completas(lista_auxiliar), "jugadores.csv")
    elif opcion_elegida_por_usuario == "4":
        print(indice_jugadores(lista_auxiliar))
        print(mostrar_logros(lista_auxiliar))
    elif opcion_elegida_por_usuario == "5":
        print(f"El promedio de puntos por partido de todo el equipo del Dream Team es: {calcular_promedio(lista_auxiliar)}")
    elif opcion_elegida_por_usuario == "6":
        print(indice_jugadores(lista_auxiliar))
        print(miembro_salon_fama(lista_auxiliar))
    elif opcion_elegida_por_usuario == "7":
        print(jugador_mas_rebotes_totales(lista_auxiliar))
    elif opcion_elegida_por_usuario == "8":
        print(jugador_mayor_porcentaje_tiros(lista_auxiliar))
    else:
        print("Opción no válida\nIngrese la opcion correcta")

opciones_menu(lista_auxiliar)





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

    
    return '\n'.join(lista_jugadores_posicion)

    




    
def indice_jugadores(lista_auxiliar: list) -> str:
    lista_jugadores = []
    for i in range(len(lista_auxiliar)):
        nombre = lista_auxiliar[i]["nombre"]
        lista_jugadores.append(f"{i+1}- {nombre}")
    return '\n'.join(lista_jugadores)


#Permitir al usuario seleccionar un jugador por su índice y
# mostrar sus estadísticas completas, incluyendo temporadas jugadas,
# puntos totales, promedio de puntos por partido, rebotes totales,
# promedio de rebotes por partido, asistencias totales, promedio de asistencias por partido,
# robos totales, bloqueos totales, porcentaje de tiros de campo, porcentaje de tiros libres y
# porcentaje de tiros triples.

def estadisticas_completas_csv(lista_auxiliar: list, indice_seleccionado: int, nombre_archivo: str):
    if indice_seleccionado <= 0 or indice_seleccionado > len(lista_auxiliar):
        return "Opcion no valida"
    else:
        jugador = lista_auxiliar[indice_seleccionado - 1]
        nombre = jugador["nombre"]
        posicion = jugador["posicion"]
        estadisticas = jugador["estadisticas"]
        jugador_con_estadisticas = f"{nombre}: {estadisticas}"

    with open(nombre_archivo, "w") as archivo:
        linea = "{0},{1},{2}\n"
        linea = linea.format(nombre, posicion, str(estadisticas))
        archivo.write(linea)

    return jugador_con_estadisticas







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
        
    


def calcular_y_mostrar(lista_auxiliar:list,opcion:str):
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

def calcular_y_mostrar_promedio(lista_auxiliar:list,opcion:str):
    lista_aux = []
    lista_aux_sin_min = []
    
    for jugador in lista_auxiliar:
        estadistica = jugador["estadisticas"][opcion]
        lista_aux.append(estadistica)

    menor = min(lista_aux)
    for estadistica in lista_aux:
        if estadistica != menor:
            lista_aux_sin_min.append(estadistica)
    
    promedio_sin_min = sum(lista_aux_sin_min) / len(lista_aux_sin_min)

    mensaje = f"el promedio de puntos por partido del equipo excluyendo al jugador con menos promedio es: {promedio_sin_min}"

    return mensaje


# 17)Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos


def calcular_y_mostrar_mayor_logros(lista_auxiliar:list):
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




def jugadores_promedio_porcentaje_mayor(lista_auxiliar:list,valor_ingresado,opcion:str):
    lista_jugadores_mayor = []
    for jugador in lista_auxiliar:
        if jugador["estadisticas"][opcion] > valor_ingresado:
            nombre = jugador["nombre"]
            estadistica = jugador["estadisticas"][opcion]
            lista_jugadores_mayor.append(f"{nombre} - {estadistica}")
    
    if len(lista_jugadores_mayor) == 0:
        return "No hay jugadores"
    
    return "\n".join(lista_jugadores_mayor)


#20) Permitir al usuario ingresar un valor y mostrar los jugadores
#ordenados por posición en la cancha, que hayan tenido un porcentaje
#  de tiros de campo superior a ese valor.

            
def jugadores_ordenados_porcentaje_tiros(lista_auxiliar,valor_porcentaje):
    

    # Filtrar los jugadores con un porcentaje de tiros de campo superior al valor ingresado
    jugadores_mayor_porcentaje = []

    for jugador in lista_auxiliar:
        if jugador["estadisticas"]["porcentaje_tiros_de_campo"] > valor_porcentaje:
            jugadores_mayor_porcentaje.append(jugador)
            

    # Imprimir los jugadores filtrados en orden de posición en la cancha
    posiciones = ["Base", "Escolta", "Alero", "Ala-Pívot", "Pívot"]

    for posicion in posiciones:
        for jugador in jugadores_mayor_porcentaje:
            if jugador["posicion"] == posicion:
                print(f"Nombre: {jugador['nombre']}")
                print(f"Posición: {jugador['posicion']}")
                print(f"Porcentaje de tiros de campo: {jugador['estadisticas']['porcentaje_tiros_de_campo']}%")
                print("---------------------")





        

     

    



    

    

#Permitir al usuario buscar un jugador por su nombre y mostrar sus logros, como campeonatos de la NBA, participaciones en el All-Star y pertenencia al Salón de la Fama del Baloncesto, etc.
#Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre de manera ascendente. 

def opciones_menu(lista_auxiliar):
    """
    Esta función muestra el menu, le permite al usuario
    ingresar una opcion e imprime por consola
    la opcion elegida
    """
    
    opcion_elegida_por_usuario = input("\n\n1- Mostrar lista de jugadores del Dream Team\n"
                        "2- Seleccionar un jugador por su indice y mostrar sus estadisticas completas,luego guarda toda la informacion de ese jugador en un archivo CSV\n"
                        "3- -\n"
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
        resultado = estadisticas_completas_csv(lista_auxiliar, indice_seleccionado, "jugador_exportad.csv")
        if resultado == "Opcion no valida":
            print("Opcion no valida")
        else:
            print(f"Jugador seleccionado: {resultado}")
    elif opcion_elegida_por_usuario == "3":
        pass
    elif opcion_elegida_por_usuario == "4":
        print(indice_jugadores(lista_auxiliar))
        print(mostrar_logros(lista_auxiliar))
    elif opcion_elegida_por_usuario == "5":
        print(f"El promedio de puntos por partido de todo el equipo del Dream Team es: {calcular_promedio(lista_auxiliar)}")
    elif opcion_elegida_por_usuario == "6":
        print(indice_jugadores(lista_auxiliar))
        print(miembro_salon_fama(lista_auxiliar))
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





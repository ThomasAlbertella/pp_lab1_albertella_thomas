import re
import json

def parse_json(nombre_archivo:str)->list:
    """
    esta funcion recibe la ubicacion del archivo json
    crea un diccionario
    abre el archivo y le carga todos lo datos
    
    """
    dic_json = {}
    with open(nombre_archivo, "r") as archivo:
        dic_json = json.load(archivo)

    return dic_json["juegos"]

lista_juegos = parse_json("data_pp.json")
lista_auxiliar = lista_juegos[:]
from pymongo import MongoClient
import requests
from dotenv import load_dotenv
import os
import pandas as pd
import geopandas as gpd
from cartoframes.viz import Map, Layer, popup_element
from functools import reduce
import operator
import json

def geocode(direccion):
    """
    This function gets the coordinates of a given direction.
    Argg: the direction.
    Returns: the coordinates.
    """
    data = requests.get(f"https://geocode.xyz/{direccion}?json=1").json()
    try:
        return {"type": "Point", "coordinates": [data["latt"], data["longt"]]}
    except:
        return data

def getFromDict(diccionario,mapa):
    return reduce(operator.getitem,mapa,diccionario)

def extraetodo(json):
    """
    This function gets name, latitud and longitud of a givn json with data.
    Argg: the json.
    Returns: a list with th given data.
    """
    todo = {"nombre": ["name"], "latitud": ["location", "lat"], "longitud": ["location", "lng"]} 
    total = []
    for elemento in json:
        place = {key: getFromDict(elemento, value) for key,value in todo.items()}
        place["location"] = type_point([place["latitud"], place["longitud"]])
        total.append(place)
    return total

def type_point(lista):
    """
    This function gets one list.
    Argg: a list.
    Returns: a type point.
    """
    return {"type":"Point", "coordinates": lista}


def places_cities(place, city):
    """
    This function returns a final json where all the latter functions are combined.
    Argg: the place and a city to be searched.
    Returns: a json.
    """
    url_query = 'https://api.foursquare.com/v2/venues/search'
    url_recomendados = 'https://api.foursquare.com/v2/venues/explore'
    client_id = os.getenv("tok1")
    client_secret = os.getenv("tok2")
    parametros = {
        "client_id": client_id,
        "client_secret": client_secret,
        "v": "20180323",
        "ll": f"{city['coordinates'][0]}, {city['coordinates'][1]}", #aquí pongo la ciudad que quiero
        "query": f"{place}" #aquí pongo lo que quiero buscar en la ciudad.
}
    resp = requests.get(url_query, params = parametros).json()
    map_ = ["location", "lat"]
    getFromDict(resp["response"]["venues"][0], map_)
    resp["response"]["venues"][0]["location"]["address"]
    loquebusco = resp["response"]["venues"]
    
    return extraetodo(loquebusco)

def build_df(lovemosclaro:dict):
    """
    This function builds a dataframe.
    Argg: a json.
    Returns: a dataframe.
    """
    return pd.DataFrame(lovemosclaro)

def build_json(place,city,lovemosclaro:dict):
    """
    This function exports a json.
    Argg: a place, a city, and a json.
    Returns: json file in a given directory.
    """
    json_name = f'{place}_{city}.json'    
    with open (json_name,"w") as f: # creamos un archivo vacío en el que vamos a escribir
        json.dump(lovemosclaro,f) # cargamos nuestra lista de diccionarios en ese archivo

def visualize():
    """
    This function creates a map.
    Argg: needs the same arguments givn in the place_cities()function.
    Returns: map with all points given represented.
    """
    search_point = places_cities(place, city)
    gdf = gpd.GeoDataFrame(search_point, geometry=gpd.points_from_xy(search_point.longitud, search_point.latitud))
    return Map(Layer(gdf, "color:purple", popup_hover=[popup_element("nombre", f"{place} in {city}")]))
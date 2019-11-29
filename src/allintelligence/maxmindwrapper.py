import requests
import json
from config import MAXMIND_USER_API, MAXMIND_API_KEY

"""
Módulo de MaxMind para obtener geolocalización IP.

__author__: AllPentesting
"""

def petition(ip):
    """
    Función encargada de realizar una petición a MaxMind
    Parametros:
        - ip: IP de la cual obtener geolocalización
    """
    response = requests.get('https://geoip.maxmind.com/geoip/v2.1/insights/'+ip, auth=requests.auth.HTTPBasicAuth(MAXMIND_USER_API,MAXMIND_API_KEY), headers={'Accept':'application/json'})
    try:
        return __parser(response.json())

    except Exception:
        return {"error":"Error with MaxMind"}

def __parser(geolocation):
    """
    Función encargada de interpretar el json obtenido mediante requests 
    y devuelve un diccionario con la información de geolocalización.
    Parametros:
        - geolocation: JSON que nos proporciona MaxMind con la información de geolocalización
    """
    try:
        dict_geo = {"city":{},"continent":{},"country":{},"location":{}}
        if "city" in geolocation:
            if "confidence" in geolocation["city"]:
                dict_geo["city"].update({"confidence":geolocation["city"]["confidence"]})
            if "names" in geolocation["city"]:
                dict_geo["city"].update({"name":geolocation["city"]["names"]["en"]})

        if "continent" in geolocation:
            if "code" in geolocation["continent"]:
                dict_geo["continent"].update({"code":geolocation["continent"]["code"]})
            if "names" in geolocation["continent"]:
                dict_geo["continent"].update({"name":geolocation["continent"]["names"]["en"]})
        
        if "country" in geolocation:
            if "confidence" in geolocation["continent"]:
                dict_geo["country"].update({"confidence":geolocation["country"]["confidence"]})
            if "names" in geolocation["continent"]:
                dict_geo["country"].update({"name":geolocation["country"]["names"]["en"]})

        if "location" in geolocation:
            if "accuracy_radius" in geolocation["location"]:
                dict_geo["location"].update({"accuracy_radius":geolocation["location"]["accuracy_radius"]})

            if "latitude" in geolocation["location"]:
                dict_geo["location"].update({"latitude":geolocation["location"]["latitude"]})

            if "longitude" in geolocation["location"]:
                dict_geo["location"].update({"longitude":geolocation["location"]["longitude"]})
            
            if "time_zone" in geolocation["location"]:
                dict_geo["location"].update({"time_zone":geolocation["location"]["time_zone"]})


        return dict_geo

    except Exception:
        return {"error":"Error"}
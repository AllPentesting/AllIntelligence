import requests
import json
from config import DEHASHED_API_KEY, DEHASHED_USER_API

"""
Módulo de dehashed para obtener leaks.

__author__: AllPentesting
"""

def petition(email):
    """
    Función encargada de realizar una petición a dehashed
    Parametros:
        - email: Correo de la persona que se quieren obtener fugas de información
    """
    response = requests.get('https://dehashed.com/search?query=\'"'+email+'"\'', auth=requests.auth.HTTPBasicAuth(DEHASHED_USER_API,DEHASHED_API_KEY), headers={'Accept':'application/json'})
    try:
        return __parser(response.json())

    except Exception:
        return {"error":"Error with Dehashed"}

def __parser(leaks):
    """
    Función encargada de interpretar el json obtenido mediante requests y devuelve un diccionario con los leaks.
    Parametros:
        - leaks: JSON que nos proporciona dehashed
    """
    try:
        #dict_leaks = {}
        array_leaks = []
        #Accedemos a la key entries donde se encuentra la información de los leaks
        for leak in leaks["entries"]:
            #Vamos añadiendo al array los leaks
            array_leaks.append({"email":leak["email"],"username":leak["username"],"password":leak["password"],"hashed_password":leak["hashed_password"],"name":leak["name"],"address":leak["address"],"ip_address":leak["ip_address"],"phone":leak["phone"],"breach":leak["obtained_from"]})
        #Agregamos al diccionario la key leaks con el array de los leaks
        #dict_leaks.update(array_leaks)
        return array_leaks

    except Exception:
        #Si las credenciales son inválidas te devolverá un JSON con la key success que será False
        if(leaks["success"] == False):
            return {"error":"Invalid credentials"}
        return {"error":"Leaks not found"}
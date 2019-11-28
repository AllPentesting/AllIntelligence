import requests
import json
import pyhunter
from allintelligence.config import HUNTER_API_KEY

"""
Módulo de hunter.io para obtener correos de una organización.

__author__: AllPentesting
"""

def petition(domain):
    """
    Función encargada de realizar una petición a hunter.io.
    """

    response = requests.get("https://api.hunter.io/v2/domain-search?domain="+str(domain)+"&limit=20&api_key="+HUNTER_API_KEY)
    return __parser(response.json())

def __parser(emails):
    """
    Función encargada de interpretar el json obtenido mediante requests y devuelve un diccionario con los correos.
    Parametros:
        - emails: JSON que nos proporciona hunter.io
    """
    try:
        dict_mails = {}
        dict_mails.update({"organization":emails["data"]["organization"]})
        array_mails = []
        #Accedemos al array de emails
        for email in emails["data"]["emails"]:
            #Creamos el diccionario del email
            dict_mail = {"email" : email["value"], "type":email["type"],"confidence":email["confidence"],"first_name":email["first_name"],"last_name":email["last_name"],"position":email["position"],"seniority":email["seniority"],"department":email["department"],"linkedin":email["linkedin"],"twitter":email["twitter"],"phone_number":email["phone_number"]}
            sources = []
            #Accedemos a las fuentes desde donde se ha obtenido la información de ese correo
            for source in email["sources"]:
                sources.append(source["uri"])
            dict_mail.update({"sources":sources})
            #Agregamos al array de correos el nuevo correo analizado
            array_mails.append(dict_mail)
        #Una vez recorridos todos los correos añadimos al diccionario el array con los diferentes correos
        dict_mails.update({"emails":array_mails})
        return dict_mails
    except Exception:
        return {"error":emails["errors"][0]["details"]}
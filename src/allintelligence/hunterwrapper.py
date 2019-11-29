import requests
import json
import pyhunter
from config import HUNTER_API_KEY

"""
Módulo de hunter.io para obtener correos de una organización.

__author__: AllPentesting
"""

def petition(domain):
    """
    Función encargada de realizar una petición a hunter.io.
    Parametros:
        - domain: Dominio de el que se van a obtener correos.
    """

    response = requests.get("https://api.hunter.io/v2/domain-search?domain="+domain+"&limit=20&api_key="+HUNTER_API_KEY)
    try:
        return __parser(response.json())
    except Exception:
        return {"error":"Error with Hunter"}


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
            dict_mail = {"email" : [], "type": None,"confidence": None,"first_name": None,"last_name": None,"position": None,"seniority":None,"department":None,"linkedin":None,"twitter":None,"phone_number":[]}
            
            if(email["value"] != []):
                dict_mail.update({"email" : [email["value"]]})
            
            if(email["type"] != None):
                dict_mail.update({"type": email["type"]})
            
            if(email["confidence"] != None):
                dict_mail.update({"confidence": email["confidence"]})
            
            if(email["first_name"] != None):
                dict_mail.update({"first_name": [email["first_name"]]})
            
            if(email["last_name"] != None):
                dict_mail.update({"last_name": [email["last_name"]]})
            
            if(email["position"] != None):
                dict_mail.update({"position": email["position"]})
            
            if(email["seniority"] != None):
                dict_mail.update({"seniority": email["seniority"]})
            
            if(email["department"] != None):
                dict_mail.update({"department": email["department"]})

            if(email["linkedin"] != None):
                dict_mail.update({"linkedin": [email["linkedin"]]})
            
            if(email["twitter"] != None):
                dict_mail.update({"twitter":[email["twitter"]]})
            
            if(email["phone_number"] != None):
                dict_mail.update({"phone_number":[email["phone_number"]]})


            
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
import requests
from allintelligence.config import PIPL_API_KEY

"""
Módulo de interconexión con la API de Pipl para obtener información sobre las identidades digitales a partir de un email

__author__:AllPentesting
"""


def petition(email):
    """
    Función que concecta con la API Pipl y nos devuelve una serie de información a partir de de un email que se le pasa
    Parametros:
        - email: correo de la persona que buscamos información

    """
    response = requests.get("https://api.pipl.com/search/?email="+email+"&key="+PIPL_API_KEY)

    return __parser(response.json())


def __parser(info_pipl):    
    """
    Función encargada de interpretar el json obtenido mediante requests y devuelve un diccionario con los datos de Pypl.
    Parametros:
        - info_pipl: JSON que nos proporciona pipl
    """
    try:
        #Diccionario principal con toda la información de pipl
        dict_pipl = {}


        array_usernames = []

        for username in info_pipl["person"].get("usernames",None):
            array_usernames.append(username["content"])

        #Añadimos el array de usernames al diccionario principal de Pipl
        dict_pipl.update({"usernames":array_usernames})


        array_emails = []

        for email in info_pipl["person"].get("emails", None):
            array_emails.append(email["address"])

        #Añadimos el diccionario de emails al diccionario principal de Pipl
        dict_pipl.update({"emails":array_emails})


        array_addresses = []

        for address in info_pipl["person"].get("addresses", None):
            array_addresses.append(address["display"])

        #Añadimos el array de addresses al diccionario principal de Pipl
        dict_pipl.update({"addresses":array_addresses})


        array_phones = []

        for phone in info_pipl["person"].get("phones", None):
            array_phones.append(phone["display_international"])

        #Añadimos el array de phones al diccionario principal de Pipl
        dict_pipl.update({"phones":array_phones})


        array_jobs = []

        for job in info_pipl["person"].get("jobs", None):
            array_jobs.append(job["display"])

        #Añadimos el array de jobs al diccionario principal de Pipl
        dict_pipl.update({"jobs":array_jobs})


        dict_images = []

        for img in info_pipl["person"].get("images", None):
            check_image = requests.get(img["url"])
            if check_image.status_code == 200:
                dict_images.append({
                    "@last_seen": img["@last_seen"],
                    "url":img["url"]
                })

        #Añadimos el diccionario de images al diccionario principal de Pipl
        dict_pipl.update({"images":dict_images})


        dict_urls = []

        for url in info_pipl["person"].get("urls", None):
            dict_urls = {
                "@category": url.get("@category",None),
                "url": url["url"]
            }

        #Añadimos el diccionario de urls al diccionario principal de Pipl
        dict_pipl.update({"urls":dict_urls})

        return dict_pipl
    except Exception:
        return {"error":info_pipl["@http_status_code"]}
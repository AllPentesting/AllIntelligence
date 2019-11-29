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
        for username in info_pipl["person"].get("usernames",[]):
            array_usernames.append(username.get("content", None))
        array_usernames = list(filter(None.__ne__, array_usernames))
        if(len(array_usernames) == 0):
            array_usernames = []

        #Añadimos el array de usernames al diccionario principal de Pipl
        dict_pipl.update({"usernames":array_usernames})


        array_emails = []

        for email in info_pipl["person"].get("emails", []):
            array_emails.append(email.get("address", None))
        
        array_emails = list(filter(None.__ne__, array_emails))
        if(len(array_emails) == 0):
            array_emails = []
            
        #Añadimos el diccionario de emails al diccionario principal de Pipl
        dict_pipl.update({"emails":array_emails})


        array_addresses = []

        for address in info_pipl["person"].get("addresses", []):
            array_addresses.append(address.get("display", None))

        array_addresses = list(filter(None.__ne__, array_addresses))
        if(len(array_addresses) == 0):
            array_addresses = []

        #Añadimos el array de addresses al diccionario principal de Pipl
        dict_pipl.update({"addresses":array_addresses})


        array_phones = []

        for phone in info_pipl["person"].get("phones", []):
            array_phones.append(phone.get("display_international", None))

        array_phones = list(filter(None.__ne__, array_phones))
        if(len(array_phones) == 0):
            array_phones = []

        #Añadimos el array de phones al diccionario principal de Pipl
        dict_pipl.update({"phones":array_phones})


        array_jobs = []

        for job in info_pipl["person"].get("jobs", []):
            array_jobs.append(job.get("display", None))
        array_jobs = list(filter(None.__ne__, array_jobs))
        if(len(array_jobs) == 0):
            array_jobs = []

        #Añadimos el array de jobs al diccionario principal de Pipl
        dict_pipl.update({"jobs":array_jobs})


        dict_images = []

        for img in info_pipl["person"].get("images", []):
            image = img.get("urls", None)
            if(image != None):
                check_image = requests.get(image)
                if check_image.status_code == 200:
                    dict_images.append({
                        "@last_seen": img.get("@last_seen", None),
                        "url":img.get("urls", None)
                })

        #Añadimos el diccionario de images al diccionario principal de Pipl
        dict_pipl.update({"images":dict_images})

        array_urls = []

        for url in info_pipl["person"].get("urls", {}):
            array_urls.append({
                "@category": url.get("@category",None),
                "url": url.get("url", None)
            })

        array_urls = list(filter(None.__ne__, array_urls))
        if(len(array_urls) == 0):
            array_urls = []

        #Añadimos el diccionario de urls al diccionario principal de Pipl
        dict_pipl.update({"urls":array_urls})

        return dict_pipl
    except Exception:
        print(info_pipl)
        return {"error":info_pipl["@http_status_code"]}
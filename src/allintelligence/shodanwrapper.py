import shodan
from config import SHODAN_API_KEY
"""
Módulo de interconexión con la API de Shodan para obtener información de shodan a parti de una IP

__author__:AllPentesting
"""
 
def gethost(ip):
    """
    Función que concecta con la API Shodan y nos devuelve una serie de información en un diccionario
    Parametros:
        - ip: dirección ip del dominio a consultar

    La información que devueleve es: ASN, ISP, City, Latitude, Longitude, Country, Organization, Array de Hostnames,Array de ports,Array de vulns y Arrays de datos
    como información del CVE, CVSS, si está verificado o información y enlaces de la vulnerabilidad

    """
    api = shodan.Shodan(SHODAN_API_KEY)

    host_info = api.host(ip)
    
        
    #Diccionario principal con toda la información de shodan
    dict_shodan = {}

    #Comprobamos si existe cada una de las keys y sino le asignamos None para que no de fallo en caso de acceso 
    if "ip_str" in host_info:
        dict_shodan.update({"ip":host_info['ip_str']})
    else:
        dict_shodan.update({"ip": None})
    

    if "asn" in host_info:
        dict_shodan.update({"asn":host_info['asn']})
    else:
        dict_shodan.update({"asn": None})

    if "isp" in host_info:
        dict_shodan.update({"isp":host_info['isp']})
    else:
        dict_shodan.update({"isp": None})

    if "city" in host_info:
        dict_shodan.update({"city":host_info['city']})
    else:
        dict_shodan.update({"city": None})

    if "latitude" in host_info:
        dict_shodan.update({"latitude":host_info['latitude']})
    else:
        dict_shodan.update({"latitude": None})

    if "longitude" in host_info:
        dict_shodan.update({"longitude":host_info['longitude']})
    else:
        dict_shodan.update({"longitude": None})

    if "country_name" in host_info:
        dict_shodan.update({"country_name":host_info['country_name']})
    else:
        dict_shodan.update({"country_name": None})

    if "org" in host_info:
        dict_shodan.update({"org":host_info['org']})
    else:
        dict_shodan.update({"org": None})

    if "last_update" in host_info:
        dict_shodan.update({"last_update":host_info['last_update']})
    else:
        dict_shodan.update({"last_update": None})
    
    if "hostnames" in host_info:
        dict_shodan.update({"hostnames":host_info['hostnames']})
    else:
        dict_shodan.update({"hostnames": None})

    if "ports" in host_info:
        dict_shodan.update({"ports":host_info['ports']})
    else:
        dict_shodan.update({"ports": None})

    if "vulns" in host_info:
        dict_shodan.update({"vulns":host_info['vulns']})
    else:
        dict_shodan.update({"vulns": None})

    if "data" in host_info:
        dict_shodan.update({"data":host_info['data']})
    else:
        dict_shodan.update({"data": None})

    return dict_shodan



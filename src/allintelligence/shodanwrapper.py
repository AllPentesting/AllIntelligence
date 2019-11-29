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
    #print (host_info['vulns'])

    return {
        'ip': host_info['ip_str'],
        'asn': host_info['asn'],
        'isp': host_info['isp'],
        'city': host_info['city'],
        'latitude': host_info['latitude'],
        'longitude': host_info['longitude'],
        'country_name': host_info['country_name'],
        'org': host_info['org'],
        'last_update': host_info['last_update'],  
        'hostnames': host_info['hostnames'],
        'ports': host_info['ports'],
        'vulns': host_info['vulns'],
        'data': host_info['data']
    
    }

gethost("150.214.110.200")
import shodan
from allintelligence.config import SHODAN_API_KEY
"""
Shodan module to obtain information about an IP

__author__:AllPentesting
"""
 
def gethost(ip):
    """
    Function that contracts with the Shodan API and returns a series of information in a dictionary
    Parameters:
        - ip: ip address of the domain to consult

    The information you return is: ASN, ISP, City, Latitude, Longitude, Country, Organization, Hostnames Array, Port Array, Vulnerability and Data Array
    such as CVE information, CVSS, if verified or information and links of the vulnerability

    """
    api = shodan.Shodan(SHODAN_API_KEY)

    host_info = api.host(ip)
    
        
    # Main dictionary with all the shodan information
    dict_shodan = {}

    # We check if each one of the keys exists and if not assign it None so that it does not fail in case of access
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



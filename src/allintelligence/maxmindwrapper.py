import requests
from allintelligence.config import MAXMIND_USER_API, MAXMIND_API_KEY

"""
MaxMind module to obtain IP geolocation.

__author__: AllPentesting
"""

def petition(ip):
    """
    Function responsible for making a request to MaxMind
    
    Parameters:
        - ip: IP from which to obtain geolocation
    """
    response = requests.get('https://geoip.maxmind.com/geoip/v2.1/insights/'+ip, auth=requests.auth.HTTPBasicAuth(MAXMIND_USER_API,MAXMIND_API_KEY), headers={'Accept':'application/json'})
    try:
        return __parser(response.json())

    except Exception:
        return {"error":"Error with MaxMind"}

def __parser(geolocation):
    """
    Function responsible for interpreting the json obtained through requests
    and returns a dictionary with the geolocation information.

    Parameters:
        - geolocation: JSON provided by MaxMind with geolocation information
    """
    try:
        # Add city information
        dict_geo = {"city":{},"continent":{},"country":{},"location":{}}
        if "city" in geolocation:
            if "confidence" in geolocation["city"]:
                dict_geo["city"].update({"confidence":geolocation["city"]["confidence"]})
            if "names" in geolocation["city"]:
                dict_geo["city"].update({"name":geolocation["city"]["names"]["en"]})

        # Add continent information
        if "continent" in geolocation:
            if "code" in geolocation["continent"]:
                dict_geo["continent"].update({"code":geolocation["continent"]["code"]})
            if "names" in geolocation["continent"]:
                dict_geo["continent"].update({"name":geolocation["continent"]["names"]["en"]})
        
        # Add country information
        if "country" in geolocation:
            if "confidence" in geolocation["continent"]:
                dict_geo["country"].update({"confidence":geolocation["country"]["confidence"]})
            if "names" in geolocation["continent"]:
                dict_geo["country"].update({"name":geolocation["country"]["names"]["en"]})

        # Add location information
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
        return {"error":"Error with MaxMind Keys"}
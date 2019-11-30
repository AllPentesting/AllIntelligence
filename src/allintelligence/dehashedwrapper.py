import requests
from allintelligence.config import DEHASHED_API_KEY, DEHASHED_USER_API

"""
Dehashed module to obtain leaks.

__author__: AllPentesting
"""

def petition(email):
    """
    Function responsible for making a request to dehashed
    Parameters:
        - email: Mail of the person who wants to get information leaks
    """
    response = requests.get('https://dehashed.com/search?query=\'"'+email+'"\'', auth=requests.auth.HTTPBasicAuth(DEHASHED_USER_API,DEHASHED_API_KEY), headers={'Accept':'application/json'})
    try:
        return __parser(response.json())

    except Exception:
        return {"error":"Error with Dehashed"}

def __parser(leaks):
    """
    Function responsible for interpreting the json obtained through requests and returns a dictionary with the leaks.
    Parameters:
        - leaks: JSON que nos proporciona dehashed
    """
    try:
        array_leaks = []
        # We access the key entries where the leaks information is located
        for leak in leaks["entries"]:
            # We are adding the leaks to the array
            array_leaks.append({"email":leak["email"],"username":leak["username"],"password":leak["password"],"hashed_password":leak["hashed_password"],"name":leak["name"],"address":leak["address"],"ip_address":leak["ip_address"],"phone":leak["phone"],"breach":leak["obtained_from"]})
        return array_leaks

    except Exception:
        # If the credentials are invalid, it will return a JSON with the key success that will be "False"
        if(leaks["success"] == False):
            return {"error":"Invalid credentials"}
        return {"error":"Leaks not found"}
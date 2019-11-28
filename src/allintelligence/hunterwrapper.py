import requests
import json
import pyhunter
from config import HUNTER_API_KEY

def petition(domain):
    response = requests.get("https://api.hunter.io/v2/domain-search?domain="+domain+"&limit=20&api_key="+HUNTER_API_KEY)
    return __parser(response.json())

def __parser(emails):
    dict_mails = {}
    dict_mails.update({"organization":emails["data"]["organization"]})
    array_mails = []
    for email in emails["data"]["emails"]:
        dict_mail = {"email" : email["value"], "type":email["type"],"confidence":email["confidence"],"first_name":email["first_name"],"last_name":email["last_name"],"position":email["position"],"seniority":email["seniority"],"department":email["department"],"linkedin":email["linkedin"],"twitter":email["twitter"],"phone_number":email["phone_number"]}
        sources = []
        for source in email["sources"]:
            sources.append(source["uri"])
        dict_mail.update({"sources":sources})
        array_mails.append(dict_mail)
    dict_mails.update({"emails":array_mails})
    return dict_mails
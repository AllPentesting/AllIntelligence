import requests
from allintelligence.config import PIPL_API_KEY

"""
Pipl module to obtain information about a person from an email

__author__:AllPentesting
"""


def petition(email):
    """
    Function that contracts with the API Pipl and returns a series of information from an email that is passed
    Parameters:
        - email: mail of the person we are looking for information
    """
    response = requests.get("https://api.pipl.com/search/?email="+email+"&key="+PIPL_API_KEY)
    return __parser(response.json())

def __parser(info_pipl):    
    """
    Function responsible for interpreting the json obtained through requests and returns a dictionary with Pypl data.
    Parameters:
        - info_pipl: JSON that gives us pipl
    """
    try:
        # Main dictionary with all the pipl information
        dict_pipl = {}

        array_usernames = []
        for username in info_pipl["person"].get("usernames",[]):
            array_usernames.append(username.get("content", None))
        array_usernames = list(filter(None.__ne__, array_usernames))
        if(len(array_usernames) == 0):
            array_usernames = []

        # We add the array of usernames to the main Pipl dictionary
        dict_pipl.update({"usernames":array_usernames})


        array_emails = []

        for email in info_pipl["person"].get("emails", []):
            array_emails.append(email.get("address", None))
        
        array_emails = list(filter(None.__ne__, array_emails))
        if(len(array_emails) == 0):
            array_emails = []
            
        # We add the email dictionary to the main Pipl dictionary
        dict_pipl.update({"emails":array_emails})


        array_addresses = []

        for address in info_pipl["person"].get("addresses", []):
            array_addresses.append(address.get("display", None))

        array_addresses = list(filter(None.__ne__, array_addresses))
        if(len(array_addresses) == 0):
            array_addresses = []

        # We add the array of addresses to the main Pipl dictionary
        dict_pipl.update({"addresses":array_addresses})


        array_phones = []

        for phone in info_pipl["person"].get("phones", []):
            array_phones.append(phone.get("display_international", None))

        array_phones = list(filter(None.__ne__, array_phones))
        if(len(array_phones) == 0):
            array_phones = []

        # We add the array of phones to the main Pipl dictionary
        dict_pipl.update({"phones":array_phones})


        array_jobs = []

        for job in info_pipl["person"].get("jobs", []):
            array_jobs.append(job.get("display", None))
        array_jobs = list(filter(None.__ne__, array_jobs))
        if(len(array_jobs) == 0):
            array_jobs = []

        # We add the array of jobs to the main Pipl dictionary
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

        # We add the images dictionary to the main Pipl dictionary
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

        # We add the urls dictionary to the main Pipl dictionary
        dict_pipl.update({"urls":array_urls})

        return dict_pipl
    except Exception:
        print(info_pipl)
        return {"error":info_pipl["@http_status_code"]}
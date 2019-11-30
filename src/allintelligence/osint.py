from allintelligence import hunterwrapper, dehashedwrapper, piplwrapper

"""
Osint Module that generates the emails dictionary
by performing different things:
    - Hunter API
    - Dehashed API
    - Pipl API

__author__: AllPentesting
"""

def analyze(domain, config):
    """
    Analysis function that launchers other modules.
    Parameters:
        - domain: Domain to do the analysis
        - config: Configuration to activate o desactivate module
    """

    #Check if Hunter is checked
    if(config['hunter'] != False):
        dict_emails = hunterwrapper.petition(domain)

        i=0
        for emails in dict_emails["emails"]:
            dict_emails["emails"][i].update({"passwords":[],"usernames":[],"ips":[],"addresses":[], "jobs":[],"images":[]})
            i = i+1
        i=0

        #Check if Pipl is checked
        if(config['pipl'] != False):
            for emails in dict_emails["emails"]:
                
                for email in dict_emails["emails"][i]["email"]:
                    print(email)

                    if("@mail.com" not in email):
                        pipl = piplwrapper.petition(email)
                        if "emails" in pipl:
                            # Add new emails to array 
                            for email in pipl["emails"]:
                                if email not in dict_emails["emails"][i]["email"]:
                                    dict_emails["emails"][i]["email"].append(email)

                        # We add the other new fields found in PIPL
                        if "usernames" in pipl: 
                            for username in pipl["usernames"]:
                                if username not in dict_emails["emails"][i]["usernames"]:
                                    dict_emails["emails"][i]["usernames"].append(username)
                        
                        if "addresses" in pipl: 
                            for address in pipl["addresses"]:
                                if address not in dict_emails["emails"][i]["addresses"]:
                                    dict_emails["emails"][i]["addresses"].append(address)

                        if "phones" in pipl:
                            for phone in pipl["phones"]:
                                if phone not in dict_emails["emails"][i]["phone_number"]:
                                    dict_emails["emails"][i]["phone_number"].append(phone)

                        if "job" in pipl:
                            for job in pipl["jobs"]:
                                if job not in dict_emails["emails"][i]["jobs"]:
                                    dict_emails["emails"][i]["jobs"].append(job)

                        if "images" in pipl:
                            for image in pipl["images"]:
                                if image not in dict_emails["emails"][i]["images"]:
                                    dict_emails["emails"][i]["images"].append(image)
                        
                        if "urls" in pipl:
                            for url in pipl["urls"]:
                                if url not in dict_emails["emails"][i]["sources"]:
                                    dict_emails["emails"][i]["sources"] = dict_emails["emails"][i]["sources"] + url
                i=i+1

        # Check if Dehashed is checked
        if(config['dehashed'] != False):
            i = 0
            # We now recover all emails from that person found with Hunter and / or PIPL 
            for email_list in dict_emails["emails"]:
                for email in email_list['email']:
                    dehashed = dehashedwrapper.petition(email)
                    #Go adding the info to the main dictionary
                    for leak in dehashed:
                        if "username" in leak:
                            if leak["username"] is None:
                                dict_emails["emails"][i]["usernames"].append(leak["username"])
                            if leak["phone"] is None:
                                dict_emails["emails"][i]["phone_number"].append(leak["phone"])
                        
                        if "password" in leak:
                            if leak["password"] is None:
                                dict_emails["emails"][i]["passwords"].append({"password": leak["password"], "hash": leak["hashed_password"] ,"origin": leak["breach"]})
                        
                        if "address" in leak:
                            if leak["address"] is None:
                                dict_emails["emails"][i]["addresses"].append({leak["address"]})
                        
                        if "ip_address" in leak:
                            if leak["ip_address"] is None:
                                dict_emails["emails"][i]["ips"].append({leak["ip_address"]})
                i = i + 1

    else:
        dict_emails = {"error": "OSINT module not active"}

    return dict_emails


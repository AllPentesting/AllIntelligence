from allintelligence import hunterwrapper, dehashedwrapper, piplwrapper

def analyze(domain, config):

    # Primera información
    if(config['hunter'] != False):
        dict_emails = hunterwrapper.petition(domain)


        # To-Do: optimize 
        i=0
        for emails in dict_emails["emails"]:
            #Añadimos nuevas keys al diccionario para pipl y dehashed
            dict_emails["emails"][i].update({"passwords":[],"usernames":[],"ips":[],"addresses":[], "jobs":[],"images":[]})

            #Ejecutamos pipl
            if(config['pipl'] != False):
                for email in dict_emails["emails"][i]["email"]:
                    if("@mail.com" not in email):
                        pipl = piplwrapper.petition(email)
                        #Añadimos los nuevos correos encontrados relacionados con esa persona
                        for email in pipl["emails"]:
                            if email not in dict_emails["emails"][i]["email"]:
                                dict_emails["emails"][i]["email"].append(email)
                        
                        #Añadimos los demás campos nuevos encontrados en PIPL
                        for username in pipl["usernames"]:
                            if username not in dict_emails["emails"][i]["usernames"]:
                                dict_emails["emails"][i]["usernames"].append(username)
                        
                        for address in pipl["addresses"]:
                            if address not in dict_emails["emails"][i]["addresses"]:
                                dict_emails["emails"][i]["addresses"].append(address)

                        for phone in pipl["phones"]:
                            if phone not in dict_emails["emails"][i]["phone_number"]:
                                dict_emails["emails"][i]["phone_number"].append(phone)

                        for job in pipl["jobs"]:
                            if job not in dict_emails["emails"][i]["jobs"]:
                                dict_emails["emails"][i]["jobs"].append(job)

                        for image in pipl["images"]:
                            if image not in dict_emails["emails"][i]["images"]:
                                dict_emails["emails"][i]["images"].append(image)

                        for url in pipl["urls"]:
                            if url not in dict_emails["emails"][i]["sources"]:
                                dict_emails["emails"][i]["sources"].append(url["url"])
                    i=i+1

            if(config['dehashed'] != False):
                i = 0
                #Recorremos ahora todos los correos de esa persona encontrados con Hunter y/o PIPL
                for email in dict_emails["emails"][i]["email"]:
                    dehashed = dehashedwrapper.petition(email)
                    #Va añadiendo la info al diccionario principal
                    for leak in dehashed:
                        if leak["username"] is None:
                            dict_emails["emails"][i]["usernames"].append(leak["username"])
                        if leak["phone"] is None:
                            dict_emails["emails"][i]["phone_number"].append(leak["phone"])
                        
                        if leak["password"] is None:
                            dict_emails["emails"][i]["passwords"].append({"password": leak["password"], "hash": leak["hashed_password"] ,"origin": leak["breach"]})
                        
                        if leak["address"] is None:
                            dict_emails["emails"][i]["addresses"].append({leak["address"]})
                        
                        if leak["ip_address"] is None:
                            dict_emails["emails"][i]["ips"].append({leak["ip_address"]})
                    i = i+ 1

    else:
        dict_emails = {}

    return dict_emails


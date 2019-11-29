from allintelligence import hunterwrapper, dehashedwrapper, piplwrapper

def analyze(domain, config):

       #dict_emails = {'organization': 'Onbranding', 'emails': [{'email': 'satoe82@hotmail.com', 'type': 'personal', 'confidence': 94, 'first_name': 'Selva', 'last_name': 'Orejon', 'position': 'CSO', 'seniority': 'executive', 'department': 'executive', 'linkedin': 'http://es.linkedin.com/in/selvaorejon', 'twitter': 'selvaorejon', 'phone_number': [], 'sources': ['http://comunicae1.rssing.com/chan-15207315/all_p655.html', 'http://noticiasdeocio.es/onbranding-sella-alianza-con-egarante-para-ofrecer-los-productos-de-certificacion-digital-a-sus-clientes', 'http://notasdeprensagratis.es/11470/onbranding-sella-alianza-con-egarante-para-ofrecer-los-productos-de-certificacion-digital-a-sus-clientes', 'http://europapress.es/comunicados/empresas-00908/noticia-comunicado-onbranding-sella-alianza-egarante-ofrecer-productos-certificacion-digital-clientes-20170317111427.html', 'http://diario-economia.com/nota/5608/onbranding-sella-alianza-con-egarante-para-of.html', 'http://notasdeprensa.es/1180583/onbranding-sella-alianza-con-egarante-para', 'http://noticiasdeinformatica.es/onbranding-sella-alianza-con-egarante-para-ofrecer-los-productos-de-certificacion-digital-a-sus-clientes', 'http://minotadeprensa.es/nota/6464/onbranding-sella-alianza-con-egarante-para-of.html', 'http://sonarticulos.com/2013/11/15/convocatoria-de-abstractsponencias-para-el-2o-congreso-brand-care', 'http://estrelladigital.es/articulo/comunicados/onbranding-sella-alianza-egarante-ofrecer-productos-certificacion-digital-clientes/20170317140935315815.html', 'http://slideplayer.es/slide/16746', 'http://camaltecpress.com/11275/onbranding-sella-alianza-con-egarante-para-ofrecer-los-productos-de-certificacion-digital-a-sus-clientes', 'http://comunicae1.rssing.com/chan-15207315/latest.php', 'http://onbranding.es/proteccion-reputacion-celebridades-internet', 'http://onbranding.es/proteccion-reputacion-celebridades-internet/', 'http://onbranding.es/']}, {'email': 'onbranding@onbranding.es', 'type': 'generic', 'confidence': 90, 'first_name': None, 'last_name': None, 'position': None, 'seniority': None, 'department': None, 'linkedin': None, 'twitter': None, 'phone_number': None, 'sources': ['http://ciberinvestigacion.com/tag/fanta', 'http://ciberinvestigacion.com/tag/robertus-de-rotterdam', 'http://ciberinvestigacion.com/tag/spot', 'http://comunicae1.rssing.com/chan-15207315/all_p234.html', 'http://onbranding.es/el-anuncio-de-fanta-y-sus-cursos-de-community-manager', 'http://onbranding.es/onbranding-te-acerca-a-las-empresa-visibilidad-y-reputacion-en-internet', 'http://noticiasmarketing.es/onbranding-y-legal-consultors-activan-su-servicio-celebrandsec-seguridad-para-celebridades-en-internet', 'http://uy.globedia.com/facebook-cambia-politica-privacidad-cunda-panico', 'http://madridbusiness.es/selva-orejon-ofrecera-el-curso-promocion-de-negocios-en-internet-en-san-sebastian', 'http://ciberinvestigacion.com/2009/01/05/busqueda-de-empleo-%c2%bftarea-monotonaa-%c2%bfestas-preparado', 'http://ciberinvestigacion.com/2010/05/24/el-anuncio-de-fanta-y-sus-%e2%80%9ccursos-de-community-manager%e2%80%9d', 'http://es.slideshare.net/sorejon/ciberinvestigacion-reputaciononlineonbrandingbarcelona', 'http://celebrandsec.es/servicios.html', 'http://noticiasdeinformatica.es/onbranding-y-legal-consultors-activan-su-servicio-celebrandsec-seguridad-para-celebridades-en-internet', 'http://celebrandsec.es/index.html', 'http://slideshare.net/sorejon/practicas-asistente-ejecutiva-ceo-barcelona-ceoassistantbarcelona', 'http://notasdeprensagratis.es/11510/onbranding-y-legal-consultors-activan-su-servicio-celebrandsec-seguridad-para-celebridades-en-internet', 'http://onbranding.es/jornada-proteccion-identidad-digital-madrid-22-abril-viernes-selva-orejon', 'http://europapress.es/comunicados/empresas-00908/noticia-comunicado-onbranding-legal-consultors-activan-servicio-celebrandsec-seguridad-celebridades-internet-20170321113443.html', 'http://noticiasdederecho.es/onbranding-y-legal-consultors-activan-su-servicio-celebrandsec-seguridad-para-celebridades-en-internet', 'http://celebrandsec.es', 'http://asturiasbusiness.es/2017/03/22/onbranding-y-legal-consultors-activan-su-servicio-celebrandsec-seguridad-para-celebridades-en-internet', 'http://notasdeprensa.es/1180584/onbranding-y-legal-consultors-activan-su_1', 'http://barcelonabusiness.es/2017/03/22/onbranding-y-legal-consultors-activan-su-servicio-celebrandsec-seguridad-para-celebridades-en-internet', 'http://perits.org/judiciales/expertos-en-identidad-digital-imagen-y-reputacion-en-la-red/perito-selva-maria-orejon-lozano-461', 'http://sonarticulos.com/2013/11/15/convocatoria-de-abstractsponencias-para-el-2o-congreso-brand-care', 'http://lainformacion.com/comunicados_empresas/legal-consultors-celebrandsec-celebridades-internet_0_1009999195.html', 'http://perits.org/judicials/experts-en-identitat-digital-imatge-i-reputacio-a-la-red/perit-selva-maria-orejon-lozano-461', 'http://onbranding.wordpress.com/partners', 'http://onbranding.wordpress.com/servicios']}, {'email': 'clara@onbranding.es', 'type': 'personal', 'confidence': 84, 'first_name': None, 'last_name': None, 'position': None, 'seniority': None, 'department': None, 'linkedin': None, 'twitter': None, 'phone_number': None, 'sources': ['http://slideshare.net/clarasolerd/twitter-adds-social-to-commerce']}]}
    if(config['hunter'] != False):
        dict_emails = hunterwrapper.petition(domain)

        i=0
        for emails in dict_emails["emails"]:
            dict_emails["emails"][i].update({"passwords":[],"usernames":[],"ips":[],"addresses":[], "jobs":[],"images":[]})
            i = i+1
        i=0
        #Ejecutamos pipl
        if(config['pipl'] != False):
            for emails in dict_emails["emails"]:
                #Añadimos nuevas keys al diccionario para pipl y dehashed
                # dict_emails["emails"][i].update({"passwords":[],"usernames":[],"ips":[],"addresses":[], "jobs":[],"images":[]})
                
                for email in dict_emails["emails"][i]["email"]:
                    print(email)

                    if("@mail.com" not in email):
                        pipl = piplwrapper.petition(email)
                        if "emails" in pipl:
                            #Añadimos los nuevos correos encontrados relacionados con esa persona
                            for email in pipl["emails"]:
                                if email not in dict_emails["emails"][i]["email"]:
                                    dict_emails["emails"][i]["email"].append(email)

                        #Añadimos los demás campos nuevos encontrados en PIPL
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
                                    # dict_emails["emails"][i]["sources"].append(url["url"])
                i=i+1

        if(config['dehashed'] != False):
            i = 0
            #Recorremos ahora todos los correos de esa persona encontrados con Hunter y/o PIPL
            for email_list in dict_emails["emails"]:
                for email in email_list['email']:
                    dehashed = dehashedwrapper.petition(email)
                    #Va añadiendo la info al diccionario principal
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


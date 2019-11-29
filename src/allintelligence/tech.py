import socket
import requests
import dns.resolver
import shodanwrapper

def analyze(domain):
    global_dictionary = {}

    #Comprobamos si el dominio resuelve DNS o no
    try:
        dns_results= dns.resolver.query(domain)
        dns_records = [ip.address for ip in dns_results]
        domainOn= True
    except:
        domainOn= False
        
    
    #Obtención de la IP del dominio
    if domainOn:
        ip=socket.gethostbyname(str(domain)) 


    #Módulo de whois y contractar manualmente


        #Módulo de shodan 
        dict_shodan = shodanwrapper.gethost(ip)
        print (dict_shodan)


   

    #Módulo de maxmind 



    print(domainOn)
    if domainOn:
        print(ip)
    return global_dictionary


def analyze_SMTP(domai):
    pass


def analyze_HTTP_S(domai):
    pass



#domain="allpentesting.es"
domain="lucano.uco.es"
analyze(domain)

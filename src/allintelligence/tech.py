import socket
import requests
import dns.resolver
import shodanwrapper
from config import BING_API_KEY

def analyze(domain):
    global_dictionary = {}

    #----------------------------------------RESOLUCION DNS
    #Comprobamos si el dominio resuelve DNS o no
    try:
        dns_results= dns.resolver.query(domain)
        dns_records = [ip.address for ip in dns_results]
        domainOn= True
    except:
        domainOn= False
      
     #----------------------------------------RESOLUCION DNS   
    #Obtención de la IP del dominio
    if domainOn:
        ip=socket.gethostbyname(str(domain)) 

    #----------------------------------------CHECK Cloudflare YES|NO   
    #Averiguamos si la IP está o no en alguno de los rangos de IPs de cloudflare
    if domainOn:
        cloudflareOn=check_cloudflare(ip)

    if cloudflareOn:
        print ("La ip "+ip+" ES de Cloudflare")
    else:
        print ("La ip "+ip+" NO ES de Cloudflare")


    #----------------------------------------HOSTING COMPARITOD o DEDICADO
    #Hacemos petición a bing con el operador IP
    #API gratuita de BING https://helpcenterhq.com/knowledgebase.php?article=189
    #rbing=requests.get("https://www.bing.com/search?q=ip%3A"+ip)
     
   
    #Módulo de whois y contractar manualmente

    #Obtener manualmente X info del dominio
    
    #Obtenemos los emails server MX
    mxs=[]
    mxs=dns.resolver.query(domain, 'MX')
    for mx in mxs:
        print(mx)
    #NS


    #Módulo de shodan 
    dict_shodan = shodanwrapper.gethost(ip)
    #print (dict_shodan)



    #Módulo de maxmind 



    return global_dictionary


def check_cloudflare(ip):

    #Leemos la lista de dominios IPv4 donde está cloudflare de manera dinámica
    r=requests.get("https://www.cloudflare.com/ips-v4")
    cloudflare_ips=r.text.strip().split("\n")

    #Ahora vamos viendo octeto a octeto si la ip coincide con el rango de IPs de cloudflare
    ipaddr = int(''.join(['%02x' % int(x) for x in ip.split('.')]), 16)
    for net in cloudflare_ips:
        netstr, bits = net.split('/')
        netaddr = int(''.join(['%02x' % int(x) for x in netstr.split('.')]), 16)
        mask = (0xffffffff << (32 - int(bits))) & 0xffffffff
        if (ipaddr & mask) == (netaddr & mask):
            return True
    return False


def check_hosting_compartido(ip):
    headers = {"Ocp-Apim-Subscription-Key": BING_API_KEY}
    params = {"q": "ip:"+ip+", "textDecorations": True, "textFormat": "HTML"}
    response = requests.get("https://api.cognitive.microsoft.com/bing/v7.0/search",headers=headers, params=params)
    search_results = response.json()

    tama=len(search_results['webPages']['value'])

    for i in range(0,tama):
        (search_results['webPages']['value'][i]['url'].split("//")[1].split("/")[0])
    
    #Faltaría meterlo en una lista y eliminar los que son iguales


    return True

def analyze_SMTP(domai):
    pass


def analyze_RDP(domai):
    pass

def analyze_FTP(domai):
    pass

def analyze_HTTP_S(domai):
    pass



#domain="allpentesting.es"
domain="onbranding.es"
analyze(domain)

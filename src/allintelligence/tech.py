import socket
import requests
import dns.resolver
import smtplib
from ftplib import FTP

import allpentesting.shodanwrapper
import allpentesting.maxmindwrapper
"""
Tech module that generates the technical dictionary 
by performing different tests:
    - Shodan API
    - MaxMind API
    - Cloudflare active or not
    - FTP anonymous active
    - RDP open
    - Email server with Open Relay

__author__: AllPentesting
"""

def analyze(domain,email, config):
    """
    Analysis function that launches other modules and functions.
    Parameters:
        - domain: Domain to do the analysis
        - email: Email to be used in Open Relay testing
        - config: Configuration to activate o desactivate module
    """
    dict_tech = {"domain":domain}

    """
    DNS RESOLUTION

    We check if the domain resolves DNS or not
    """
    try:
        dns_results= dns.resolver.query(domain)
        dns_records = [ip.address for ip in dns_results]
        dict_tech.update({"domainOn" : True})
    except:
        dict_tech.update({"domainOn" : False})
      
    # Obtaining the domain IP
    if dict_tech.get("domainOn", None):
        ip=socket.gethostbyname(str(domain)) 

    # Check that cloudflare is active
    if(config['cloudflare'] != False):
        if __check_cloudflare(ip):
            dict_tech.update({"cloudflare" : True})
        else:
            dict_tech.update({"cloudflare" : False})


    # Shodan module
    if(config['shodan'] != False):
        dict_shodan = shodanwrapper.petition(ip)
        dict_tech.update({"shodan":dict_shodan})


    # MaxMind module
    if config['maxmind'] != False and config['shodan'] != False:
        if(dict_tech["cloudflare"] != True):
            dict_maxmind = maxmindwrapper.petition(ip)
            dict_tech.update({"maxmind":dict_maxmind})
    
    # FTP module
    if config['ftp'] != False and config['shodan'] != False:
        if(21 in dict_tech["shodan"]["ports"]):
            dict_ftp = __analyze_FTP(domain)
            dict_tech.update(dict_ftp)
    
    # RDP module
    if config['rdp'] != False and config['shodan'] != False:
        dict_rdp = __analyze_RDP(domain)
        dict_tech.update(dict_rdp)

    # Open_Relay module
    if config['smtp'] != False and config['shodan'] != False:
        dict_smtp = __analyze_SMTP(domain,email)
        dict_tech.update(dict_smtp)

    return dict_tech


def __check_cloudflare(ip):
    """
    We check if the IP is in one of the CloudFlare IP ranges
    Parameters:
        - ip: IP address to check if it is in the CloudFlare range
    """

    r=requests.get("https://www.cloudflare.com/ips-v4")
    cloudflare_ips=r.text.strip().split("\n")

    # Now we see octet to octet if the ip matches the range of cloudflare IPs
    ipaddr = int(''.join(['%02x' % int(x) for x in ip.split('.')]), 16)
    for net in cloudflare_ips:
        netstr, bits = net.split('/')
        netaddr = int(''.join(['%02x' % int(x) for x in netstr.split('.')]), 16)
        mask = (0xffffffff << (32 - int(bits))) & 0xffffffff
        if (ipaddr & mask) == (netaddr & mask):
            return True
    return False


def __analyze_FTP(domain):
    """
    Check if the anonymous user is active on the FTP server
    Parameters:
        - domain: FTP server domain
    """
    try:
        if(FTP(domain).login()):
            return {"ftp":{"anonymous":True}}
    except:
        return {"ftp":{"anonymous":False}}
    

def __analyze_SMTP(domain, email):
    """
    Check if there is Open Relay on the mail server
    Parameters:
        - domain: Mail server domain
        - email: Email from mail server
    """
    try:
        # We proceed to get the MX
        mxs = dns.resolver.query(domain,'MX')
        mxRecord = []
        try:
            # We check if it is a domain and we try to solve it
            dns.resolver.query(mxs[0].exchange,'A')
            mxRecord.append(str(mxs[0].exchange))

        except:
            # We check if it is an ip
            try:
                ipaddress.ip_address(unicode(mxs[0].exchange))
                mxRecord.append(str(mxs[0].exchange))
            except:
                pass
        
        # Google servers give a false positive so we omit them
        if any("google.com" in s for s in mxRecord):
            return {"open_relay": False}
        

        server = smtplib.SMTP()
        server.set_debuglevel(0)
        
        # We check if you can connect to the server
        server.connect(mxRecord[0])
        server.helo(server.local_hostname)

        """
        We create a non-intrusive test where we will open to make an attempt to send an email
        If the code is equal to 250 or 554 there is Open Relay if not, it is not possible to perform the Open Relay.
        """
        sender = "allintelligence@"+domain

        code_sender, message_sender = server.mail(sender)

        if code_sender == 250:
            code_recipient, message_recipient = server.rcpt(email)
            if code_recipient == 250 or code_recipient == 554:
                server.quit()
                return {"open_relay": True}
        
        return {"open_relay": False}
    except:
        return {"open_relay": False}


def __analyze_RDP(domain):
    """
    Check if the default port(3389) of the RDP is open
    Parameters:
        - domain: RDP server domain
    """
    rdp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = rdp.connect_ex((domain,3389))
    rdp.close()
    if result == 0:
        rdpOpen = True
    else:
        rdpOpen = False

    return ({"rdp":rdpOpen})

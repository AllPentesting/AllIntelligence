import shodan
from allintelligence.config import SHODAN_API_KEY
 
def gethost(ip):
    api = shodan.Shodan(SHODAN_API_KEY)

    host_info = api.host(ip)
    '''
        host_info['asn'] -> ASN
        host_info['city'] -> Puede ser None
        host_info['hostnames'] -> array
        host_info['isp']
        host_info['org']
        host_info['ports'] -> Puertos abiertos array
        host_info['vulns'] -> Array
    '''

    return {
        'ip': host_info['ip_str'],
        'ans': host_info['asn'],
        'hostnames': host_info['hostanames'],
        'org': host_info['org'],
        'ports': host_info['ports'],
        'vulns': host_info['vulns']
    }
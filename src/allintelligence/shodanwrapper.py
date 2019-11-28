import shodan

def gethost(ip):
    SHODAN_API_KEY = ""
    api = shodan.Shodan(SHODAN_API_KEY)

    host_info = api.host(ip)
    '''

    a['asn'] -> ASN
    a['city'] -> Puede ser None

    a['hostnames'] -> array
    a['isp']
    a['org']
    a['ports'] -> Puertos abiertos array
    a['vulns'] -> Array
    '''

    return {
        'ip': host_info['ip_str'],
        'ans': host_info['asn'],
        'hostnames': host_info['hostanames'],
        'org': host_info['org'],
        'ports': host_info['ports'],
        'vulns': host_info['vulns']
    }
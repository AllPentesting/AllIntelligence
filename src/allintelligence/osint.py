from allintelligence import hunterwrapper
from allintelligence import dehashedwrapper

def analyze(domain, config):

    # Primera información
    if(config['hunter'] != False):
        dictionary = hunterwrapper.petition(domain)

        if(config['pipl'] != False):
            pass

        if(config['dehashed'] != False):
            pass

    else:
        dictionary = {}

    return dictionary



def combine_dict(dictionary):
    return dictionary
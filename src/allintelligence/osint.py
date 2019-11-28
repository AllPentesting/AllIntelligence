from allintelligence import hunterwrapper

def analyze(domain):
    global_dictionary = {}

    # To-Do: module control
    global_dictionary['hunter'] =  hunterwrapper.petition(domain)

    return global_dictionary
    
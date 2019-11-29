from allintelligence import hunterwrapper
from allintelligence import dehashedwrapper

def analyze(domain):
    # dictionary = {}

    # To-Do: module control

    # Primera información
    dictionary = hunterwrapper.petition(domain)

    # Recorremos los mails y buscamos en dehashed y añadimos si hay resultados

    # for email in dictionary['emails']:
    #     dictionary['emails'].update({email:{"passwords":dehashedwrapper.petition(email)}})

    return dictionary



def combine_dict(dictionary):
    return dictionary
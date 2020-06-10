import json
import random

with open('selenium_py/configuracion.json','r') as fichero_config:
    config = fichero_config.read()

configuracion = json.loads(config)
print(configuracion['Mensajes'])
mensajes = configuracion['Mensajes'].values()
print(mensajes.values())

for mensaje in mensajes:
    print(mensaje)


movie_list = ['The Godfather', 'The Wizard of Oz', 'Citizen Kane', 'The Shawshank Redemption', 'Pulp Fiction']

moview_item = random.choice(movie_list)
print ("Randomly selected item from list is - ", moview_item)

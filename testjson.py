import json
import random

with open('selenium_py/configuracion.json','r') as fichero_config:
    config = fichero_config.read()

configuracion = json.loads(config)

mensajes = configuracion['Mensajes'].values()
print(mensajes)

for mensaje in mensajes:
    print(mensaje)

random.choice(dict(mensajes.values()))
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import random

with open('selenium_py/configuracion.json','r') as fichero_config:
    config = fichero_config.read()

configuracion = json.loads(config)
print(configuracion['Mensajes'])
mensajes = configuracion['Mensajes'].values()
print(mensajes)
lista_mensajes = []

for mensaje in mensajes:
    lista_mensajes.append(mensaje)

print(lista_mensajes)

mensaje_aleatorio = random.choice(lista_mensajes)
print ("Mensaje aleatorio ->", mensaje_aleatorio)

import json


with open('selenium_py/configuracion.json','r') as configuracion:
    data = configuracion.read()

y = json.loads(data)

print(y["Instagram"]['username'])
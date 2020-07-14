from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import json
import time
import random


#recupero fichero de configuracion
with open('selenium_py/configuracion.json','r') as fichero_config:
    config = fichero_config.read()
#recupero todos los valores y me los dejo en el objeto configuracion
configuracion = json.loads(config)
#busco el driver en el sistema y le aplico configuraciones especificas
driver = webdriver.Chrome('C:/Driver/chromedriver.exe')
driver.implicitly_wait(configuracion['Configuracion']['implicitly_wait'])
#accedo a la url indicada
driver.get("https://www.instagram.com/")
#para facilitar la visualizacion y evitar problemas de compatibilidad del tipo de pantalla, la maximizo
driver.maximize_window()
#defino la espera estandar en segs
wait = WebDriverWait(driver, 3)
#recupero valor de username y lo introduzco
xp_usuario = configuracion['elementos']['xp_usuario']
driver.find_element_by_xpath(xp_usuario).send_keys(configuracion['instragram']['username'])
#recupero valor de password y lo introduzco
xp_contrasena = configuracion['elementos']['xp_contrasena']
driver.find_element_by_xpath(xp_contrasena).send_keys(configuracion['instragram']['password'])
#busco el boton de entrar y lo pulso
xp_entrar = configuracion['elementos']['xp_entrar']
driver.find_element_by_xpath(xp_entrar).submit()
time.sleep(5)
#Voy al primer usuario
#cargo los mensajes en un array
mensajes = configuracion['mensajes'].values()
lista_mensajes = []
for mensaje in mensajes:
    lista_mensajes.append(mensaje)
print(lista_mensajes)
#lista_mensajes contiene todos los mensajes posibles configurados
usuarios = configuracion['usuarios'].values()
lista_usuarios = []
for usuario in usuarios:

    driver.get("https://www.instagram.com/" + usuario)
    xp_ultima_foto = configuracion['elementos']['xp_ultima_foto']
    driver.find_element_by_xpath(xp_ultima_foto).click()
    xp_comentario = configuracion['elementos']['xp_comentario']
    driver.find_element_by_xpath(xp_comentario).click()
    mensaje_aleatorio = random.choice(lista_mensajes)
    driver.find_element_by_xpath(xp_comentario).send_keys(mensaje_aleatorio)
    xp_boton_publicar = configuracion['elementos']['xp_boton_publicar']
    #driver.find_element_by_xpath(XPBotonPublicar).click()
    time.sleep(10)

driver.close()
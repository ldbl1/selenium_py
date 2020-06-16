from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import json
import time


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
XPusuario = configuracion['Elementos']['XPusuario']
driver.find_element_by_xpath(XPusuario).send_keys(configuracion['Instagram']['username'])
#recupero valor de password y lo introduzco
XPcontrasena = configuracion['Elementos']['XPcontrasena']
driver.find_element_by_xpath(XPcontrasena).send_keys(configuracion['Instagram']['password'])
#busco el boton de entrar y lo pulso
XPentrar = configuracion['Elementos']['XPentrar']
driver.find_element_by_xpath(XPentrar).submit()
time.sleep(5)
#Voy al primer usuario
#cargo los mensajes en un array
mensajes = configuracion['Mensajes'].values()
lista_mensajes = []
for mensaje in mensajes:
    lista_mensajes.append(mensaje)
print(lista_mensajes)
#lista_mensajes contiene todos los mensajes posibles configurados
usuarios = configuracion['Usuarios'].values()
lista_usuarios = []
for usuario in usuarios:

    driver.get("https://www.instagram.com/" + usuario)
    XPUltimaFoto = configuracion['Elementos']['XPUltimaFoto']
    driver.find_element_by_xpath(XPUltimaFoto).click()
    XPComentario = configuracion['Elementos']['XPComentario']
    driver.find_element_by_xpath(XPComentario).click()
    driver.find_element_by_xpath(XPComentario).send_keys(configuracion['Mensajes']['0'])
    XPBotonPublicar = configuracion['Elementos']['XPBotonPublicar']
    #driver.find_element_by_xpath(XPBotonPublicar).click()
    time.sleep(10)

driver.close()
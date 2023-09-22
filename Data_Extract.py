import requests 
import re
from urllib.parse import urlparse, parse_qs
from bs4 import BeautifulSoup
import zipfile


def obtener_url():
    url = []
    for anio in range(2015,2024):
        texto="https://cammesaweb.cammesa.com/historico-sintesis-mensual-"+str(anio) +"/"
        response = requests.get(texto)
        urls = re.findall(r'https://[^"\s]*base[^"\s]*', response.text)
        for uurl in urls:
           url.append(uurl)
    return url

def descarga(url_actual):
    nombre_archivo = "archivo.zip"
    
    response = requests.get(url_actual)

    if response.status_code == 200:
        with open(nombre_archivo, 'wb') as archivo:
            archivo.write(response.content)
        print(url, "Descarga exitosa.")
    else:
        print("Error al descargar el archivo. Código de estado:", response.status_code)
    return nombre_archivo

def unzip(archivo_zip):
    with zipfile.ZipFile(archivo_zip, 'r') as archivo_zip:
        archivo_zip.extractall()
    return


url = obtener_url()
for urls in (url):
    nombre_archivo = descarga(urls)
    unzip(nombre_archivo)

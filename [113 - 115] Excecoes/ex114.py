"""
Site está acessível?
"""
import urllib
import urllib.request

try:
    site = urllib.request.urlopen("http://www.pudim.com.br")
except urllib.error.URLError:
    print("Não foi possivel abrir o site")
else:
    print("Deu bom")
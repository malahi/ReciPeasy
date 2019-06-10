import socketserver
import requests
import urllib
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
from handler import HCIRequestHandler
# req = urllib.request.Request("https://food52.com/recipes/12167-beauty-school-knockout-peppermint-hot-fudge-sundae", headers={'User-Agent' : "Magic Browser"})
# html = urllib.request.urlopen( req )
# soup = BeautifulSoup(html, "html.parser")
#
# print(soup.findAll('meta',attrs={'name':re.compile('twitter:title')}))
# print(soup.findAll(text=re.compile('Author Notes')))
Handler = HCIRequestHandler
server = socketserver.TCPServer(('0.0.0.0', 8080), Handler)

server.serve_forever()

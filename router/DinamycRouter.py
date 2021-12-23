import requests
from schemas.user import userEntity
import json

class DinamycRouter:

 def __init__(self, url):
    self.url = url

 def getUrl(self):
        return self.url

 def GETJson(self):
   resp = requests.get(self.url)
   if resp.status_code != 200:
       print("Error en el server" + self.url)
   respuesta = resp.json()
   return respuesta

 #{'firstname':'Ryan', 'lastname':'Mitchell'}#
 def POSTJson(self, diccionary):
    entity = json.dumps(diccionary)
    resp = requests.post(self.url, data=entity)
    #return resp.status_code
    return resp.json()

 def PUTJson(self, diccionary):
     entity = json.dumps(diccionary)
     resp = requests.put(self.url, data=entity)
     #return resp.status_code
     return resp.json()


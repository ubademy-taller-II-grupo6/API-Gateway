import requests

class DinamycRouter:


 def _init_self(self,url):
    self.url = url

 def getUrl(self):
        return self.url

 def GETJson(self):
   resp = requests.get(self.url)
   if resp.status_code != 200: print ("Erro en el server" + self.url)
   respuesta = resp.json()
   return respuesta

 #{'firstname':'Ryan', 'lastname':'Mitchell'}#
 def POSTJson(self, json):
    resp = requests.post(self.url, data=json)
    return resp.status_code

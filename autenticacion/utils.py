import firebase_admin

from firebase_admin import credentials
from firebase_admin import auth

cred = credentials.Certificate('ubademy-apigateway-firebase-adminsdk-hbeag-c06eb7278c.json')
default_app = firebase_admin.initialize_app(cred)
id_project = default_app.project_id

def validar_token(id_token):
    try:
       decoded_token = auth.verify_id_token(id_token, default_app)
       aud = decoded_token['aud']   #uid
       if aud == id_project:
         return "Id del proyecto confimada ud"+ aud
    except:
       return'Token invalido o vencido'
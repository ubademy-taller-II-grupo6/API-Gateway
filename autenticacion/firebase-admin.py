import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

#Inicializa el SDK firebase
#cred = credentials.Certificate('/home/marcos/PycharmProjects/API-Gateway/ubademy-apigateway-firebase-adminsdk-hbeag-c06eb7278c.json')

firebase_admin.initialize_app(cred)
uid = 'ICfowjTE50V8uLXB1ruoxycokkh2'  #mriarte9@gmail.com
#custom_token = auth.create_custom_token(uid)
#print(custom_token)

# id_token comes from the client app (shown above)
decoded_token = auth.verify_id_token(id_token)
uid = decoded_token['uid']

email = input('ṕor favor inra seuma iol')
password = input('ṕor favor ingres eu pass')

user = auth.create_user(email=email, password=password)
# id_token comes from the client app (shown above)
decoded_token = auth.verify_id_token(id_token)
uid = decoded_token['uid']



cred = credentials.RefreshToken('path/to/refreshToken.json')
default_app = firebase_admin.initialize_app(cred)

#Decodficio el token
decoded_token = auth.verify_id_token(id_token)
uid = decoded_token['uid']

#Si se inicializó el SDK con la opción projectId explícita de la app, este usa el valor de esa opción.
options = {
    'serviceAccountId': 'my-client-id@my-project-id.iam.gserviceaccount.com',
}
firebase_admin.initialize_app(options=options)

uid = 'ICfowjTE50V8uLXB1ruoxycokkh2'
custom_token = auth.create_custom_token(uid)
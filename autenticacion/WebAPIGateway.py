import pyrebase

config = {

    "apiKey": "AIzaSyB5cvfwNdX_HP4pJODxxlNv4JRuIIWJp_s",

    "authDomain": "ubademy-apigateway.firebaseapp.com",

    "projectId": "ubademy-apigateway",

    "storageBucket": "ubademy-apigateway.appspot.com",

    "messagingSenderId": "934202487625",

    "appId": "1:934202487625:web:ad459ee18794d8af20e098",

    "measurementId": "G-7085K4CLZJ"

}

firebase = pyrebase.initialize_app(config)
#storage = firebase.storage()
#database = firebase.database()
auth = firebase.auth()

#Login usuario
email = input('Ingrese mail')
password = input('ingrese password')

try:
    auth.sign_in_with_email_and_password(email, password)
    print('Login exitoso')

except:
      print('usuario invalido o password invalido, tratemos de nuevo')




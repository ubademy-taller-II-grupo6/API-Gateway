import firebase_admin
from fastapi import APIRouter, Depends, HTTPException, status
from firebase_admin import credentials, auth
from autenticacion.get_Token import get_token
from models.administrator import Administrator
from models.deposit import Deposit
from models.user import User
from models.userExt import UserExt
from router.DinamycRouter import DinamycRouter
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

APIGateway = APIRouter()
cred = credentials.Certificate('./ubademy-apigateway-firebase-adminsdk-hbeag-c06eb7278c.json')
default_app = firebase_admin.initialize_app(cred)



#Crea el registro del usuario, devuelve el status code
@APIGateway.post('/users')
def create_user(user: User):
    new_user = dict(user)
    service = DinamycRouter('https://obscure-wildwood-00771.herokuapp.com/users')
    return service.POSTJson(new_user)


#Devuelve la lista de todos los usuarios del sistema
@APIGateway.get('/users')
def list_users():
         service = DinamycRouter('https://obscure-wildwood-00771.herokuapp.com/users')
         return service.GETJson()


#Cambia los datos de un usuario en el sistema
@APIGateway.put('/users/{userId}')
def get_user(user: UserExt, userId:str , authorization: HTTPAuthorizationCredentials = Depends(HTTPBearer(auto_error=False))):
    new_user = dict(user)
    service = DinamycRouter('https://obscure-wildwood-00771.herokuapp.com/users/'+userId)
    return service.GETJson(new_user)

#Devuelve un usuarios de sistema
@APIGateway.get('/users/{userId}')
def find_user(userId: str):
    serviceAdmin = DinamycRouter("https://obscure-wildwood-00771.herokuapp.com/users?user_id="+userId)
    return serviceAdmin.GETJson()


##Administradores

#Registro de administrador
@APIGateway.post('/admin/register')
def create_admin(administrator: Administrator):
    new_administrator = dict(administrator)
    serviceAdmin = DinamycRouter("https://calm-shore-44525.herokuapp.com/user")
    return serviceAdmin.POSTJson(new_administrator)


#Perfil  #Definir el user Id (por ahora el mail)
@APIGateway.get('/admin/{userId}')
def find_admin(userId: str):
    serviceAdmin = DinamycRouter("https://calm-shore-44525.herokuapp.com/user/?email="+userId)
    return serviceAdmin.GETJson()


#Devuelve todos los administradores
@APIGateway.get('/admin/')
def find_all_admins():
    serviceAdmin = DinamycRouter("https://calm-shore-44525.herokuapp.com/users/")
    return serviceAdmin.GETJson()


#Ingresar al sistema de de admins
@APIGateway.get('/admin/login/{userid}&{password}')
def find_all_admins(userId: str, password: str):
    service = DinamycRouter("https://calm-shore-44525.herokuapp.com/login/?email="+userId+"&contraseña="+password)
    return service.GETJson()

#Sistema de pagos

#Obtener la billetera del usuario (direccion del block chain y clave)
@APIGateway.get('/user/wallet/{userid}')
def get_wallet(userId: str):
    service = DinamycRouter("https://infinite-caverns-43846.herokuapp.com/wallet/"+userId)
    return service.GETJson()

#Obtener todas las billeteras de todos los usuarios
@APIGateway.get('/user/all_wallets')
def get_all_wallets():
    service = DinamycRouter("https://infinite-caverns-43846.herokuapp.com/wallet")
    return service.GETJson()

#Realiza un pago en ethers para un user id
@APIGateway.post('/user/deposit')
def deposit_amounth(deposit: Deposit):
    new_deposit = dict(deposit)
    servicePay = DinamycRouter("https://infinite-caverns-43846.herokuapp.com/deposit")
    return servicePay.POSTJson(new_deposit)

#Autenticacion y autorizacion

#Autenticacion por token
@APIGateway.get('/user/get_token/{mail}&{password}')
def get_user_token(mail: str, password: str):
    return get_token(mail, password)


@APIGateway.post('/user/auth')
def verify_login(cred: HTTPAuthorizationCredentials = Depends(HTTPBearer(auto_error=False))):
    if cred is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Bearer authentication required",
            headers={'WWW-Authenticate': 'Bearer realm="auth_required"'},
        )
    try:
       decoded_token = auth.verify_id_token(cred.credentials)
       aud = decoded_token['aud']
       id_project = default_app.project_id
       if aud == id_project:
            return "Autorizado"
       else:
            # default_app.delete()
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Token invalido",
                headers={'WWW-Authenticate': 'Bearer error="invalid_token"'},
            )
    except Exception as err:
           raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid authentication credentials. {err}",
            headers={'WWW-Authenticate': 'Bearer error="invalid_token"'},
           )



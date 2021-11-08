from fastapi import APIRouter, Header
from models.register import Register
from models.login import Login
from models.administrator import Administrator
from router.DinamycRouter import DinamycRouter
from schemas.administrator import administratorEntity, administratorsEntity


from autenticacion.utils import validar_token

import firebase_admin

from firebase_admin import credentials
from firebase_admin import auth



APIGateway = APIRouter()


#Crea el registro del usuario, devuelve el status code
@APIGateway.post('/user/resgister')
def create_register(register: Register):
    new_register = dict(register)
    service = DinamycRouter('https://obscure-wildwood-00771.herokuapp.com/users/registration')
    return service.POSTJson(new_register)

#Autenticacion por token
@APIGateway.post('/user/auth')
def verify_login(authorization: str = Header(None)):
    id_token = authorization.split(' ')[1]  #Separa la cadena y toma el codigo de token (sin "Beareer")
    return validar_token(id_token)



#Realiza un login en el sistema
@APIGateway.post('/user/login/{userId}&&{password}')
def create_login(login: Login):
    new_login = dict(login)
    service = DinamycRouter('https://obscure-wildwood-00771.herokuapp.com/users/login')
    return service.POSTJson(new_login)

#Administradores

#Registro de administrador
@APIGateway.post('/admin/register')
def create_admin(administrator: Administrator):
    new_administrator = dict(administrator)
    service = DinamycRouter("https://calm-shore-44525.herokuapp.com/user")
    return service.POSTJson(new_administrator)

#Perfil  #Definir el user Id
@APIGateway.get('/admin/{userId}')
def find_admin(userId: str):
    service = DinamycRouter("https://calm-shore-44525.herokuapp.com/user"+userId)
    return administratorsEntity(service.GETJson())


#@log.get('/user/recover_password/{email}')
#def create_entry(entry: Entry):
 #   new_user = dict(entry)
    #Guarda el usuario recibido en la base de datos ,esta le asigna un id en la DB
  #  id  = client.ubademyLog.Login.insert_one(new_user).inserted_id
    #Busca en base el id anterior el usuario y lo devuelve
   # entry = client.ubademyLog.Login.find_one(id)
    #return e
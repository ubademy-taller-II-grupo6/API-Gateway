from pydantic import BaseModel


class Administrator(BaseModel):
   email: str
   contraseña: str
   nombre: str
   apellido: str

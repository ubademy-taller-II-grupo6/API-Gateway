import os
import uvicorn
from fastapi import FastAPI
from routers.APIGateway import APIGateway

app = FastAPI(
    title= "Ubademy-APIGateway de usuarios",
    description= "API gateway ubademy, implementa la autenticacion e interfaz de servicios",
    version=1.0
)

app.include_router(APIGateway)

if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=int(os.environ.get('PORT')), reload=True)
   #uvicorn.run('app:app')
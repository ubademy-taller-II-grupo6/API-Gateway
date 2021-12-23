import os
import uvicorn
from fastapi import FastAPI
from routers.APIGateway import APIGateway
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title= "Ubademy-APIGateway de usuarios",
    description= "API gateway ubademy, implementa la autenticacion e interfaz de servicios",
    version=1.0
)

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"],
                   allow_headers=["*"])

app.include_router(APIGateway)

if __name__ == '__main__':
  #  uvicorn.run('app:app', host='0.0.0.0', port=int(os.environ.get('PORT')), reload=True)
  uvicorn.run('app:app')
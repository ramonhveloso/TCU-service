from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import router as api_router
from app.database.base import Base
from app.database.session import engine

app = FastAPI(
    title="Boilerplate Automa",
    description="""Este projeto é um template base para aplicações 
                    backend utilizando FastAPI, projetado para acelerar o 
                    desenvolvimento de novos projetos. Ele segue boas práticas 
                    de organização, escalabilidade e facilidade de manutenção, 
                    permitindo que seja reutilizado como ponto de partida para 
                    diferentes tipos de aplicações.""",
    version="0.1.0",
)

# Criar tabelas do banco de dados
Base.metadata.create_all(bind=engine)

# Incluir rotas
app.include_router(api_router, prefix="/api/v1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

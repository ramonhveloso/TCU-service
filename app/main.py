from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import router as api_router
from app.database.base import Base
from app.database.session import engine

app = FastAPI(
    title="Application Automa",
    description="""Este projeto consiste em uma aplicação de backend robusta, 
                    desenvolvida com FastAPI, que fornece uma API RESTful eficiente 
                    e de alto desempenho. O sistema foi projetado para suportar um 
                    front-end dinâmico, que foi desenvolvido com a assistência do GPT Engine, 
                    garantindo uma interface de usuário intuitiva e envolvente.""",
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

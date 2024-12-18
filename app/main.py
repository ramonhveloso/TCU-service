from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import router as api_router
from app.database.base import Base
from app.database.session import engine

app = FastAPI(
    title="Microservice TCU",
    description="""Este repositório contém um microserviço desenvolvido com FastAPI 
                    para atender às necessidades do Tribunal de Contas da União (TCU). 
                    O serviço foi projetado para oferecer uma solução eficiente e escalável, 
                    promovendo a automação e modernização de processos relacionados à fiscalização, 
                    auditoria e controle.""",
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

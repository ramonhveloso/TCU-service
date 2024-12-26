import os
from typing import Annotated

from fastapi import APIRouter, HTTPException, Security
import httpx
from bs4 import BeautifulSoup

from app.api.v1.usuarios.usuario_repository import UsuarioRepository
from app.api.v1.usuarios.usuario_service import UsuarioService
from app.middleware.dependencies import AuthUser, jwt_middleware

router = APIRouter()
user_service = UsuarioService(UsuarioRepository())
BASE_URL = os.getenv("BASE_URL") 

@router.get("/list-remote-folders/")
async def list_remote_folders(
    path: str = "/",
    #AuthUser: Annotated[AuthUser, Security(jwt_middleware)],
):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(BASE_URL + path)

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Não foi possível acessar o servidor.")

        soup = BeautifulSoup(response.text, "html.parser")
        folders = []

        # Procura links que apontam para subdiretórios
        for link in soup.find_all("a"):
            href = link.get("href")
            if href and href.endswith("/"):
                folders.append(href.strip("/"))

        return {"base_url": BASE_URL, "folders": folders}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao acessar o servidor remoto: {str(e)}")


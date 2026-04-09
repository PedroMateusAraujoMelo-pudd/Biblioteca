from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from schemas.livro import LivroCreate, LivroOut
from services.biblioteca_service import (
    criar_livro,
    listar_livro,
    buscar_livro,
    alterar_preco_livro,
)
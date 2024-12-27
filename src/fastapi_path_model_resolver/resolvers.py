from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi_path_model_resolver_danielrangelsa import PathModelResolverMiddleware, resolve_orm, instantiate_orm

def get_db():
    # Função para obter a sessão do banco de dados
    # Substitua pelo código específico do seu projeto
    pass

def get_model_instance(model_class, model_id: int, db: Session = Depends(get_db)):
    detected_orms = resolve_orm()
    if not detected_orms:
        raise HTTPException(status_code=500, detail="No known ORM detected")

    orm_instance = instantiate_orm(detected_orms[0])
    resolver = PathModelResolverMiddleware(orm_instance, "fastapi")
    model_instance = resolver.resolve_model(model_class, model_id)
    if not model_instance:
        raise HTTPException(status_code=404, detail="Model not found")
    return model_instance
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

class User(BaseModel):
    name: str
    age: int = Field(..., gt=0, description="Age must be greater than 0")

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API FastAPI!"}

@app.post("/users")
def create_user(user: User):
    return {"message": f"Usuário {user.name} com idade {user.age} recebido com sucesso!"}
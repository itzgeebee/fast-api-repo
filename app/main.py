from app import models, test
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(test.router, tags=['Tests'], prefix='/api/tests')
@app.get("/api")
def root():
    return {"message": "welcome to this test fast api server"}

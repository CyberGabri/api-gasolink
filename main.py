from fastapi import FastAPI
from routers.profile import router as profile_router

app = FastAPI()

app.include_router(profile_router)

@app.get("/")
def root():
    return {"message": "API organizada rodando 🚀"}

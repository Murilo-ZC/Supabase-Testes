from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import image, collection

app = FastAPI()

app.include_router(image.router, prefix="/image", tags=["Image"])
app.include_router(collection.router, prefix="/collection", tags=["Collection"])

app.mount("/static", StaticFiles(directory="static"), name="static")

# Quando o script main.py for executado, ele inicializa o servidor da aplicação.
# Importante: reload=True, apenas em tempo de desenvolvimento, desativar em produção.

import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
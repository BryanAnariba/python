from fastapi import FastAPI

app = FastAPI()
# Iniciar el servidor: uvicorn main:app --reload
# Detener el servidor: CTRL + C

# Documentacion de la API con Swagger: http://127.0.0.1:8000/docs
# Documentacion de la API con Redocly: http://127.0.0.1:8000/redoc

@app.get('/')
async def root():
    return "Hola Fast Api"
2:42
@app.get('/cursos')
async def getCursos():
    return { "urlCurso": "http://bryananariba.com/angular" }
from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.model import predict_image
from app.utils import read_imagefile
import shutil
import os

app = FastAPI()


# Set up Jinja2 templates
templates = Jinja2Templates(directory="app/web")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": None})

@app.post("/predict-ui", response_class=HTMLResponse)
async def predict_ui(request: Request, file: UploadFile = File(...)):
    image = read_imagefile(await file.read())
    prediction = predict_image(image)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": prediction,
        "filename": file.filename
    })

@app.post("/predict")
async def predict_api(file: UploadFile = File(...)):
    image = read_imagefile(await file.read())
    prediction = predict_image(image)
    return {"prediction": prediction}
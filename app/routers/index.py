from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/")
def read_index(request: Request, response_class=HTMLResponse):
    return templates.TemplateResponse("index.html", {"request": request})
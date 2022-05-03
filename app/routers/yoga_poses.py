from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.models.poses import Poses

router = APIRouter()
templates = Jinja2Templates(directory="app/templates/")

@router.get("/yoga_poses")
def read_index(request: Request, response_class=HTMLResponse):
    poses = Poses()
    return templates.TemplateResponse("yoga_poses/index.html", {"request": request, "poses": poses.group_by(3)})

@router.get("/yoga_poses/{yoga_pose_id}")
def read_yoga_pose_id(yoga_pose_id, request: Request, response_class=HTMLResponse):
    poses = Poses()
    pose = poses.find_by(int(yoga_pose_id))
    return templates.TemplateResponse("yoga_poses/show.html", {"request": request, "pose": pose})

@router.get("/yoga_poses/{yoga_pose_id}/perform")
def read_yoga_pose_id(yoga_pose_id, request: Request, response_class=HTMLResponse):
    poses = Poses()
    pose = poses.find_by(int(yoga_pose_id))
    return templates.TemplateResponse("yoga_poses/perform.html", {"request": request, "pose": pose})

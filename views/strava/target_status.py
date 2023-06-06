import fastapi
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import status

from view_models.strava.target_status import TargetStatusViewModel 
from controllers.strava import assess_target

router = fastapi.APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse, include_in_schema=False)
async def form(request: Request):
    vm = TargetStatusViewModel(request)
    return templates.TemplateResponse("/strava/index.html", vm.to_dict())

@router.post("/", response_class=HTMLResponse, include_in_schema=False)
async def form(request: Request):
    vm = TargetStatusViewModel(request)
    await vm.load()
    params = f'?kms={vm.kms}&target={vm.target}&message={vm.message}'
    response = fastapi.responses.RedirectResponse(f"/target_status{params}", status_code=status.HTTP_302_FOUND)
    return response 
    

@router.get("/target_status", response_class=HTMLResponse, include_in_schema=False)
def target_status(request: Request, target:str, kms:str):
    vm = TargetStatusViewModel(request)
    if target.isdigit() and kms.isdigit():
        vm.kms = kms
        vm.target = target
        vm.assess_target()
    else:
        vm.message = "Target and Kms needs to be a number"
    return templates.TemplateResponse("/strava/target_status.html", vm.to_dict())


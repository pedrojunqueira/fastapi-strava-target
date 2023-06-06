
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


from api import api_responses
from views.strava import target_status

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(api_responses.router)
app.include_router(target_status.router)



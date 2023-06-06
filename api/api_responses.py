from datetime import datetime

import fastapi

from models.kilometers_request import KilometerRequest
from controllers.strava import assess_target

router = fastapi.APIRouter()

@router.post("/calculate_kilometers")
def calculate_kilometers(km_request: KilometerRequest):
    target = km_request.target
    kilometers = km_request.kilometers

    message = assess_target(target, kilometers)

    return {"message": message}
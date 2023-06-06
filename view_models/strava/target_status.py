from typing import Optional
from starlette.requests import Request

from view_models.shared.view_model import ViewModelBase
from controllers import strava

class TargetStatusViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)
        self.target: Optional[str] = ''
        self.kms: Optional[str] = ''
        self.message: Optional[str] = None
    
    async def load(self):
        form = await self.request.form()
        self.target = form.get('target')
        self.kms = form.get('kilometers')

    def assess_target(self):
        self.message = strava.assess_target(int(self.target), km_ridden=int(self.kms))
        
        

        
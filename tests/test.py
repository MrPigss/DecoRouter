from starlette.applications import Starlette
from starlette.responses import JSONResponse
from decoRouter.decoRouter import Router

router = Router()

@router.get('/')
async def home(request):
    return JSONResponse({'a':'1'})

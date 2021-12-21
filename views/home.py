import fastapi
import fastapi_chameleon
from fastapi_chameleon import template
import os

ROOT_DIR = os.path.abspath(os.curdir)
router = fastapi.APIRouter()
fastapi_chameleon.global_init('templates')


@router.get('/')
@template(template_file=ROOT_DIR+'/templates/home/index.pt')
def index():
    return {
        'package_count': 274_000,
        'release_count': 2_234_847,
        'user_count': 73_874,
        'packages': [
            {'id': 'fastapi', 'summary': "A great web framework"},
            {'id': 'uvicorn', 'summary': "Your favorite ASGI server"},
            {'id': 'httpx', 'summary': "Requests for an async world"},
        ]
    }


@router.get('/about')
@template()
def about():
    return fastapi.responses.HTMLResponse(content="Pappu pass")

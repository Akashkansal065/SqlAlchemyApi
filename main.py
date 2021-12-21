from typing import Optional
from db.sessiondb import *
from views import home
import fastapi_chameleon
import fastapi
from fastapi import Depends
import uvicorn
from starlette.staticfiles import StaticFiles
from db.Schemas import *
from sqlalchemy.orm import Session
import Apis.Allapis as Allapis
import os

ROOT_DIR = os.path.abspath(os.curdir)
api = fastapi.FastAPI(titel="Learn", description="Started learning fastapi using alchemy library")
# Base.metadata.create_all(engine)
fastapi_chameleon.global_init('templates', auto_reload=True)
api.mount('/static', StaticFiles(directory="static"), name="static")
api.include_router(router=home.router)
api.include_router(router=Allapis.router)


# @api.get('/')
# def index():
#     return fastapi.responses.JSONResponse('welcome back to fast api learn')


@api.get('/name')
def print_hi(a: int, b: int, c: Optional[int] = None):
    value = a + b
    if c is not None:
        value *= c
    else:
        return fastapi.Response(content='fail', status_code=400)
    result = {"val": value}
    return result


def main():
    # startCreatingTables()
    print(ROOT_DIR)
    uvicorn.run(api, port=8001)


if __name__ == '__main__':
    main()

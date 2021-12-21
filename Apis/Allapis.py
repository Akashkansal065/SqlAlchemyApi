import fastapi
import sqlalchemy.orm
from sqlalchemy.orm import Session
from fastapi import Depends
import db.sessiondb as getSess
from db.Schemas import *
import views.pydanviews as pyview

router = fastapi.APIRouter()


@router.post('/createorder')
def createorder(proddet: pyview.Orderview, db: Session = Depends(getSess.getDb)):
    dbInsert = Order(productname=proddet.productname, emailId=proddet.emailId)
    print(proddet.productname, proddet.emailId)
    db.add(dbInsert)
    print('data inserted')
    db.commit()
    db.refresh(dbInsert)
    return dbInsert


@router.get('/list')
def orderlist(db: Session = Depends(getSess.getDb)):
    allOrdersList = db.query(Order).all()
    return allOrdersList  # fastapi.responses.JSONResponse(content=allOrdersList, status_code=200)

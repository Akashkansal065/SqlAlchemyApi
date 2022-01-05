import fastapi
import sqlalchemy.orm
from sqlalchemy.orm import Session
from fastapi import Depends, UploadFile, File
import db.sessiondb as getSess
from db.Schemas import *
import views.pydanviews as pyview
import os
import openpyxl as op
import pandas as pd
import json
import shutil

RootDir = os.path.abspath(os.curdir)
#excelpath = RootDir+"\\CartData.xlsx"


def fetchExcel(path):
    #print(RootDir)
    exl = op.load_workbook(filename=path)
    allSheets = exl.sheetnames
    activeSheet = exl[allSheets[0]]
    #print(activeSheet)

    sheet = pd.read_excel(path, sheet_name=allSheets[0])
    # print(sheet)
    # print('Excel Sheet to Dict:', sheet.to_dict('records'))
    df = pd.DataFrame(data=sheet.to_dict('records'))
    df = df.dropna(thresh=5)
    df = df.fillna(value='NA')
    # print(df.dtypes)
    df = df.applymap(str)
    df = df.replace(".0", "")
    sheetData = df.to_dict('records')
    print(sheetData)
    return sheetData


router = fastapi.APIRouter()


@router.post('/createorder')
def createorder(proddet: pyview.Orderview, db: Session = Depends(getSess.getDb)):
    dbInsert = Order(productname=proddet.productname, emailId=proddet.emailId, username=proddet.username)
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


@router.post('/upload')
def fileuploading(file: UploadFile = File(...)):
    print(file.content_type)
    print(file.filename)
    with open("cartdata.xlsx", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    print(file.filename)
    adaa =  fetchExcel(RootDir+"\\cartdata.xlsx")
    return fastapi.responses.JSONResponse(adaa)

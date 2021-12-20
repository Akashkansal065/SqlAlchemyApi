import sqlalchemy as sqa
import sqlalchemy.orm as orm
from db.AlchemBase import Sqldeclarative
from db.Schemas import *
from sqlalchemy.orm.session import *

connstr = 'sqlite:///./checkout.db'
engine = sqa.create_engine(connstr, echo=True, connect_args={"check_same_thread": False})
Localdbsession = orm.sessionmaker(bind=engine)
Base = Sqldeclarative
Base.metadata.create_all(bind=engine)


def getDb():
    db = Localdbsession()
    try:
        print('creating session')
        yield db
    finally:
        print('session closed')
        db.close()

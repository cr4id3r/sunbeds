from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from src.datastore.db_constants import DB_NAME, DB_HOST, DB_PASS, DB_USER

db = create_engine('mysql://%s:%s@%s/%s' % (DB_USER, DB_PASS, DB_HOST, DB_NAME), echo=True)
Base = declarative_base()
session = Session(db)

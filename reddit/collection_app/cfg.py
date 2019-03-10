import psycopg2
import os
from sqlalchemy import create_engine, Table, Column, String, MetaData

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey

from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base


client_id = "CuZZ9Hw2-lENkQ"
client_secret = "Cu8ruqL1A5LBGHOiGJ32QISpomw"
password = "A2sSaQq9w4f5E49"
username = "RavenousDataBot"


if 'RDS_DB_NAME' in os.environ:
    dbname = os.environ['RDS_DB_NAME']

else:
    dbname = 'django1'

db = create_engine('postgresql+psycopg2:///%s' % (dbname))


meta = MetaData(bind=db, reflect=True )

meta.bind = db

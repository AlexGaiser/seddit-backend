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
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }

    dbname = os.environ['RDS_DB_NAME']
    dbuser = os.environ['RDS_USERNAME']
    dbpassword = os.environ['RDS_PASSWORD']
    dbhost = os.environ['RDS_HOSTNAME']
    dbport = os.environ['RDS_PORT']
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

    basdir=os.path.abspath(os.path.dirname(__file__))

    db = create_engine("postgres:///%s:%s@aayoxvcb6ixvlm.csv8i3eqbu4y.us-east-1.rds.amazonaws.com%s/%s" % (dbuser,dbpassword, dbport, dbname))
    
    print(db)
else:
    dbname = 'django2'
    db = create_engine('postgresql+psycopg2:///'+str(dbname))


meta = MetaData(bind=db, reflect=True )

meta.bind = db

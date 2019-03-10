import psycopg2
from sqlalchemy import create_engine, Table, Column, String, MetaData

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey

from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base

import reddit.collection_app.schema as sc

from reddit.collection_app.cfg import db, meta

# import schema as sc


def insert_pgdb(database, table, data):
    db.execute(meta.tables[table].insert(), data)
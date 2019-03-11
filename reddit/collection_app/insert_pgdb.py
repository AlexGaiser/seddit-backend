import psycopg2
from sqlalchemy import create_engine, Table, Column, String, MetaData

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey

from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base



import reddit.collection_app.schema as sc

# from reddit.collection_app.cfg import db, meta

from django.shortcuts import render
from django.conf import settings
from django.core import serializers
import sqlalchemy
from rest_framework import generics
from django.contrib.postgres.search import SearchVector



from reddit.models import RedditPost

# import schema as sc


def insert_pgdb(data):
    RedditPost.objects.create(**data)
    # db.execute(meta.tables[table].insert(), data)exit()
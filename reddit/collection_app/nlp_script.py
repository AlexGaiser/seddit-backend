

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
import psycopg2, numpy
from sqlalchemy.sql.expression import func


from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base



from textblob import TextBlob

# import reddit.collection_app.schema as sc
from reddit.collection_app.insert_pgdb import insert_pgdb
# from reddit.collection_app.cfg import meta, db, dbname

# Session = sessionmaker(bind = db)


# session = Session()
# search2 = session.query(Content).filter_by(reviewid = 16).first()

def sentiment(queryset, query):
    polarity = []
    subjectivity = []
    
    for instance in queryset:
        if instance.title:
            title_blob = TextBlob(instance.title)
            polarity.append(title_blob.sentiment.polarity)
            subjectivity.append(title_blob.sentiment.subjectivity)
            print("title polarity:"  + str(title_blob.sentiment.polarity))
            print('title subjectivity' + str(title_blob.sentiment.subjectivity))  
        if instance.body:
            body_blob = TextBlob(instance.body)
            polarity.append(body_blob.sentiment.polarity)
            subjectivity.append(body_blob.sentiment.subjectivity)
             #         # try:
    
    data = {"polarity":numpy.mean(polarity),
            "subjectivity": numpy.mean(subjectivity),
            "query": query
        }
    # insert_pgdb(dbname, 'nlp_record', data)

    # insert_pgdb(data)
    
    
    return data
    # search2 = session.query(sc.RedditHot).filter(func.length(sc.RedditHot.body) > 1000).first()

    # print(search2)
    # search_blob = TextBlob(search2.body)
    # print("raw version sentiment %s" % str(search_blob.sentiment))


# def spacy_sentiment(table):
#     if not table in meta.tables:
#         sc.create_table_nlp(table)

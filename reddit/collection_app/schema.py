from sqlalchemy import create_engine, Table, Column, Integer, String, Float, ForeignKey

from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base

from reddit.collection_app.cfg import db, meta

# engine = create_engine('postgresql+psycopg2:///django1', echo=True)
Base = declarative_base()



class RedditNew(Base):
    __tablename__ = "reddit_posts_new"
    
    id = Column('id', Integer, primary_key = True)
    post_id = Column('post_id', String )
    title = Column('title', String)
    body = Column('body', String)
    karma = Column('karma', Integer)
    subreddit = Column('subreddit', String)
    submission_link_url = Column("submission_link_url", String)
    submission_url = Column("submission_url", String)
    date_time = Column('date_time', String)
    collected_date = Column("collected_date", String)



    def __repr__(self):
        return "<Posts(post_id= '%s', title= '%s', body= '%s', karma= '%s', subreddit= '%s', submission_link_url = '%s')>" % (self.post_id, self.title, self.body, self.karma, self.subreddit,self.submission_link_url)

class RedditHot(Base):
    __tablename__ = "reddit_posts_hot"
    
    id = Column('id', Integer, primary_key = True)
    post_id = Column('post_id', String )
    title = Column('title', String)
    body = Column('body', String)
    karma = Column('karma', Integer)
    subreddit = Column('subreddit', String)
    submission_link_url = Column("submission_link_url", String)
    submission_url = Column("submission_url", String)
    date_time = Column('date_time', String)
    collected_date = Column("collected_date", String)


    def __repr__(self):
        return "<Posts(post_id= '%s', title= '%s', body= '%s', karma= '%s', subreddit= '%s', submission_link_url = '%s')>" % (self.post_id, self.title, self.body, self.karma, self.subreddit,self.submission_link_url)


class RedditRising(Base):
    __tablename__ = "reddit_posts_rising"
    
    id = Column('id', Integer, primary_key = True)
    post_id = Column('post_id', String )
    title = Column('title', String)
    body = Column('body', String)
    karma = Column('karma', Integer)
    subreddit = Column('subreddit', String)
    submission_link_url = Column("submission_link_url", String)
    submission_url = Column("submission_url", String)
    date_time = Column('date_time', String)
    collected_date = Column("collected_date", String)



    def __repr__(self):
        return "<Posts(post_id= '%s', title= '%s', body= '%s', karma= '%s', subreddit= '%s', submission_link_url = '%s')>" % (self.post_id, self.title, self.body, self.karma, self.subreddit,self.submission_link_url)

def create_table_nlp(name):
            'creating table'
            new_table = Table(name, meta,
            Column('id', Integer, primary_key = True),
            Column('post_id', String, unique= True),
            Column('sentiment_polarity', Integer),
            Column('sentiment_subjectivity', String),
            )
            meta.create_all(db)


def create_table_reddit(name):
            'creating table'
            new_table = Table(name, meta,
            Column('id', Integer, primary_key = True),
            Column('post_id', String, unique= True),
            Column('title', String),
            Column('body', String),
            Column('karma', Integer),
            Column('subreddit', String),
            Column("submission_link_url", String),
            Column("submission_url", String),
            Column('date_time', String),
            Column("collected_date", String)
            )
            
            meta.create_all(db)


def subreddit_search(subreddit):
    return 

def search_db(search):
    return 

Base.metadata.create_all(db)
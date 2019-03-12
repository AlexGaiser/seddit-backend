
import reddit.collection_app.schema as sc
import praw, time, pdb, re, os, csv, datetime

import reddit.collection_app.cfg as cfg
# from reddit.collection_app.cfg import meta, db
from reddit.collection_app.insert_pgdb import insert_pgdb
from reddit.collection_app.nlp_script import sentiment

def get_reddit_data(**kwargs):
    subreddit = kwargs['subreddit']
    sort= kwargs['sort'] 
    limit = kwargs['limit']

    r = praw.Reddit(username = cfg.username,
                    password = cfg.password,
                    client_id = cfg.client_id,
                    client_secret = cfg.client_secret,
                    user_agent = 'RavenousDataBot test friendship maker v0.1')

    subreddit = r.subreddit(subreddit)
    
    sub_sort = ''

    table = "reddit_posts"

    if sort == "new":
        sub_sort = subreddit.new(limit = limit)
    elif sort == "top":
        sub_sort = subreddit.top(limit = limit)
    elif sort == "controversial":
        sub_sort = subreddit.controversial(limit = limit)
    elif sort == "rising":
        sub_sort= subreddit.rising(limit = limit)
    elif sort == "top":
        filter = kwargs['filter']
        sub_sort = subreddit.top(time_filter = filter, limit = limit)
    else:
        sub_sort = subreddit.hot(limit = limit)
    

    repeated_post = 0

    for submission in sub_sort:
        post_dict={
            "post_id" : str(submission.id),
            "title" : str(submission.title),
            "body" : str(submission.selftext),
            "karma" : int(submission.score),
            "date_time" : str(datetime.datetime.fromtimestamp(int(submission.created)).strftime('%Y-%m-%d %H:%M:%S')),
            "subreddit" : str(submission.subreddit),
            "submission_link_url": str(submission.url),
            "submission_url": str(submission.permalink),
            "collected_date" : str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            }
        print(post_dict)
        
        # if not table in meta.tables:
        #     sc.create_table_reddit(table)
        try:
            insert_pgdb(post_dict)

            # insert_pgdb(cfg.dbname, table, post_dict)
        except:
            repeated_post +=1
            print('not able to insert')
            if repeated_post >=20:
                break

    print("collection finished")

def reddit_search(search):
    subreddit = 'all'
    table = "reddit_posts"
    repeated_post = 0

     
    r = praw.Reddit(username = cfg.username,
                    password = cfg.password,
                    client_id = cfg.client_id,
                    client_secret = cfg.client_secret,
                    user_agent = 'RavenousDataBot test friendship maker v0.1')
                    
    subreddit = r.subreddit(subreddit)
    sub_search = subreddit.search(search, sort = 'relevance', limit=1000)
    
    
    
    for submission in sub_search:
        post_dict={
            "post_id" : str(submission.id),
            "title" : str(submission.title),
            "body" : str(submission.selftext),
            "karma" : int(submission.score),
            "date_time" : str(datetime.datetime.fromtimestamp(int(submission.created)).strftime('%Y-%m-%d %H:%M:%S')),
            "subreddit" : str(submission.subreddit),
            "submission_link_url": str(submission.url),
            "submission_url": str(submission.permalink),
            "collected_date" : str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            }
        print(post_dict)
    
        # if not table in meta.tables:
        #     sc.create_table_reddit(table)
        try:
            insert_pgdb(post_dict)

            # insert_pgdb(cfg.dbname, table, post_dict)
        except:
            repeated_post +=1
            if repeated_post >=20:
                break



# if __name__ == '__main__':
#     get_reddit_data(subreddit="all", sort="new", limit=1000)
#     get_reddit_data(subreddit="all", sort="hot", limit=1000)
#     get_reddit_data(subreddit="all", sort="controversial", limit=1000)
#     get_reddit_data(subreddit="all", sort="rising", limit=1000)
    # get_reddit_data(subreddit="all", sort = "top", filter = 'all', limit = 1000)
from  collection_app import geddit

def script ():
    print('hello world')
    geddit.get_reddit_data(subreddit="all", sort="new", limit=1000)
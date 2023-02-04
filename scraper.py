import praw
#import pandas as pd

reddit_read_only = praw.Reddit(client_id="BADD-RyGlOxA7-G-FsIqxA",
                               client_secret="c1hpbMp_VGHThdf5ydT-IaWxP6tB3A",
                               user_agent="Mtang1217")
def scraper(s): 
    subreddit = reddit_read_only.subreddit(s)
    print("Display Name:", subreddit.display_name)
    print("Title:", subreddit.title)
    #print("Description:", subreddit.description)

    for post in subreddit.hot(limit=5):
        print(post.title)
        print()

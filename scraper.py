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
    count = 0
    postlist = []
    print("Top 5 Hot Posts of " + subreddit.display_name + ":")
    for post in subreddit.hot(limit=5):
        postlist.append(post)
        count+=1
        print(str(count) + ". " + post.title)
        print(post.url)
        print()
    result = input("If you would like to read the contents of a post, input the number of the post\nType \"comments\" if you would like to see the top comments of a post\n> ") 
    if result.isdigit():
        print(postlist[int(result) - 1].selftext)
    elif result == "comments":
        comments(input("Input URL: \n> "))
    
def comments(link):
    submission = reddit_read_only.submission(url=link)
    count = 0
    limit = 5
    for comment in submission.comments:
        count+=1
        print(str(count)+ ". " + comment.body)
        print()
        if count >= limit:
            if input("Would you like more comments? \n> ").lower() == ("yes"):
                limit += 5
            else:
                break
            
def gamehelp(game):
    count = 0
    submissionlist = []
    for submission in reddit_read_only.subreddit("all").search(game + " guide"):
        submissionlist.append(submission)
        count+=1
        print(str(count) + ". " + submission.title)
        print(submission.url)
        print()
        if count >= 5:
            result = input("If you would like to read the contents of a post, input the number of the post\n> ") 
            if result.isdigit():
                print(submissionlist[int(result) - 1].selftext)
            break
        
def subsearch(keywords):
    x = []
    x = keywords.split()
    count = 0
    submissionlist = []
    for submission in reddit_read_only.subreddit(x[0]).search(x[1]):
        submissionlist.append(submission)
        count+=1
        print(str(count) + ". " + submission.title)
        print(submission.url)
        print()
        if count >= 5:
            result = input("If you would like to read the contents of a post, input the number of the post\n> ") 
            if result.isdigit():
                print(submissionlist[int(result) - 1].selftext)
            break
            
def search(keywords):
    count = 0
    submissionlist = []
    for submission in reddit_read_only.subreddit("all").search(keywords):
        submissionlist.append(submission)
        count+=1
        print(str(count) + ". " + submission.title)
        print(submission.url)
        print()
        if count >= 5:
            result = input("If you would like to read the contents of a post, input the number of the post\n> ") 
            if result.isdigit():
                print(submissionlist[int(result) - 1].selftext)
            break


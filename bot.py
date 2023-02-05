# bot.py

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging
from scraper import *
import webbrowser

logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)

chatbot = ChatBot("HackBot")

trainer = ListTrainer(chatbot)
'''
trainer.train([
    "Hi",
    "Welcome, friend!",
    ])
'''

corpus_trainer = ChatterBotCorpusTrainer(chatbot)
corpus_trainer.train('chatterbot.corpus.english')

exit_conditions = (":q", "quit", "exit")

print("Welcome to the Hackbot!\nA friendly chatbot that can provide video game help and search through reddit")
print("Type \"help\" for more options")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    elif query in "help":
        print("Type \"reddit\" for the top posts of your favorite subreddits!")
        print("     \"search\" for a general search through reddit with keywords")
        print("     \"subredditsearch\" for a search through a specific subreddit with keywords")
        print("     \"comments\" for the top comments of a reddit post")
        print("     \"gamehelp\" for advice on video games")
    elif query in "gamehelp":
        gamehelp(input("Which game? \n> "))
    elif query in "search":
        search(input("Input keywords \n> "))
    elif query in "subredditsearch":
        subsearch(input("Input subreddit and keywords in format \"Subreddit Keyword\"\n> "))
    elif query in "reddit":
        scraper(input("which subreddit? \n> "))
    elif query in "comments":
        comments(input("Input URL: \n> "))
    else:
        print(f"{chatbot.get_response(query)}")

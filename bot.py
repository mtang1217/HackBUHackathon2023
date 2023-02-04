# bot.py

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging
from scraper import *

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
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    elif query in "help":
        print("HELP")
    elif query in "reddit":
        scraper(input("which subreddit"))
    else:
        print(f"{chatbot.get_response(query)}")

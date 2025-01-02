#!/usr/bin/env python
# coding: utf-8

# # Funções

# ## Importing libs

import os
import requests
import tweepy
from datetime import datetime as dt

# ## Auth

# Setting up OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Setting up Twitter API keys with tweepy.Client
tt = tweepy.Client(
    #Consumer Keys
    consumer_key= os.environ['CONSUMER_KEY'],
    consumer_secret= os.environ['CONSUMER_SECRET'],
    # Access Token and Secret
    access_token= os.environ['ACCESS_TOKEN'],
    access_token_secret= os.environ['ACCESS_TOKEN_SECRET'])

# ## Defining Functions

import random

# Function to create a random prompt for tweet generation
def generate_prompt() -> str:
    # Example of creating a random prompt for generating tech, inspiration, personal development, or quirky content
    categories = ['tech', 'inspiration', 'personal development', 'quirky', 'funny']
    category = random.choice(categories)

    if category == 'tech':
        options = [
            "Write a tweet about the latest technology trends in AI.",
            "What is the most exciting thing happening in tech today?",
            "Share an insight about the future of AI that will blow people's minds."
        ]
        return random.choice(options)

    elif category == 'inspiration':
        options = [
            "Write an inspirational tweet to kickstart someone's day.",
            "Share a motivational thought to help someone overcome their challenges.",
            "Give a quick pep talk to remind people they can achieve anything."
        ]
        return random.choice(options)

    elif category == 'personal development':
        options = [
            "Write a tweet about how personal growth is a journey, not a destination.",
            "Share an idea for improving one small habit today.",
            "Give a tip on how to break free from a comfort zone."
        ]
        return random.choice(options)

    elif category == 'quirky':
        options = [
            "Write a quirky tweet about the wonders of coffee and its magical powers.",
            "Share a fun fact about the weirdest tech gadget you've seen recently.",
            "Make a funny observation about everyday tech struggles."
        ]
        return random.choice(options)

    elif category == 'funny':
        options = [
            "Write a funny tweet about the daily struggles of being a techie.",
            "Share a light-hearted joke about productivity and procrastination.",
            "Write a witty tweet about how technology is taking over, one app at a time."
        ]
        return random.choice(options)

    else:
        return "Write a tweet about overcoming challenges with a dash of humor."


#!/usr/bin/env python
# coding: utf-8

# ## Importing libs

import os
import requests
import tweepy
import random
import openai
from datetime import datetime as dt
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# ## Auth

# Setting up OpenAI API key
# Initialize OpenAI client securely using environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # API key loaded from environment variable


tt = tweepy.Client(
    #Consumer Keys
    consumer_key= os.environ['CONSUMER_KEY'],
    consumer_secret= os.environ['CONSUMER_SECRET'],
    # Access Token and Secret
    access_token= os.environ['ACCESS_TOKEN'],
    access_token_secret= os.environ['ACCESS_TOKEN_SECRET'])




# Function to create a random prompt for tweet generation
def generate_prompt() -> str:
    # Example of creating a random prompt for generating tech, inspiration, personal development, or quirky content
    categories = ['tech', 'inspiration', 'personal development', 'quirky', 'funny']
    category = random.choice(categories)

    if category == 'tech':
        options = [
           
        ]
        return random.choice(options)

    elif category == 'inspiration':
        options = [
            "Stricly noting of the twitter text threshold, be natural,  Write an inspirational tweet to kickstart someone's day.",
            "Stricly noting of the twitter text threshold, be natural, Share a motivational thought to help someone overcome their challenges.",
            "Stricly noting of the twitter text threshold, be natural,  Give a quick pep talk to remind people they can achieve anything."
        ]
        return random.choice(options)

    elif category == 'personal development':
        options = [
            "Stricly noting of the twitter text threshold, be natural,  Write a tweet about how personal growth is a journey, not a destination.",
            "Stricly noting of the twitter text threshold, be natural,  Give a tip on how to break free from a comfort zone."
        ]
        return random.choice(options)

    elif category == 'quirky':
        options = [
            "Stricly noting of the twitter text threshold, be quircky Write a quirky tweet about the wonders of coffee and its magical powers.",
            "Stricly noting of the twitter text threshold, Make a funny observation about everyday tech struggles."
        ]
        return random.choice(options)

    elif category == 'funny':
        options = [
            "Stricly noting of the twitter text threshold,  Write a funny tweet about the daily struggles of being a techie.",
            "Stricly noting of the twitter text threshold,  Share a light-hearted joke about productivity and procrastination.",
            "Stricly noting of the twitter text threshold,  Write a witty tweet about how technology is taking over, one app at a time."
        ]
        return random.choice(options)

    else:
        return "In less than 280 tweet characters Stricly noting of the twitter text threshold, be natural Write a tweet about overcoming challenges with a dash of humor."

# Function to generate tweet content using OpenAI's GPT
def generate_tweet_from_openai(prompt: str) -> str:
    try:
        # Requesting OpenAI to generate tweet content based on the generated prompt
        completion = client.chat.completions.create(
              messages=[
                {"role": "system", "content": "You are a helpful assistant that generates tweets."},
                {"role": "user", "content": prompt}
            ],
            model="gpt-4o-mini",  # You can use any other model, like text-curie-001 or gpt-3.5-turbo
            max_tokens=280,  # Keeping the tweet under Twitter's character limit
            temperature=0.7  # Controls randomness in the output
        )

        # Extracting the text response from OpenAI
        tweet_content = completion.choices[0].message.content.strip()

        return tweet_content

    except Exception as e:
        print(f"Error generating tweet with OpenAI: {e}")
        return "Error generating tweet."
        

# Function to post the tweet using Twitter API
def post_tweet(tweet: str):
    try:
        # Posting the tweet using tweepy.Client's create_tweet method
        tt.create_tweet(text=tweet)  # 'text' is required for the new create_tweet method
        print("Tweet posted successfully!")
    except tweepy.errors.TweepyError as e:  # Catch errors using the new exception class
        print(f"Error posting tweet: {e}")

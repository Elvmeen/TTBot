#!/usr/bin/env python
# coding: utf-8

# ## Importing libs

import os
import requests
import tweepy
import random
import time
import openai
from dotenv import load_dotenv
from openai import OpenAI
from datetime import datetime


# Load environment variables from .env file
load_dotenv()

# ## 

# Setting up OpenAI API key/Auth
# Initialize OpenAI client securely using environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # API key loaded from environment variable


tt = tweepy.Client(
    #Consumer Keys
    consumer_key= os.environ['CONSUMER_KEY'],
    consumer_secret= os.environ['CONSUMER_SECRET'],
    # Access Token and Secret
    access_token= os.environ['ACCESS_TOKEN'],
    access_token_secret= os.environ['ACCESS_TOKEN_SECRET'])



import random

# Function to create a random prompt for tweet generation
def generate_prompt() -> str:
    # Categories for generating prompts
    categories = ['tech', 'personal_dev', 'humour']
    category = random.choice(categories)

    if category == 'tech':
        options = [
            "Write a first-person tweet sharing a hard-earned lesson from a recent coding challenge.",
            "Create a tweet discussing the importance of some subjecttive areas programming like quant finance or orther sectios in today's digital age.",
            "Share a tip for optimizing code performance that every developer should know.",
            "Write a tweet about the evolution of programming languages and how it’s changed the way we code.",
            "Pose a radom question about the cybersecurity/programming that encourages engagement as a tweet."
        ]
        return random.choice(options)

    elif category == 'personal_dev':
        options = [
            "Write a motivational tweet where I reflect on a moment I overcame self-doubt and how it transformed me.",
            "Create a tweet where I share a personal revelation about the importance of embracing failure as a stepping stone to success, in a very strong tone",
            "Generate an inspiring tweet where I talk about my journey of breaking free from my comfort zone and the growth that followed",
            "If your code works on the first try, did you really learn anything?",
        ]
        return random.choice(options)

    elif category == 'humour':
        options = [
            "Write a short, very emotionally charged question that sparks deep reflection.",
            "Craft a greeting that’s both humorous and strongly provocative",
            "Create a one-liner that blends intense humor and should be flirty and witty related to women",
        ]
        return random.choice(options)

    else:
        return "In less than 280 characters, write a tweet about overcoming challenges with a extreamly strong, motivational tone."

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
        

                               
## Function to post the tweet using Twitter API
def post_tweet(tweet: str):
    try:
        # Posting the tweet using tweepy.Client's create_tweet method
        tt.create_tweet(text=tweet)  # 'text' is required for the new create_tweet method
        print("Tweet posted successfully!")
    except tweepy.errors.TweepyError as e:  # Catch errors using the new exception class
        print(f"Error posting tweet: {e}")

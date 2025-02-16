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
    categories = ['tech', 'life_wisdom']
    category = random.choice(categories)

    if category == 'tech':
        options = [
            "Generate a single, engaging, first-person tweet that is punchy, candid, and thought-provoking. The tweet should share a hard-earned lesson, insight, or provocative question from the world of tech and programming. Cover topics such as coding challenges, the evolution of programming languages, cybersecurity, quant finance, or tips for optimizing code. The tone should be conversational and relatable, designed to spark reflection and engagement among tech enthusiasts, capturing both the humor and the seriousness of the tech journey, don't give output you've given before"
        ]
        return random.choice(options)

    elif category == 'life_wisdom':
        options = [
            "Generate a bold, provocative, and conversational tweet that tackles an everyday relationship dilemma, personal insecurity, or social observation with a sharp, candid tone. The tweet should be short, punchy, and designed to spark engagement, resembling a casual conversation or internal reflection about life and relationships. Provide only one response, dont use hashtags and don't give answers you've given before"
        ]
        return random.choice(options)

    else:
        return "In one powerful line, write a tweet that challenges the way we think about overcoming obstacles. Keep it sharp, unapologetic, and leave people questioning their own limits, don't give answers you've given before."


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
            temperature=0.2  # Controls randomness in the output
        )

        # Extracting the text response from OpenAI
        tweet_content = completion.choices[0].message.content.strip()

        # Remove quotes from the start and end of the tweet content if they exist
        if tweet_content.startswith('"') and tweet_content.endswith('"'):
            tweet_content = tweet_content[1:-1]

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
    except tweepy.errors.TooManyRequests as e:  # Catch rate limit error specifically
        # Check if the exception contains a response and attempt to access rate limit reset
        if hasattr(e, 'response') and e.response is not None:
            # If 'x-rate-limit-reset' is available in the response headers
            rate_limit_reset_header = e.response.headers.get('x-rate-limit-reset')
            if rate_limit_reset_header:
                rate_limit_reset = datetime.fromtimestamp(int(rate_limit_reset_header))
                wait_time = rate_limit_reset - datetime.now()
                error_message = f"{datetime.now()}: Rate limit reached. Waiting until {rate_limit_reset}. Time remaining: {wait_time}"
                print("Rate limit reached. Check your logs for the wait time.")  # Log the message, don't post to Twitter
                # Optionally, you can print out the error message or log it somewhere
                print(f"Error details (not posted to Twitter): {error_message}")
            else:
                print("Rate limit reset header not found.")
        else:
            print("Response object not available.")
    except tweepy.errors.TweepyError as e:  # Catch other Tweepy errors
        general_error_message = f"Error posting tweet: {e}"
        print("An error occurred. Check your logs for more details.")  # Log the error, don't post to Twitter
        # Optionally, you can print out the general error message or log it somewhere
        print(f"General error details (not posted to Twitter): {general_error_message}")


                               
## Function to post the tweet using Twitter API
#def post_tweet(tweet: str):
#    try:
#        # Posting the tweet using tweepy.Client's create_tweet method
#        tt.create_tweet(text=tweet)  # 'text' is required for the new create_tweet method
#        print("Tweet posted successfully!")
#    except tweepy.errors.TweepyError as e:  # Catch errors using the new exception class
#        print(f"Error posting tweet: {e}")

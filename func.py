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
            "What's the most underrated programming language today, and why?",
            "AI is advancing rapidly, but are we prepared for the ethical challenges it brings?",
            "Write a serious tweet about the importance of cybersecurity in an increasingly connected world.",
            "If you had to explain AI to someone in one sentence, what would you say?",
            "Why do some developers still prefer older languages over the new, flashy ones?",
            "Write a thought-provoking tweet on the future of machine learning in healthcare."
        ]
        return random.choice(options)

    elif category == 'inspiration':
        options = [
            "Every great tech innovation started with a single idea. What's holding you back from starting yours?",
            "When you hit a roadblock in coding, remember that every bug is a lesson in disguise.",
            "Innovation thrives in discomfort. Step out of your comfort zone today.",
            "Progress in tech is relentless, but so is your potential. Keep pushing the boundaries.",
            "Think of the tech giants today. They all started small. What’s stopping you from starting?"
        ]
        return random.choice(options)

    elif category == 'personal development':
        options = [
            "In tech, skills are your currency. What new skill will you invest in today?",
            "Personal growth in programming isn't just about new languages; it's about mastering the mindset.",
            "Discipline in learning to code can reshape your life. What's one thing you'll commit to learning today?",
            "Tech changes, but the ability to adapt remains constant. How flexible is your learning approach?",
            "Breaking out of your comfort zone isn't easy, but it's where the real growth happens. When was the last time you challenged yourself?"
        ]
        return random.choice(options)

    elif category == 'quirky':
        options = [
            "Why do programmers always mix up Halloween and Christmas? Because Oct 31 == Dec 25!",
            "If your code works on the first try, did you really learn anything?",
            "Ever notice how debugging is like being a detective in a crime movie where you are also the murderer?",
            "Code is like humor. When you have to explain it, it’s bad."
        ]
        return random.choice(options)

    elif category == 'funny':
        options = [
            "Why do Java developers wear glasses? Because they don't see sharp.",
            "I have a joke about recursion, but I’ll tell it after I explain recursion.",
            "There are 10 kinds of people in the world: those who understand binary, and those who don’t."
        ]
        return random.choice(options)

    else:
        return "In less than 280 characters, write a tweet about overcoming challenges with a strong, motivational tone."

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

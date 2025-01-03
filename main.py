#!/usr/bin/env python
# coding: utf-8

from func import generate_prompt, post_tweet  # Import the necessary functions from func.py

if __name__ == "__main__":
    # Generate a random tweet prompt
    tweet = generate_prompt()

    # Post the generated tweet using the Twitter API
    post_tweet(tweet)  # Now it will work without passing any extra arguments

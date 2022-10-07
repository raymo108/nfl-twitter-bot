#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tweepy
from GoogleNews import GoogleNews
from random import randint

client = tweepy.Client(consumer_key='YOUR_CONSUMER_KEY_HERE',
                       consumer_secret='YOUR_CONSUMER_SECRET_HERE',
                       bearer_token='YOUR_BEARER_TOKEN_HERE',
                       access_token='YOUR_ACCESS_TOKEN_HERE',
                       access_token_secret='YOUR_ACCESS_TOKEN_SECRET_HERE')

gn = GoogleNews(period='12h')
gn.get_news('nfl')
result = gn.result()

for items in result:
    title = items['title']
    link = items['link']
    
    element_info = {
        "Title": title,
        "Link": link
    }
# GoogleNews pulls articles as "items"
#Find random article in last 24 hours using randint between index 0 and the last index
article=[items][randint( 0, len([items])-1 ) ]

#construct the tweet text
tweet_text = f"In NFL News: {title}. See full article: {link}. #nfl #nflnews #football #sports"

#Fire off the tweet!

response = client.create_tweet(text=tweet_text)
print(response)


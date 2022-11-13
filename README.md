# NFL Twitter Bot
## Project Description 
This project scrapes Google News for articles related to "NFL" in the last 12 hours. Then selects a random article from that time period to create and send tweet from a user specified Twitter account. 
#### Technologies used
- ```Tweepy``` enables communication with the Twitter API to create and send tweets
- ```GoogleNews``` scrape and read articles from the Google News feature
- ```random``` tell program to pick a random article from Google News
- ```time``` to signal how long the script should "sleep" before running again

## How to Install and Run
Most importantly, any user will need to create a Twitter Developer account (https://developer.twitter.com/en/support/twitter-api/developer-account). From there, you can retrieve personal access tokens to link your twitter account. Now just open your favorite editor and install/import the packages listed above. 

Customizable options:
- ```GoogleNews(period='x')``` user can change which time period to scrape Google News
- ```gn.get_news('x')``` change which category of articles to scrape
- ```element_info = {``` change which items to actually pull from the scraped article
- ```tweet_text``` format how the tweet looks and what is included
- An infinite while loop is used to continously run the script. ```time.sleep()``` can be adjusted to change the interval on how long to wait until running the script again

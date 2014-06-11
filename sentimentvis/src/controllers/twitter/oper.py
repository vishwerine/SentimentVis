#! /usr/bin/env python

#### oper is the main file for twitter handler component , contains all the common functions like fetching tweets

import fetch_tweets

import datetime

class Tweet:
        text = ""
        user = ""
        date = datetime.datetime(2014,1,1,0,0)




def getTweets(q):
      ''' connects to twitter server and returns the tweets that match query q '''
      
      tweets = fetch_tweets.get_tweets(q)
      
      Tweets = []
      for tweet in tweets:
           if tweet.lang=="en":
                  # check for only english tweets
                  t = Tweet()
                  t.text = tweet.text
                  t.user = tweet.user.name
                  t.date = tweet.created_at
                  Tweets.append(t)
  
      
      return Tweets



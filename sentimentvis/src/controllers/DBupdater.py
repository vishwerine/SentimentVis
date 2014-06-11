#! /usr/bin/env python

### python program for updating tweets database

from twitter import oper


from sentimentvis.models import TweetObject


def update(q):
     ''' call this function to update the database with latest 100 tweets '''
     

     tweets = oper.getTweets(q)
     for tweet in tweets:
           t = TweetObject()
           t.text = tweet.text
           t.user = tweet.user
           t.date = tweet.date
           t.query = q
           t.save()
     return


     
     
     

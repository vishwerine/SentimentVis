#! /usr/env/bin python


## source code for matching emotions and sentiments from the lexicon matcher

from sentimentvis.models import TweetObject

import string
import re


def get(q):
      ''' gets top 100 from tweet database '''

      list1 = TweetObject.objects.filter(query=q).order_by('date')

          
      if len(list1) < 100:
            
            return list1
      else:
        leng = len(list1)

        for i in range(leng-100):
              list1[i].delete()
        
        return list1      
      




def processing(list1):
      ''' this does simple regular expressions based processing '''
      list2 = []
      for tweet in list1:
        #Convert to lower case
        tweet.text = tweet.text.lower()
        #Convert www.* or https?://* to URL
        tweet.text = re.sub('((www\.[\s]+)|(https?://[^\s]+))','URL',tweet.text)
        #Convert @username to AT_USER
        tweet.text = re.sub('@[^\s]+','AT_USER',tweet.text)
        #Remove additional white spaces
        tweet.text = re.sub('[\s]+', ' ', tweet.text)
        #Replace #word with word
        tweet.text = re.sub(r'#([^\s]+)', r'\1', tweet.text)
        #trim
        tweet.text = tweet.text.strip('\'"')
        list2.append(tweet)
        #end
      return list2


class LexiconTweet:
         tweet = TweetObject()
         emotion = []


def getNo(s):
      if s=="sadness":
              return 0
      elif s=="anger":
              return 1
      elif s=="fear":
              return 2
      elif s=="trust":
              return 3
      elif s=="disgust":
              return 4
      elif s=="anticipation":
              return 5
      elif s=="joy":
              return 6
      elif s=="surprise":
              return 7
      elif s=="negative":
              return 8
      else:
       return 9
          

def match(q):
     ''' fetches data from database, stores emotions as well as sentiments in database '''
     
     list1 = get(q)
     list2 = processing(list1)

     f = open('sentimentvis/src/lexicon_matcher/nrc_emotion_lexicon.txt','r')
     line = f.readline()
     lexicon = []
     while line!= "":
            s = string.split(line)
            a = []
            a.append(s[0])
            a.append(s[1])
            a.append(s[2])
            lexicon.append(a)
            line = f.readline()
     
     ans = []
     ans2 = []
     
     for i in range(10):
        ans2.append(0)

     for li in list2:
           obj0 = LexiconTweet()
           obj0.emotion = [] 
           words = string.split(li.text)
           
           for word in words:
                 for lex in lexicon:
                      if lex[0] == word:
                        if lex[2]=='1':
                            ## word found
                            n = getNo(lex[1])
                            ans2[n] = ans2[n] + 1
                            obj0.emotion.append(lex[1]) 
                            break
           
           obj0.tweet = li
           ans.append(obj0)
           
     return ans                
                   

   
       


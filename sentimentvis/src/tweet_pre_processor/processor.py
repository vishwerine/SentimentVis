#! /usr/bin/env python

### does pre-processing on tweets to be used for lexicon matching

import re


from sentimentvis.models import TweetObject


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



def pre_process(q):
         list1 = get(q)
         
         list2 = processing(list1)

         return list2


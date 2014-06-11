#! /usr/bin/env python

from sentimentvis.models import TweetObject



def get(q):
      ''' gets top 100 from tweet database '''

      list1 = TweetObject.objects.filter(query=q)

          
      if len(list1) < 100:
            
            return list1
      else:
        leng = len(list1)

        for i in range(leng-100,0,-1):
              list1[i].delete()
      
        return list1      
      




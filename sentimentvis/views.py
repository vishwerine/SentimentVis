from django.http import HttpResponse
from django.shortcuts import render

from django.template.loader import get_template
from django.template import Context

##### source packages #############


from src.controllers import DBupdater , TweetFetcher
from src.tweet_pre_processor import processor
from src.lexicon_matcher import matcher



###################################



def index(request):
      return render(request,'index.html',{})


def fetchtweets(request):
     if 'q' in request.GET.keys():
       q = request.GET['q']
       if q=="":
           return render(request,'error_no_query.html',{})
       DBupdater.update(q)
       tweetlist = TweetFetcher.get(q)
       tweetlist = sorted(tweetlist,key=lambda x:x.date, reverse=True)
       return render(request,'tweets.html',{'tweetlist':tweetlist,'q':q})
     else:
        return render(request,'error_no_query.html',{})



def preProcess(request):
        q = request.GET['q']
        list1 = processor.pre_process(q)
        
        
        return render(request,'processed_tweets.html',{'tweetlist':list1,'q':q})


class ans2Obj:
       anticipation = 0
       sadness = 0
       anger = 0
       fear = 0
       negative = 0
       positive = 0
       disgust = 0
       joy = 0
       surprise = 0
       trust = 0


def getMacro(anslist):
      ans2 = ans2Obj()
      
      for l in anslist:
          for s in l.emotion:
              
               if s=="sadness":
                 ans2.sadness = ans2.sadness + 1
               elif s=="anger":
                ans2.anger = ans2.anger + 1
               elif s=="fear":
                ans2.fear = ans2.fear + 1
               elif s=="trust":
                ans2.trust = ans2.trust + 1             
               elif s=="disgust":
                ans2.disgust = ans2.disgust + 1
               elif s=="anticipation":
                ans2.anticipation = ans2.anticipation + 1
               elif s=="joy":
                ans2.joy = ans2.joy + 1
               elif s=="surprise":
                ans2.surprise = ans2.surprise + 1
               elif s=="negative":
                ans2.negative = ans2.negative + 1
               else:
                ans2.positive = ans2.positive + 1
      return ans2   

def removeRepeatedTags(list1):
       ''' removes repeated tags of emotion '''
       for l in list1:
           emp = []
           if "sadness" in l.emotion:
               emp.append("sadness")
           if "anger" in l.emotion:
               emp.append("anger")
           if "fear" in l.emotion:
               emp.append("fear")
           if "negative" in l.emotion:
               emp.append("negative")
           if "trust" in l.emotion:
               emp.append("trust")
           if "disgust" in l.emotion:
               emp.append("disgust")
           if "anticipation" in l.emotion:
               emp.append("anticipation")
           if "joy" in l.emotion:
               emp.append("joy")
           if "surprise" in l.emotion:
               emp.append("surprise")
           if "positive" in l.emotion:
               emp.append("positive")
           l.emotion = emp
       return list1
            
       

def emotion(request):
       q = request.GET['q']
       ans = matcher.match(q)
       macro = getMacro(ans)
       ans = removeRepeatedTags(ans)
       return render(request,'lexicon_tweets2.html',{'ans':ans , 'macro':macro , 'q':q })



def topics(request):
       return render(request,'topics.html',{})

def sentiments(request):
       return render(request,'sentiments.html',{})



from django.db import models



class TweetObject(models.Model):
           text = models.CharField(max_length = 150)
           query = models.CharField(max_length = 30)
           user = models.CharField(max_length = 30)
           date = models.DateTimeField()
       

    

from django import template

register = template.Library()

@register.filter(name="samplefunc")
def sampleFunc(value):
     return value


@register.filter(name="percen")
def percen(value,args):
      ans = value
      su = ans.trust + ans.sadness + ans.disgust + ans.anticipation + ans.surprise + ans.joy + ans.fear + ans.anger
      
      if args=="sadness":
             return ans.sadness*100.0/su
      elif args=="anger":
             return ans.anger*100.0/su
      elif args=="fear":
             return ans.fear*100.0/su
      elif args=="trust":
             return ans.trust*100.0/su
      elif args=="disgust":
             return ans.disgust*100.0/su
      elif args=="anticipation":
             return ans.anticipation*100.0/su
      elif args=="joy":
             return ans.joy*100.0/su
      elif args=="surprise":
             return ans.surprise*100.0/su

@register.filter(name="posinegi")
def posinegi(value,args):
         ans = value
         su = ans.positive + ans.negative
         
         if args=="up":
             return ans.positive*100/su
         elif args=="down":
             return ans.negative*100/su

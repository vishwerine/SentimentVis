from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


from views import index, fetchtweets, preProcess , topics, sentiments , emotion

urlpatterns = patterns('',
    (r'^index/$',index),
    (r'^tweets/$',fetchtweets),
    (r'^update/$',fetchtweets),
    (r'^tweetPreProcess/$',preProcess),
    (r'^topics/$',topics),
    (r'^sentiments/$',sentiments),
    (r'^emotion/$',emotion),
 
    # Examples:
    # url(r'^$', 'sentimentvis.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

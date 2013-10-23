from django.conf.urls import patterns, url

urlpatterns = patterns('fabsvc.views',
    url(r'^$', 'index'),
    url(r'^service/$', 'service'),
)


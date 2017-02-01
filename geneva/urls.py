from django.conf.urls import url
from . import views

app_name = 'geneva'
urlpatterns = [
    # Geneva Home
    url(r'^$', views.index, name='index'),
    # Url by record ID geneva/1
    url(r'^(?P<geneva_id>[0-9]+)/$', views.geneva_record, name='geneva_record'),
    # log redirect
    url(r'^(?P<geneva_id>[0-9]+)/redirect/$', views.redirect, name='redirect'),

]

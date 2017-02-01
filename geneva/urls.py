from django.conf.urls import url
from . import views

app_name = 'geneva'
urlpatterns = [
    # Geneva Home
    url(r'^$', views.IndexView.as_view(), name='index'),
    # Url by record ID geneva/1
    url(r'^(?P<pk>[0-9]+)/$', views.RecordView.as_view(), name='geneva_record'),
    # url(r'^(?P<geneva_id>[0-9]+)/$', views.geneva_record, name='geneva_record'),
]

from django.conf.urls import url
from . import views

app_name = 'geneva'
urlpatterns = [
    # Geneva Home
    url(r'^$', views.IndexView.as_view(), name='index'),
    # Url by record ID geneva/1
    url(r'^(?P<pk>[0-9]+)/$', views.RecordView.as_view(), name='geneva_record'),
    # /geneva_record/add
    url(r'geneva_record/add/$', views.RecordCreate.as_view(), name='record-add'),
]

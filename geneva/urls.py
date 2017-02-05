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
    # /geneva_record/1
    url(r'geneva_record/(?P<pk>[0-9]+)/$', views.RecordUpdate.as_view(), name='record-update'),
    # /geneva_record/1/delete
    url(r'geneva_record/(?P<pk>[0-9]+)/delete$', views.RecordDelete.as_view(), name='record-delete'),
]

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(test)', views.retrieve, name='retrieve'),
    # alternative URL site for JSON examples
    #url(r'^(?P<result_id>[0-9]+)', views.retrieve, name='retrieve'),
]

from django.conf.urls import url
from . import views
app_name = 'note'

urlpatterns = [
    url(r'^$', views.index, name='indexpage')
]
from django.urls import path
from . import views
#showing the path 
urlpatterns = [
    path("",views.hello,name ='hello'),
    path("start/",views.start,name='start'),
    path("site/",views.site,name ='site')
 ]

from django.conf.urls import url 

from . import views

urlpatterns = [
    url(r'blogpost',views.blogpost,name='blogpost'),
    url(r'blog',views.index,name='index'),
    url(r'login',views.login,name='login'),
    url(r'mauri',views.mauritius,name='mauritius'),
    url(r'beach',views.beach,name='cover'),
    url(r'confirm',views.confirm,name='confirm'),
    url(r'sunset',views.sunset,name='cover'),
    url(r'home',views.home,name='home'),
    url(r'',views.cover,name='cover')
]

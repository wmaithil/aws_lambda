from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'blog',views.index,name='index'),
    url(r'login',views.login,name='signin'),
    url(r'home',views.home,name='home'),
    url(r'',views.cover,name='cover')
   
]

from django.conf.urls import url 
from . import views

urlpatterns = [
     
    # blog_pages urls
    url(r'mauri',views.mauritius,name='mauritius'),
    url(r'beach',views.beach,name='beach'),
    url(r'confirm',views.confirm,name='confirm'),
    url(r'sunset',views.sunset,name='sunset'),
    url(r'home',views.home,name='home'),
    #authentication urls
    url(r'signup',views.signup,name='signup'),
    url(r'login',views.handleLogin,name='handleLogin'),
    url(r'logout',views.handleLogout,name='handleLogout'),
     url(r'^$', views.blog, name='blog')  
]

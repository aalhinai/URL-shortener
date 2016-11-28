"""URLshortenerSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
#from URLshortenerApp import views as v
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from URLshortenerApp.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', v.index),                                                      #ABD added
    #url(r'^accounts/login/$', v.login, name='login'),             #ABD added
    #url(r'^accounts/auth/$',  v.auth_view),         #ABD added
    #url(r'^home/$', v.home),                                                  #ABD added
    #url(r'^register/$', v.register),                                          #ABD added
    #url(r'^register/success/$', v.register_success),                          #ABD added
    #url(r'^accounts/login/$', 'django.contrib.auth.views.URLshortenerApp'),             #ABD added
    #url(r'^logout/$', v.logout_page),                                         #ABD added
    url(r'^$', login),
    url(r'^home/$', home),
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^accounts/login/$', login),
    url(r'^logout/$', logout_page),
]

#urlpatterns += staticfiles_urlpatterns()

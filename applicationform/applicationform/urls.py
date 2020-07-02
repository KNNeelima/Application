"""applicationform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from testapp.views import index_view,rg1_view,Thanks_view,list_of_applicaions,logout_view,signup_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index',index_view),
    url(r'^rg',rg1_view),
    url(r'^Thanks',Thanks_view),
    url(r'^list',list_of_applicaions),
    url(r'^logout/',logout_view),
    url(r'^signup/',signup_view),
    url(r'^accounts/', include('django.contrib.auth.urls')),

]

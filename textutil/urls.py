"""textutil URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


# code for practice
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',views.index,name='index'),
#     path('about/',views.about,name ='about')
#
# ]


# now using sinmple method
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index, name="index"),
#     path('rmpunc', views.rmpunc, name="rmpunc"),
#     path('capfirst', views.capfirst, name="capfirst"),
#     path('newlineremove', views.newlineremove, name="newlineremove"),
#     path('spaceremover', views.spaceremover, name="spaceremover"),
#     path('charcount', views.charcount, name="charcount")
#
# ]


# now use diffrent method and givee only one output

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('analyze', views.analyze, name="analyze")

]
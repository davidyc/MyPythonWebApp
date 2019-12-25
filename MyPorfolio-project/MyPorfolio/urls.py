"""MyPorfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import jobs.views
import evolution.views
import simplebot.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.main, name ='Home'),
    path('jobs/<int:job_id>', jobs.views.details, name='detail'),
    path('devinfo/<int:dev_id>', jobs.views.devinfo, name='devinfo'),
    path('jobs/evo', evolution.views.main, name='evo'),
    path('jobs/evo/themes', evolution.views.themes, name='themes'),
    path('jobs/evo/phases', evolution.views.phases, name='phases'),
    path('jobs/evo/addphases', evolution.views.addphases, name='addphases'),
    path('jobs/bot', simplebot.views.main, name='bot'),
    path('jobs/bot/dialog', simplebot.views.dialog, name='dialog'),
] 

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) 
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
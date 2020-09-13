from django.contrib import admin
from django.urls import path, include
import jobs.views
import evolution.views
import simplebot.views
import mymenu.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.main, name ='Home'),
    path('jobs/speedtest/', jobs.views.external, name ='speedtest'),
    path('jobs/<int:job_id>', jobs.views.details, name='detail'),
    path('devinfo/<int:dev_id>', jobs.views.devinfo, name='devinfo'),
    path('jobs/evo/', include('evolution.urls')),
    path('jobs/bot/', include('simplebot.urls')),    
    path('jobs/mymenu/', include('mymenu.urls')),
   
] 

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) 
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
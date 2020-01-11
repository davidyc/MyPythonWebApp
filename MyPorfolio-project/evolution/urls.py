from django.urls import path, include
import evolution.views


urlpatterns = [
    path('', evolution.views.main, name='evo'),
    path('themes', evolution.views.themes, name='themes'),
    path('phases', evolution.views.phases, name='phases'),
    path('addphases', evolution.views.addphases, name='addphases'),
] 

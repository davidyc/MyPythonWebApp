from django.urls import path, include
import voice.views

urlpatterns = [    
    path('', voice.views.main, name='voite'),

 
    
] 

from django.urls import path, include
import simplebot.views

urlpatterns = [
    path('', simplebot.views.main, name='bot'),
    path('dialog', simplebot.views.dialog, name='dialog'),
] 

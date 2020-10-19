from django.urls import path, include
import voice.views

urlpatterns = [    
    path('', voice.views.main, name='voite'),
    path('voite', voice.views.voite, name='voited'),
    path('showall', voice.views.show_allvoites, name='showall'),   
    path('showcount', voice.views.show_count, name='showcount'),   
    path('delete/<int:voice_id>', voice.views.detele_voice, name='deletevoice'),
    
] 

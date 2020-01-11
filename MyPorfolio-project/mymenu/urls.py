from django.urls import path, include
import mymenu.views

urlpatterns = [    
    path('', mymenu.views.main, name='mymenu'),
    path('addprod', mymenu.views.addproduct, name='addproduct'),
    path('login', mymenu.views.signup, name='login'),
] 

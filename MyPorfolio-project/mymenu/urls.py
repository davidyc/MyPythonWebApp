from django.urls import path, include
import mymenu.views

urlpatterns = [    
    path('', mymenu.views.main, name='mymenu'),
    path('addprod', mymenu.views.addproduct, name='addproduct'),
    path('singup', mymenu.views.signup, name='menusingup'),
    path('loginmenu', mymenu.views.loginmenu, name='loginmenu'),
    path('logoutmenu', mymenu.views.logoutmenu, name='logoutmenu'),
] 

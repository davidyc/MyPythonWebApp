from django.urls import path, include
import mymenu.views

urlpatterns = [    
    path('', mymenu.views.main, name='mymenu'),
    
    path('singup', mymenu.views.signup, name='menusingup'),
    path(r'loginmenu', mymenu.views.loginmenu, name='loginmenu'),
    path('logoutmenu', mymenu.views.logoutmenu, name='logoutmenu'),    
    path('allproduct', mymenu.views.showproduct, name='allproduct'),
    path('addprod', mymenu.views.addproduct, name='addproduct'),

    #apipart
    path('api/allproduct', mymenu.views.ProductView.as_view()),
    path('api/allproduct/<int:pk>', mymenu.views.ProductView.as_view()),

 
    
] 

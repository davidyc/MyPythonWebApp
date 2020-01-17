from django.urls import path, include
import mymenu.views

urlpatterns = [    
    path('', mymenu.views.main, name='mymenu'),
    
    path('singup', mymenu.views.signup, name='menusingup'),
    path(r'loginmenu', mymenu.views.loginmenu, name='loginmenu'),
    path('logoutmenu', mymenu.views.logoutmenu, name='logoutmenu'),    
    path('allproduct', mymenu.views.showproduct, name='allproduct'),
    path('addprod', mymenu.views.addproduct, name='addproduct'),
    path('alldish', mymenu.views.showdish, name='alldish'),
    path('adddish', mymenu.views.adddish, name='adddish'),
    path('dish/<int:dish_id>', mymenu.views.dishinfo, name='dishinfo'),
    path('deleteing/<int:ing_id>', mymenu.views.deleteing, name='deleteing'),
    path('adding/<int:ing_id>', mymenu.views.adding, name='adding'),

    #apipart
    path('api/allproduct', mymenu.views.ProductView.as_view()),
    path('api/allproduct/<int:pk>', mymenu.views.ProductView.as_view()),

 
    
] 

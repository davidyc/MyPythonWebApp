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
    path('adding/<int:dish_id>', mymenu.views.adding, name='adding'),
    path('createweek', mymenu.views.createweek, name='createweek'),


    #apipart
    path('api/allproduct', mymenu.views.apiallprod),
    path('api/product/<int:pk>', mymenu.views.apiprod),
    path('api/allcategory', mymenu.views.apiallcat),
    path('api/category/<int:pk>', mymenu.views.apicat),
    path('api/alldish', mymenu.views.apialldish),
    path('api/dish/<int:pk>', mymenu.views.apidish),
    path('api/alling', mymenu.views.apialling),
    path('api/ing/<int:pk>', mymenu.views.apiing),
    path('api/allweek', mymenu.views.apiallweek),
    path('api/week/<int:pk>', mymenu.views.apiweek),
    path('api/alllistdish', mymenu.views.apialllistdish),
    path('api/listdish/<int:pk>', mymenu.views.apilistdish),


 
    
] 

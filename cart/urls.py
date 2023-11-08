
from .views import *
from django.urls import path,include


urlpatterns = [

    path('cart' , cart , name="cart"),
    path('index', index, name='index'),
    path('crops/', crops, name='crops'),
     path('crops_list/', crops_list, name='crops_list'),
    path('process_language/', process_language, name='process_language'),  # Add this URL pattern
        
]
from django.urls import path
from . import views
   
urlpatterns=[path('search', views.search, name='search'),path('<slug:slug>',views.product_deets),path('<slug:slug>',views.category_view)]

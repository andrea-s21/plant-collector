from django.urls import path 
from . import views 

urlpatterns = [ 
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('plants/', views.plants_index, name='index'),
    path('plants/<int:plant_id>/', views.plants_detail, name='detail'),
    path('plants/create/', views.PlantCreate.as_view(), name='plants_create'),
    path('plants/<int:pk>/update/', views.PlantUpdate.as_view(), name='plants_update'),
    path('plants/<int:pk>/delete/', views.PlantDelete.as_view(), name='plants_delete'),
    path('plants/<int:plant_id>/add_watering/', views.add_watering, name='add_watering'),
    path('plants/<int:plant_id>/assoc_category/<int:category_id>/', views.assoc_category, name='assoc_category'),
    path('plants/<int:plant_id>/remove_category/<int:category_id>/', views.remove_category, name='remove_category'),
    path('categories/', views.CategoryList.as_view(), name="categories_index"),
    path('categories/<int:pk>/', views.CategoryDetail.as_view(), name='categories_detail'),
    path('categories/create/', views.CategoryCreate.as_view(), name='categories_create'),
    path('categories/<int:pk>/update/', views.CategoryUpdate.as_view(), name='categories_update'),
    path('categories/<int:pk>/delete/', views.CategoryDelete.as_view(), name='categories_delete'),
]
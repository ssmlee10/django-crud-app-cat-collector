from django.urls import path
from . import views

urlpatterns = [
  # 3 arguments
  # 1. empty string, index path
  # 2. we will define a home function that runs when this path is reached
  # 3. string of name = 'home'

  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('cats/', views.cat_index, name='cat-index'),
  path('cats/<int:cat_id>/', views.cat_detail, name='cat-detail'),
  path('cats/create/', views.CatCreate.as_view(), name='cat-create'),
  path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cat-update'),
  path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cat-delete'),
]

# now route is defined, we need to define the views.home
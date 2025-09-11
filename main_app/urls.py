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
  path('cats/<int:cat_id>/add-feeding/', views.add_feeding, name='add-feeding'),
  path('toys/create/', views.ToyCreate.as_view(), name='toy-create'),
  path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toy-detail'),
  path('toys/', views.ToyList.as_view(), name='toy-index'),
  path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toy-update'),
  path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toy-delete'),
  path('cats/<int:cat_id>/assoicate-toy/<int:toy_id>/', views.associate_toy, name='associate-toy')
]

# pk = primary key
# we have an instance that is already created
# class based view, if you want to change it to pk
# this is what django likes to use (int:pk)
# now route is defined, we need to define the views.home
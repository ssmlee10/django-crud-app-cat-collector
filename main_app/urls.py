from django.urls import path
from . import views

urlpatterns = [
  # 3 arguments
  # 1. empty string, index path
  # 2. we will define a home function that runs when this path is reached
  # 3. string of name = 'home'
  # first route we are defining that we are associating with view function
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
]

# now route is defined, we need to defined the views.home

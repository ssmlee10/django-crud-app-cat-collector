from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cat
# from django.http import HttpResponse

# class Cat:
#   def __init__(self, name, breed, description, age):
#     self.name = name
#     self.breed = breed
#     self.description = description
#     self.age = age

# cats = [
#   Cat('Lolo', 'tabby', 'Kinda rude.', 3),
#   Cat('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
#   Cat('Fancy', 'bombay', 'Happy fluff ball.', 4),
#   Cat('Bonk', 'selkirk rex', 'Meows loudly.', 6)
# ]

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cat_index(request):
  cats = Cat.objects.all()
  return render(request, 'cats/index.html', {'cats': cats})

#1. request
#2. page linked
#3. dictionary called cats
# very similar to callbacks in express

def cat_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  return render(request, 'cats/detail.html', {'cat': cat})

class CatCreate(CreateView):
  model = Cat
  fields = '__all__'

class CatUpdate(UpdateView):
  model = Cat
  fields = ['breed', 'description', 'age']
  # name field not included so they can't edit the cat's name!

class CatDelete(DeleteView):
  model = Cat
  success_url = '/cats/'
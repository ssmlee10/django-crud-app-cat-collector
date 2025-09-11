from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Cat, Toy
from .forms import FeedingForm
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
  # create an instance of the feeding form
  feeding_form = FeedingForm()
  return render(request, 'cats/detail.html', {'cat': cat, 'feeding_form': feeding_form})
# this makes this form available (not display yet) to the cat detail page

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

def add_feeding(request, cat_id):
  # create a ModelForm instance using the data in request.POST
  # prepare the data for the database
  form = FeedingForm(request.POST)

    #checks to see if the form data is valid for form specifications, data types matching, etc.
  if form.is_valid():
    # after checking, save form with commit=False, which returns in-memory model ojbect so we can assign cat_id before actually saving to database
    new_feeding = form.save(commit=False)
    new_feeding.cat_id = cat_id
    new_feeding.save()
  return redirect('cat-detail', cat_id=cat_id)

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'
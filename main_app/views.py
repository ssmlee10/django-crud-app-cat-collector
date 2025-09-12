from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Cat, Toy
from .forms import FeedingForm
# from django.http import HttpResponse

# def home(request):
#   return render(request, 'home.html')

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def cat_index(request):
  # display only user's cats
  cats = Cat.objects.filter(user=request.user)
  return render(request, 'cats/index.html', {'cats': cats})

#1. request
#2. page linked
#3. dictionary called cats
# very similar to callbacks in express

def cat_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  # fetch all toys
  # toys = Toy.objects.all()
  toys_cat_doesnt_have = Toy.objects.exclude(id__in = cat.toys.all().values_list('id'))
  # create an instance of the feeding form
  feeding_form = FeedingForm()
  return render(request, 'cats/detail.html', {'cat': cat, 'feeding_form': feeding_form, 'toys': toys_cat_doesnt_have},)
# this makes this form available (not display yet) to the cat detail page

class CatCreate(CreateView):
  model = Cat
  fields = ['name', 'breed', 'description', 'age']

  # associates a user with a cat
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  # built in auth assigns object to user

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

def associate_toy(request, cat_id, toy_id):
  Cat.objects.get(id=cat_id).toys.add(toy_id)
  return redirect('cat-detail', cat_id=cat_id)

def remove_toy(request, cat_id, toy_id):
  cat = Cat.objects.get(id=cat_id)
  toy = Toy.objects.get(id=toy_id)
  cat.toys.remove(toy)

  return redirect('cat-detail', cat_id=cat_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect('cat-index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
    # Same as: 
    # return render(
    #     request, 
    #     'signup.html',
    #     {'form': form, 'error_message': error_message}
    # )
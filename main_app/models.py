from django.db import models
from django.urls import reverse

MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner'),
  # first is the lette that goes into database, second is the user friendly value for meal
  # represents the drop down selection
)

class Cat(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('cat-detail', kwargs={ 'cat_id': self.id })

class Feeding(models.Model):
  date = models.DateField('Feeding Date')
  meal = models.CharField(
    max_length=1,
    choices = MEALS,
    default = MEALS[0][0]
  )
  cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
  # first argument is Cat model
  # meal has to be created and has to be associated with this specific cat
  # if the cat happens to be deleted, the associated meals will also be deleted (cascade)

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"
  # method that automatically gets the human friendly value of breakfast, lunch, dinner
  #override dunder string method

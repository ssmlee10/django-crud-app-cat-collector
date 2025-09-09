from django.contrib import admin
from .models import Cat

# Register your models here.
# this brings in the cat model into the admin site
admin.site.register(Cat)
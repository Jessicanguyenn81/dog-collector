from django.shortcuts import render
from django.http import HttpResponse

class Dog:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

dogs = [
    Dog('Chubbs', 'Bulldog', 'chubby and sweet', 3),
    Dog('Maui', 'Pomsky', 'always hungry and active', 5),
    Dog('Kobe', 'Corgi', 'competitive and cuddly', 8)
]

# Create your views here.
def home(request):
  return HttpResponse('<h1>Hi! Welcome to Dog Collector /ᐠ｡‸｡ᐟ\</h1>')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    return render(request, 'dogs/index.html', {'dogs': dogs})
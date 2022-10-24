from django.shortcuts import render

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
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    return render(request, 'dogs/index.html', {'dogs': dogs})
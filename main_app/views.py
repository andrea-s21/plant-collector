from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Plant, Category
from .forms import WateringForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def plants_index(request):
    plants = Plant.objects.all()
    return render(request, 'plants/index.html', {'plants': plants})

def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    watering_form = WateringForm()
    return render(request, 'plants/detail.html', {
        'plant': plant, 'watering_form': watering_form})

class PlantCreate(CreateView):
    model = Plant
    fields = '__all__'
    success_url = '/plants/'

class PlantUpdate(UpdateView):
    model = Plant
    fields = ['care']

class PlantDelete(DeleteView):
    model = Plant 
    success_url = '/plants/'

def add_watering(request, plant_id):
    form = WateringForm(request.POST)
    if form.is_valid():
        new_watering = form.save(commit=False)
        new_watering.plant_id = plant_id
        new_watering.save()
    return redirect('detail', plant_id=plant_id)

class CategoryList(ListView):
  model = Category

class CategoryDetail(DetailView):
  model = Category

class CategoryCreate(CreateView):
  model = Category
  fields = '__all__'

class CategoryUpdate(UpdateView):
  model = Category
  fields = ['name']

class CategoryDelete(DeleteView):
  model = Category
  success_url = '/categories/'



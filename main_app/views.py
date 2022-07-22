from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch, Hat
from .forms import FeedingForm

# Add the following import
from django.http import HttpResponse


# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# Add new view
def finches_index(request):
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', { 'finches': finches })

def finch_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  # Get the toys the cat doesn't have...
  # First, create a list of the toy ids that the cat DOES have
  id_list = finch.hats.all().values_list('id')
  # Now we can query for toys whose ids are not in the list using exclude
  hats_finch_doesnt_have = Hat.objects.exclude(id__in=id_list)
  feeding_form = FeedingForm()
  return render(request, 'finches/detail.html', {
    'finch': finch, 'feeding_form': feeding_form,
    # Add the toys to be displayed
    'hats': hats_finch_doesnt_have
  })

def add_feeding(request, finch_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('detail', finch_id=finch_id)


class FinchCreate(CreateView):
  model = Finch
  fields = ['name','typeof', 'description', 'age']

class FinchUpdate(UpdateView):
  model = Finch
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['typeof', 'description', 'age']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches/'

def assoc_hat(request, finch_id, hat_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Finch.objects.get(id=finch_id).hats.add(hat_id)
  return redirect('detail', finch_id=finch_id)

class HatList(ListView):
  model = Hat

class HatDetail(DetailView):
  model = Hat

class HatCreate(CreateView):
  model = Hat
  fields = '__all__'
  success_url = "/hats/"

class HatUpdate(UpdateView):
  model = Hat
  fields = ['name', 'color']
  success_url = "/hats/"

class HatDelete(DeleteView):
  model = Hat
  success_url = '/hats/' 
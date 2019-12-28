from django.shortcuts import render
from db import models
from django.views.generic import DetailView
# Create your views here.

# class FilmDetailView(DetailView):
#     context_object_name = 'film_detail'
#     model = models.Film
#     template_name = 'film/film_detail.html'


def FilmDetailView(request,pk):
    model = models.Film.objects.get(id = pk)

    
    return render(request, 'film/film_detail.html', {'model':model})

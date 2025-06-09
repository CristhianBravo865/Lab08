from django.views.generic import ListView
from django.shortcuts import render
from .models import Framework, Character, Language, Movie

def index(request):
    return render(request, 'index.html')

class FrameworkListView(ListView):
    model = Framework
    template_name = 'framework_list.html'

class CharacterMoviesView(ListView):
    model = Character
    template_name = 'character_movies.html'

class LanguageListView(ListView):
    model = Language
    template_name = 'language_list.html'

class MovieListView(ListView):
    model = Movie
    template_name = 'movie_list.html'

class CharacterListView(ListView):
    model = Character
    template_name = 'character_list.html'

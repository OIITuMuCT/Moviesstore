from django.shortcuts import render
from .models import Movie

# Create your views here.
movies = [
    {
        'id': 2, 'name': 'Avatar', 'price': 13,
        'description': 'A journey to a distant world and the battle for resources'
    },
    {
        'id': 3, 'name': 'The Dark Knight', 'price': 14,
        'description': 'Gotham vigilante faces the Joker.'
    },
    {
        'id': 4, 'name': 'Titanic', 'price': 14,
        'description': 'A love story set against the backdrop of the sinking Titanic.'
    },
]

def index(request):
    template_data = {}
    template_data['title'] = 'Movies'
    template_data['movies'] = Movie.objects.all()
    return render(request, 'movies/index.html',
                {'template_data': template_data})


def show(request, id):
    movie = Movie.objects.get(id=id)

    template_data = {}
    template_data['title'] = movie.name
    template_data['movie'] = movie
    return render(request, 'movies/show.html',
                  {'template_data': template_data})
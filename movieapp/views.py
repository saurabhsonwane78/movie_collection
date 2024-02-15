from django.http import JsonResponse
from .movie_service import get_movies

def movie_list(request):
    page = request.GET.get('page', 1)
    movies_data = get_movies(page)
    movies = movies_data.get('results', [])
    return JsonResponse({'movies': movies})

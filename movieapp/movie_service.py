import requests

def get_movies(page=1):
    url = 'https://demo.credy.in/api/v1/maya/movies/'
    params = {'page': page}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

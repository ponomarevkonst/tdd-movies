import pytest
from movies.models import Movie


@pytest.mark.django_db
def test_movie_model():
    movie = Movie(title='Matrix', genre='action', year='1999')
    movie.save()
    assert movie.title == 'Matrix'
    assert movie.genre == 'action'
    assert movie.year == '1999'
    assert movie.created_date
    assert movie.updated_date
    assert str(movie) == movie.title


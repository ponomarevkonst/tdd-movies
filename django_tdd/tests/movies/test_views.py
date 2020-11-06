import json
import pytest
from rest_framework.test import APITestCase

from movies.models import Movie


class MyAPITestCase(APITestCase):
    def setUp(self) -> None:
        Movie(title="Godfather", year="1979", genre="drama").save()
        self.movies = Movie.objects.all()
        assert len(self.movies) == 1


@pytest.mark.django_db
class TestAddSingleMovie(MyAPITestCase):

    def tearDown(self) -> None:
        new_movies = Movie.objects.all()
        assert len(new_movies) - len(self.movies) == self.is_added

    def test_add_movie(self):
        resp = self.client.post(
            "/api/movies",
            json.dumps({
                "title": "Matrix",
                "genre": "action",
                "year": "1999"
            }),
            content_type="application/json"
        )
        assert resp.status_code == 201
        assert resp.data["title"] == "Matrix"
        self.is_added = True

    def test_add_movie_invalid_json(self):
        resp = self.client.post(
            "/api/movies",
            {},
            content_type="application/json"
        )
        assert resp.status_code == 400
        self.is_added = False

    def test_add_movie_invalid_json_keys(self):
        resp = self.client.post(
            "/api/movies",
            {
                "title": "Matrix",
                "genre": "action",
            },
            content_type="application/json"
        )
        assert resp.status_code == 400
        self.is_added = False


class TestGetSingleMovie(MyAPITestCase):
    def test_get_single_movie(self):
        resp = self.client.get("/api/movies/1")
        assert resp.status_code == 200
        assert resp.data["title"] == "Godfather"

    def test_get_single_movie_incorrect_id(self):
        resp = self.client.get("/api/movies/f123/")
        assert resp.status_code == 404


class TestGetAllMovies(MyAPITestCase):
    def test_get_all_movies(self):
        Movie(title="Tenet", genre="action", year="2020").save()
        Movie(title="Queen's Gambit", genre="series", year="2020").save()
        resp = self.client.get("/api/movies")
        assert resp.status_code == 200
        assert len(resp.data) == 3
from movies.serializers import MovieSerializer


def test_valid_movie_serializer():
    valid_serializer_data = {
        'title': 'Avatar',
        'genre': 'action',
        'year': "2009"
    }
    serializer = MovieSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}


def test_invalid_movie_serializer():
    invalid_serializer_data = {
        'title': 'No man land',
        'year': '1916'
    }
    serializer = MovieSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert 'genre' not in serializer.data

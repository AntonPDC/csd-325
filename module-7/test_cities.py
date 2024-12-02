from city_functions import city_country

def test_city_country():
    result = city_country('new york', 'usa')
    assert result == 'New York, Usa'

if __name__ == "__main__":
    test_city_country()
    print("Test passed!")

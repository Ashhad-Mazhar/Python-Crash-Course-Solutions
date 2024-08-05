from Exercise_11_2 import return_city_country

def test_city_country():
    output = return_city_country('santiago', 'chile')
    assert output == 'Santiago, Chile'

def test_city_country_population():
    output = return_city_country('santiago', 'chile', 5000000)
    assert output == 'Santiago, Chile - population 5000000'
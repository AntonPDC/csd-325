def city_country(city, country, language=None, population=None):
    if population and language:
        return f"{city.title()}, {country.title()} - population {population}, language {language}"
    elif population and not language:
        return f"{city.title()}, {country.title()} - population {population}"
    elif language and not population:
        return f"{city.title()}, {country.title()}, {language}"
    else:
        return f"{city.title()}, {country.title()}"
if __name__ == "__main__":
    print(city_country("santiago", "chile"))
    print(city_country("tokyo", "japan", population= 934890))
    print(city_country("paris", "france", population= 412142, language="French"))

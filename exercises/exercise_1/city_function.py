def get_formatted_city_country(city, country, population = ''):
    if population:
        formatted = f"{city.title()}, {country.title()} - population {population}"
    else:
        formatted = f"{city}, {country}"
    return  formatted
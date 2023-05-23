
def format_city_country(city, country, population=""):
    """Return a neatly formatted city and country name."""
    
    if population:
        city_info = f"{city.title()}, {country.title()} - population {population}"
    else:
        city_info = f"{city.title()}, {country.title()}"
    return city_info

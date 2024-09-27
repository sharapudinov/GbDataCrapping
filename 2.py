from requests import request
from PIL import Image


class GoogleMapsScraper:
    def __init__(self):
        self.base_url = "https://maps.googleapis.com/maps/api/"
        self.api_key = 'AIzaSyCbBb_sXMaIMHa_C7pfjRz7KJ_JFoRhk54'

    def streetview(self, lon: float, lat: float, width: int = 680, height: int = 480):
        return request(
            'get',
            self.base_url + f'streetview?location={lon},{lat}?&size={width}x{height}&key={self.api_key}'
        )


if __name__ == "__main__":
    scraper = GoogleMapsScraper()
    while True:
        try:
            lon = float(input("Широта:"))
            break
        except:
            continue
    while True:
        try:
            lat = float(input("Долгота:"))
            break
        except:
            continue

    response = scraper.streetview(lon, lat)
    with open(f'{lon}_{lat}.jpg', 'wb') as file:
        file.write(response.content)

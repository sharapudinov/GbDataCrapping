from requests import request
from PIL import Image


class GoogleMapsScraper:
    def __init__(self):
        self.base_url = "https://maps.googleapis.com/maps/api/"
        self.api_key = 'AIzaSyCbBb_sXMaIMHa_C7pfjRz7KJ_JFoRhk54'

    def stritview(self, lon: float, ltd: float, width: int = 680, height: int = 480):
        return request(
            'get',
            self.base_url + f'streetview?location={lon},{ltd}?&size={width}x{height}&key={self.api_key}'
        )


if __name__ == "__main__":
    scraper = GoogleMapsScraper()
    lon = 41.403609
    ltd = 2.174448
    response = scraper.stritview(lon, ltd)
    with open(f'{lon}_{ltd}.jpg', 'wb') as file:
        file.write(response.content)

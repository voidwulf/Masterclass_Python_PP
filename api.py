import requests #FYI: have import request in order to reqest to run in request.get()
class API:
    def extract (self):
        data = requests.get('https://www.7timer.info/bin/astro.php?lon=113.2&lat=23.1&ac=0&unit=metric&output=json&tzshift=0') #rquest data from API
        return data.text #return data in text forma

    def main(self):
        return print(self.extract()) # print extracted data


api = API()

api.main()
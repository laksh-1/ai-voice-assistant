import requests


class jokes():
    def getJoke(self):
        api_url = "https://v2.jokeapi.dev/joke/Any?format=txt&type=single"
        txt_return = requests.get(api_url).text
        return txt_return

import requests
from selenium import webdriver
from services import api


class news():
    def __init__(self):
        self.driver = webdriver.Chrome(
            executable_path='C:/Users/laksh/Downloads/chromedriver.exe')

    def getNews(self):
        api_url = "https://newsapi.org/v2/top-headlines?country=in&apiKey="+api.news_api
        txt_return = requests.get(api_url).json()
        self.driver.get(url=txt_return['articles'][0]['url'])
        newstxt = ""
        for i in range(0, 3):
            newstxt += txt_return['articles'][i]['title']
            newstxt += "\n"
        return newstxt

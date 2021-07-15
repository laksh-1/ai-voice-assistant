from selenium import webdriver


class infoWiki():
    def __init__(self):
        self.driver = webdriver.Chrome(
            executable_path='C:/Users/laksh/Downloads/chromedriver.exe')

    def getInfo(self, query):
        self.query = query
        self.driver.get(url='https://www.wikipedia.org')
        searchQuery = self.driver.find_element_by_xpath(
            '//*[@id="searchInput"]')
        searchQuery.click()
        searchQuery.send_keys(query)
        searchBtn = self.driver.find_element_by_xpath(
            '//*[@id="search-form"]/fieldset/button')
        searchBtn.click()

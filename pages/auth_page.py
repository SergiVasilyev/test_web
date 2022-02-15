from base_method.base import WebPage
from base_method.elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):

        url = 'https://www.linkedin.com/login'
        super().__init__(web_driver, url)

    email = WebElement(xpath='//*[@id="username"]')

    password = WebElement(xpath='//*[@id="password"]')

    sing_in = WebElement(xpath='//*[@id="organic-div"]/form/div[3]/button')

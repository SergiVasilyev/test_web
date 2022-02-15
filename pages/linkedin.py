
import os

from base_method.base import WebPage
from base_method.elements import WebElement


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):

        url = 'https://www.linkedin.com/'
        super().__init__(web_driver, url)

    # Sing up button
    sing_up = WebElement(xpath='/html/body/nav/div/a[1]')

    # Sing in button
    sing_in = WebElement(xpath='/html/body/nav/div/a[2]')

    # Join now button
    join_now = WebElement(xpath='/html/body/nav/div/a[1]')

    # Discover button
    discover = WebElement(xpath='/html/body/nav/ul/li[1]/a')

    # People button
    people = WebElement(xpath='/html/body/nav/ul/li[2]/a')

    # Learning button
    learning = WebElement(xpath='/html/body/nav/ul/li[3]/a')

    # Jobs button
    jobs = WebElement(xpath='/html/body/nav/ul/li[4]/a')

    # General information
    general = WebElement(xpath='//*[@id="main-content"]/section[8]/div/div/div[1]/h3')


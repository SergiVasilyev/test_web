from pages.auth_page import AuthPage

def test_authorisation(web_driver):

    page = AuthPage(web_driver)
    page.wait_page_loaded()

    page.email.send_keys('SeregaKM05@gmail.com')

    page.password.send_keys('g1h2j3o4f5q6')

    page.sing_in.click()
    page.wait_page_loaded()

    assert page.get_current_url() == 'https://www.linkedin.com/feed/'

    web_driver.quit()
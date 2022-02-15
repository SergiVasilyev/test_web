from pages.linkedin import MainPage


def test_main_page(web_driver):
    """ Make sure main search works fine. """

    page = MainPage(web_driver)

    page.scroll_down()
  #  assert page.general.is_visible()
    page.scroll_up()

    page.sing_in.click()
    page.wait_page_loaded()
    assert page.get_current_url() == 'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'
    page.go_back()

    page.sing_up.click()
    page.wait_page_loaded()
    assert  page.get_current_url() == 'https://www.linkedin.com/signup/cold-join?trk=guest_homepage-basic_nav-header-join'
    page.go_back()

    page.wait_page_loaded()

    # Verify that user can see the list of products:
    assert page.sing_in.is_visible(), 'Sorry page not found'

    web_driver.quit()
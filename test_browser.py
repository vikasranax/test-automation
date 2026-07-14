from playwright.sync_api import Page


def test_saucedemo_title_is_visible(page: Page):
    page.goto("https://www.saucedemo.com")
    assert page.is_visible("#login-button")


def test_successful_login(page: Page):
    page.goto("https://www.saucedemo.com")

    # Fill loginform
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    # check invent. page
    assert page.is_visible(".inventory_list")

def test_login_with_wrong_password(page: Page):
    page.goto("https://www.saucedemo.com")

    page.fill("#user-name", "standard_user")
    page.fill("#password", "wrong_password")
    page.click("#login-button")

    # Login should fail, so an error message should appear
    error_message = page.text_content("[data-test='error']")
    assert "do not match" in error_message.lower()    
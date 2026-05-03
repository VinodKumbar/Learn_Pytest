import time

from playwright.sync_api import Page, expect
from test_playwrightBasics import test_loginPage

def test_addToCart(page:Page):
    test_loginPage(page)
    # test scenario :
    # Select 2 Products
    # MacBook Pro M3 and Acer Predator
    # Proceed to checkout

    # filter() - Filter method is used to narrow down the selection of elements based on specific criteria.
    # has_text - is a selector engine that allows you to find elements based on their text  content.
    # It is often used in combination with other selectors to locate elements that contain specific text.
    # div => tagName
    # .card => className

    macProduct = page.locator(".card").filter(has_text="MacBook Pro M3")
    macProduct.get_by_role("button", name="Add").click()

    acerProduct = page.locator(".card").filter(has_text="Acer Predator")
    acerProduct.get_by_role("button", name="Add").click()

    time.sleep(2)

    page.get_by_text("View Cart").scroll_into_view_if_needed()
    page.get_by_text("View Cart").click()

    time.sleep(2)

    expect(page.locator("#cartTable")).to_contain_text("MacBook Pro M3")
    expect(page.locator("#cartTable")).to_contain_text("Acer Predator")

    page.get_by_role("button", name="Proceed to Checkout").is_enabled()

    page.get_by_text("Proceed to Checkout").click()

    time.sleep(5)


# Assignment -> Select Furniture from Drop-down
# Select 2 Furniture Products
# Increase the Product count
# Proceed to Checkout






from test_addTOCart_flow import test_addToCart
from playwright.sync_api import Page, expect

def test_orderHistory(page:Page):

    test_addToCart(page)
    page.wait_for_timeout(2000)

    page.get_by_placeholder("Full Name").fill("John Wick")
    page.locator("#address").fill("123 Main Street, Anytown, USA")
    page.locator("#country").select_option("USA")
    page.locator("#state").select_option("California")

    page.get_by_text("UPI").click()

    page.locator("#agreePolicy").click()

    page.get_by_role("button", name="Place Order").click()

    page.wait_for_timeout(2000)

    order_ID = page.locator("#orderId").inner_text()
    assert order_ID != " " ,  "Order ID is not empty"
    print("Order ID:", order_ID)

    page.get_by_role("button", name="Continue Shopping").click()
    page.wait_for_timeout(2000)

    page.get_by_role("button", name="Order History").click()

    expect(page.locator("#orderTable")).to_contain_text(order_ID)
    print("Order ID is present in Order History:", order_ID)

    page.get_by_role("button", name="Logout").click()
    expect(page.locator("text=Welcome to Ohreems Automation Shop")).to_be_visible()

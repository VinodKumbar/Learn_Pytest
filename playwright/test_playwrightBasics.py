import time

from playwright.sync_api import Page, expect, Playwright


# in one browser we can have multiple contexts
# in one context we can have multiple pages
def test_playwrightBasics(playwright):
       browser = playwright.chromium.launch(headless=False)
       context = browser.new_context()
       page = context.new_page()
       page.goto("https://ohreems-automation-shop.netlify.app/")
       time.sleep(5)

# Chromium engine, headless mode and 1 single text
def test_playwrightShortcut(page:Page):
       page.goto("https://ohreems-automation-shop.netlify.app/")
       time.sleep(5)

def test_loginPage(page:Page):
        page.goto("https://ohreems-automation-shop.netlify.app/")
        time.sleep(2)
        page.get_by_label("Username").fill("john")
        page.get_by_placeholder("Password").fill("wick123")
        page.get_by_role("button", name = "Login").click()
        time.sleep(2)

def test_childWindowHandle(page: Page):
    page.goto("https://ohreems-automation-shop.netlify.app/")

    # click "Forgot Password?" and wait for new page to open
    #Listens for a new page opening
    #build a closure
    # A closure is a function that remembers variables from its outer scope,
    # even after the outer function has finished executing.

    with page.context.expect_page() as newPage_info:
        page.get_by_role("link", name="Forgot Password?").click()

    #capture new page
    childpage = newPage_info.value

    # Wait for new child page to load
    childpage.wait_for_load_state()

    time.sleep(3)

    # Validate new page opened (optional)
  #  childPageURL = childpage.url
    expect(childpage.url).to_have_url("https://ohreems-automation-shop.netlify.app/forgetpasswordlink")

    print("Child page URL:", childpage.url)

    expect(childpage.locator("text=Send Reset Link")).to_be_visible()

    # Switch back to original login page
    page.bring_to_front()

    # Validate we are back on login page
    expect(page.locator("text=Welcome to Ohreems Automation Shop")).to_be_visible()

    page.get_by_label("Username").fill("john")
    page.get_by_label("Password").fill("wick123")
    page.get_by_role("button", name="Login").click()
    time.sleep(5)
    page.get_by_role("link", name="Logout").click()
    expect(page.locator("text=Welcome to Ohreems Automation Shop")).to_be_visible()

def test_firefoxBrowser(playwright : Playwright):
        firefoxBrowser =  playwright.firefox
        browser = firefoxBrowser.launch(headless=False)
        page = browser.new_page()
        page.goto("https://ohreems-automation-shop.netlify.app/")
        page.locator("#username").fill("john")
        page.locator("#password").fill("wick123")
        page.get_by_role("button", name="Login").click()
        time.sleep(5)



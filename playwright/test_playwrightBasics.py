import time

from playwright.sync_api import Page, expect


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

def test_corePlaywrightLocators(page:Page):
        page.goto("https://ohreems-automation-shop.netlify.app/")
        time.sleep(5)
        page.get_by_label("Username").fill("john")
        page.get_by_placeholder("Password").fill("wick123")
        page.get_by_role("button", name = "Login").click()
        time.sleep(5)

def test_switchTabs(page:Page):
       page.goto("https://ohreems-automation-shop.netlify.app/")

       # click on the link which opens in new tab i.e Forgot password ?
       # listen for a new tab opening
       with page.context.expect_page() as new_page_info:
           page.get_by_role("link", name = "Forgot Password?").click()

            #capture new page information
           new_page = new_page_info.value

           #wait for new tab to Load
           new_page.wait_for_load_state()
           time.sleep(5)

           #validate new page got open or not ?
           print("New Tab URL: ", new_page.url)

           # writing assert function from Playwright
           expect(page.locator("text=Forgot Password")).to_be_visible()

            # Switch  back to Original Login Page
           page.bring_to_front()

           #Validate we are back on the Login Page
           expect(page.locator("text=Welcome to Ohreems Automation Shop")).to_be_visible()

           page.get_by_label("Username").fill("john")
           page.get_by_placeholder("Password").fill("wick123")
           page.get_by_role("button", name="Login").click()
           time.sleep(5)

           page.get_by_role("link", name= "Logout").click()
           expect(page.locator("text=Welcome to Ohreems Automation Shop")).to_be_visible()






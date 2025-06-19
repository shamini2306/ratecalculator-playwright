import pytest
from playwright.sync_api import Browser, BrowserContext, Page

#@pytest.fixture(scope="session")
#def browser_type_launch_args(browser_type_launch_args):
#    return {
#        **browser_type_launch_args,
#        "slow_mo": 1000,  # 1 second delay between actions
#    }

#@pytest.fixture(scope="function")
#def context(browser: Browser):
#    context = browser.new_context()
#    yield context
#    context.close()

#@pytest.fixture(scope="function")
#def page(context: BrowserContext):
#    page = context.new_page()
#    yield page
#    page.close()

@pytest.fixture(scope="function")
def context(browser: Browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context: BrowserContext):
    page = context.new_page()
    # Store the calculator in the context
    context.calculator = None
    yield page
    page.close()

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": False,
        "slow_mo": 1000
    }
from behave import fixture, use_fixture
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.chrome import ChromeDriverManager

@fixture
def selenium_browser_firefox(context):
    # context.browser = webdriver.Chrome(ChromeDriverManager().install())
    context.browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    yield context.browser
    context.browser.quit()

def before_all(context):
    use_fixture(selenium_browser_firefox, context)


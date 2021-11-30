from behave import given, when, then

@given('I open Herokuapp website')
def open_app(context):
    context.browser.get("http://the-internet.herokuapp.com")

@given('I navigate to the "{section}" section')
def navigate_to_section(context, section):
    selector = f'//*[@id="content"]//ul/li/a[@href = "{section}"]'
    context.browser.find_element_by_xpath(selector).click()

@when('I click on the Add button')
def click_add(context):
    # TODO
    assert True is True

@then('I see Delete button is visible')
def check_delete(context):
    # TODO
    assert True is True

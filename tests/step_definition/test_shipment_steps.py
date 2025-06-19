from pytest_bdd import given, when, then, parsers, scenario
from playwright.sync_api import expect
from tests.pages.shipment_calculator_page import ShipmentCalculatorPage

@scenario("../features/shipment_calculator.feature", "Calculate valid shipment quote")
def test_valid_shipment_quote():
    print("Test completed successfully")

@given("I am on the rate calculator page")
def navigate_to_calculator(page, context):
    calculator = ShipmentCalculatorPage(page)
    calculator.navigate()
    context.calculator = calculator 
    print("Rate Calculator Page loaded successfully")

@when(parsers.parse('I enter shipment details "{postcode}" "{country}" "{weight}"'))
def fill_shipment_details(context, postcode, country, weight):
    print(f"Filling details - Postcode: {postcode}, Country: {country}, Weight: {weight}")
    calculator = context.calculator
    calculator.fill_shipment_details(
        from_postcode=postcode,
        to_country=country,
        weight=weight
    )
    print("Shipment details filled")

@when("I click Calculate")
def click_calculate(context):
    context.calculator.calculate()
    print("Calculate button clicked")

@then("I should see available shipping quotes")
def verify_quotes_displayed(context):
    context.calculator.verify_quotes()
    print("Quotes verified")
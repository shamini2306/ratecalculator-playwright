from playwright.sync_api import Page, expect
import time

class ShipmentCalculatorPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://pos.com.my/send/ratecalculator"
        
    def _wait(self, seconds=1):
        """Helper method to add delay between actions"""
        time.sleep(seconds)

    def navigate(self):
        self.page.goto(self.url, wait_until="networkidle")

    def fill_shipment_details(self, from_postcode: str, to_country: str, weight: str):
        # Fill postcode
        postcode = self.page.get_by_placeholder("Postcode").first
        postcode.click()
      
        for char in from_postcode:
            postcode.press(char)    
        # Keep focus on postcode and wait for state to update
        postcode.focus()

        # Select destination country
        country = self.page.get_by_placeholder("Select country")
        country.click()
        country.fill(to_country)
        self._wait(2)  # Extra delay for dropdown to appear
        try:
            self.page.get_by_role("option", name=f"{to_country} - ").first.click()
            print(f"Selected country: {to_country}")
        except Exception as e:
            print(f"Could not select country: {str(e)}")
        self._wait(1)
        
        # Fill weight
        weight_field = self.page.get_by_placeholder("eg. 0.1kg")
        weight_field.click()
        weight_field.fill(weight)
        print(f"Filled weight: {weight}kg")

    def calculate(self):
        try:
            self.page.get_by_text("Calculate").click()
            self._wait(3)  # Wait for calculation
        except Exception as e:
            print(f"Error during calculation: {str(e)}")
            raise

    def verify_quotes(self):
        try:
            # Scroll down to see the results
            self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            self._wait(2)
            
            # Take screenshot of results
            self.page.screenshot(path="quote_results.png")
            
            # Verify quotes are displayed
            self.page.get_by_role("heading", name="Your Quote").is_visible()
            self.page.get_by_text("Express Mail Service (EMS)").is_visible()
            self.page.get_by_text("International Air Parcel").is_visible()
            self.page.get_by_text("International Surface Parcel").is_visible()
            
            print("All expected quotes are displayed")
            return True
            
        except Exception as e:
            print(f"Error verifying quotes: {str(e)}")
            self.page.screenshot(path="verification_error.png")
            raise
    
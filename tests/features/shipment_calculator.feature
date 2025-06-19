# features/shipment_calculator.feature

Feature: Shipment Quote Calculation
  As a user
  I want to calculate shipment quotes
  So that I can see available shipping options

@test
Scenario: Calculate valid shipment quote
    Given I am on the rate calculator page
    When I enter shipment details "35600" "India" "1"
    And I click Calculate
    Then I should see available shipping quotes
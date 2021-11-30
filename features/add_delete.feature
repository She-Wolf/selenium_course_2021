Feature: Herokuapp - Add/Delete element

Scenario: Add element
    Given I open Herokuapp website
    And I navigate to the "/add_remove_elements/" section
    When I click on the Add button
    Then I see Delete button is visible

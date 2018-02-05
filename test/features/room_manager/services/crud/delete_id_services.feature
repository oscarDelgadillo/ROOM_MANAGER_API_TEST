@crud
Feature: Delete services using service ID

  Scenario: This scenario verify Delete by ID
    Given Given I have a Service Created with this data:
      | hostname                 | username | password    | type           |
      | maaaaaarcoooo@at05.local | marco    | Password123 | ExchangeServer |
    When I set DELETE to /services
      And I send the request
    Then I should get a response with status code 200
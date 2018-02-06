@crud
Feature: Delete services using service ID

  Scenario: This scenario verify Delete by ID
    Given Given I have a Service Created with this data:
      | hostname                 | username | password    | type           |
      | maaaaaarcoooo@at05.local | marco    | Password123 | ExchangeServer |
      And I keep service_id as __ServId
    When I set DELETE to /services/__ServId
      And I send the request
    Then I should get a response with status code 200
       And The response should equals that Get method
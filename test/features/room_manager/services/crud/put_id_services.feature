@crud
Feature: Put services using service ID
  @putIdServices
  Scenario: This scenario verify put service by ID
    Given Given I have a Service Created with this data:
      | hostname                 | username | password    | type           |
      | maaaaaarcoooo@at05.local | marco    | Password123 | ExchangeServer |
    When I set PUT to /services
    And I set this change :
      | username | password    |
      | oscar    | Password123 |
    And I send the request
    Then I should get a response with status code 200
    When I set DELETE to /services
      And I send the request
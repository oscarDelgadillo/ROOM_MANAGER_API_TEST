@crud
Feature: Delete services using service ID

  Scenario:
    Given I have a Service Created with this data:
      | hostname        | username | password    | type           |
      | marc@at05.local | marco    | Password123 | ExchangeServer |



#  Scenario Outline: This scenario verify Delete ID
#    Given I go to Room Manager services "/services"
#    When I do "DELETE" to services with service ID : serviceID <service_ID>
#    Then It should return status code "200"
#    Examples:
#      | service_ID               |
#      | 5a7247619390bb1630a9be19 |
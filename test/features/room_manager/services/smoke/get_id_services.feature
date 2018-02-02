Feature: smoke get service id

  Scenario Outline: This scenario verifies the service status code with service Id
    Given I go to Room Manager services "/services"
    When I do "GET" to services with service ID : serviceID <service_ID>
    Then It should return status code "200"
    Examples:
      | service_ID               |
      | 5a74b2679390bb1630a9be2d |
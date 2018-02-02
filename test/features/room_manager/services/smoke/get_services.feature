Feature: Services smoke test

  Scenario Outline: Get Room Manager Services
    Given I have room manager server up
    When I GET to /services
    And I put these data : hostname <Hostname> , name <Name>, type server <Type> and version <version>
    Then I should get a response with status code 200
    Examples:
      | Hostname   | Name                 | Type           | version               |
      | at05.local | Exchange Server 2013 | ExchangeServer | 15.0 (Build 30516.32) |


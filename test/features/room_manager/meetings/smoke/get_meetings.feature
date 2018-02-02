# Author: Abner Mamani
@smoke
Feature: Meetings smoke test
  Validate service retrieve Meetings

  @meetings
  Scenario: Get Meetings from Room Manager

    Given I make a 'GET' request to '/meetings'
    When I execute the request with the following infor
      | owner                    | start                    | credentials                              |
      | administrator@at05.local | 2017-04-21T20:00:00.000Z | YXQwNVxhZG1pbmlzdHJhdG9yOlBhc3N3b3JkMTIz |
    Then I expect a response status code '200'

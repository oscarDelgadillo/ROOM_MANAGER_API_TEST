@smoke
Feature: Meetings functional test
  Validate service retrieve Meetings

  @meetings
  Scenario Outline: Get Meetings functional

    Given I GET to /meetings
    When I set the following parameters for a meeting with

      | owner    | start    | end    | credentials    |
      | <owner_> | <start_> | <end_> | <credentials_> |
    And I send the request
    Then I should get a response with status code 200
    Examples:
      | owner_               | start_                   | end_                     | credentials_ |
      |                      | 2017-04-21T20:00:00.000Z |                          |              |
      |                      | 2017-04-21T20:00:00.000Z | 2017-04-21T21:00:00.000Z |              |
      | __USER_ADMINISTRATOR | 2017-04-21T20:00:00.000Z | 2017-04-21T21:00:00.000Z |              |


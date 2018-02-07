# Author: Abner Mamani
@smoke
Feature: Meetings smoke test
  Validate service retrieve Meetings

  @meetings
  Scenario: Get Meetings from Room Manager

    Given I GET to /meetings
    When I set the following parameters for a meeting
        | owner                | start                    | credentials                 |
        | __USER_ADMINISTRATOR | 2017-04-21T20:00:00.000Z | __CREDENTIALS_ADMINISTRATOR |
      And I send the request
    Then I should get a response with status code 200

  @after_delete_item
  Scenario: Get Meetings by Id from Room Manager

    Given I POST to /meetings
      And I set the following body
         """
            {
               "organizer": "__USER_ADMINISTRATOR",
               "subject": "Scrum Test Meetings ABNER",
               "body": "Test meeting",
               "start": "2017-04-21T20:00:00.000Z",
               "end": "2018-05-02T20:09:17.121Z",
               "rooms": [
                 "__USER_ROOM"
               ],
               "attendees": [],
               "optionalAttendees": []
            }
          """
       And I send '__CREDENTIALS_ADMINISTRATOR' as credentials
       And I send the request
       And I keep the "id" as "$id_meeting" from the previous step
    When I GET to /meetings
      And I set the following parameters for a meeting
        | owner                | start                    | credentials                 |
        | __USER_ADMINISTRATOR | 2017-04-21T20:00:00.000Z | __CREDENTIALS_ADMINISTRATOR |
      And I send the request
    Then I should get a response with status code 200

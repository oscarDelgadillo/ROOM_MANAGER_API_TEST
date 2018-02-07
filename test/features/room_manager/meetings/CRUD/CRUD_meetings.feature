@CRUD @meetings
Feature: POST /meetings CRUD

  @post @after_delete_item
  Scenario: Create a meeting with room organizer and Administrator credentials

    Given I POST to /meetings
    When I set the following body
        """
          {
            "organizer": "__USER_ROOM",
            "subject": "Subject Test Room 777 ",
            "body": "Body Test",
            "start": "2019-03-01T20:00:00.000Z",
            "end": "2019-03-01T20:30:00.000Z",
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
    Then I should get a response with status code 200
      And I validate the schema of the request
#      And I validate the response contains the body json sent


  @post @after_delete_item
  Scenario: Create a meeting with USER organizer and USER credentials

    Given I POST to /meetings
    When I set the following body
        """
          {
            "organizer": "__USER_COMMON",
            "subject": "Subject Test Room 777 ",
            "body": "Body Test",
            "start": "2019-03-01T20:00:00.000Z",
            "end": "2019-03-01T20:30:00.000Z",
            "rooms": [
              "__USER_ROOM"
            ],
            "attendees": [],
            "optionalAttendees": []
          }
        """
      And I send '__CREDENTIALS_COMMON' as credentials
      And I send the request
      And I keep the "id" as "$id_meeting" from the previous step
    Then I should get a response with status code 200
      And I validate the schema of the request
#      And I validate the response contains the body json sent






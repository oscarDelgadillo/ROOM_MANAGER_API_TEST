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
      And I should get a response with status code 200
      And I keep the "id" as "$id_meeting" from the previous step
    Then I should get a response with status code 200
      And I validate the schema of the request
      And I validate the response contains the body json sent


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
      And I validate the response contains the body json sent



  @post @after_delete_item
  Scenario: Get a Meetings by Id given I create a meeting and obtain that Id

    Given I POST to /meetings
      And I set the following body
        """
          {
            "organizer": "__USER_COMMON",
            "subject": "Get all Meetings given I create a meeting from Room Manager",
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
      And I keep the "body" respons as "$body_respons"
    When I GET to /meetings
      And I set the following parameters for a meeting
        | owner         | start                    | credentials          |
        | __USER_COMMON | 2019-03-01T20:00:00.000Z | __CREDENTIALS_COMMON |
      And I send the request
    Then I should get a response with status code 200
      And I validate the schema of the request
      And I validate the GET response  compare with POST response



    @post @after_delete_item
  Scenario: Get all Meetings given I create a meeting from Room Manager

    Given I POST to /meetings
      And I set the following body
        """
          {
            "organizer": "__USER_COMMON",
            "owner": "__USER_COMMON",
            "subject": "Samuelito",
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
      And I keep the "body" respons as "$body_respons"
    When I GET to /meetings
      And I set the following parameters for a meetings
        | owner         | start                    | end                      | credentials          |
        | __USER_COMMON | 2019-03-01T20:00:00.000Z | 2019-03-01T20:30:00.000Z | __CREDENTIALS_COMMON |
      And I send the request
    Then I should get a response with status code 200
      And I validate the schemas of the request
      And I validate the GET response contains the POST response





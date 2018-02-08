@meetings @CRUD @delete
Feature: DELETE /meetings/{meetingId}

  Background: Create a meeting
     Given I POST to /meetings
      And I set the following body
         """
            {
               "organizer": "__USER_ADMINISTRATOR",
               "subject": "Scrum Test Meetings Admin",
               "body": "Test meeting",
               "start": "2017-04-21T20:00:00.000Z",
               "end": "2018-05-02T20:09:17.000Z",
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

  Scenario: Delete an existing meeting

    When I DELETE to /meetings
      And I send the request delete
      And I construct a expected response
    Then I should get a response with status code 200
      And the built expected response should be equal to the obtained response

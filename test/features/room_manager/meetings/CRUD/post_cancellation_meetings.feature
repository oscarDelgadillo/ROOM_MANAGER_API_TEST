@meetings @crud @post
Feature: POST /meetings/{meetingId}/cancellation

  Background: Create a meeting
     Given I POST to /meetings
      And I set the following body
           """
              {
                 "organizer": "__USER_ADMINISTRATOR",
                 "subject": "Scrum Test Meetings Admin",
                 "body": "Test meeting",
                 "start": "2018-04-21T20:00:00.000Z",
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


  Scenario: Cancelling an existing meeting
    When I make POST request to /meetings/$id_meeting/cancellation
      And I send '__CREDENTIALS_ADMINISTRATOR' as credentials
      And I send the request update
      And I construct a expected response
    Then I should get a response with status code 200 extra
      And the built expected response should be equal to the obtained response


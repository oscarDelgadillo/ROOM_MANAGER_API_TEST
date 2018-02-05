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



  @meetings @afeter_delete_meeting
  Scenario: Get Meetings by Id from Room Manager

    Given I make a 'GET' request to '/meetings' by Id
      And I made a 'POST' request to '/meetings'
      And I have meeting whit credentiales 'YXQwNVxhZG1pbmlzdHJhdG9yOlBhc3N3b3JkMTIz' and the body is
	 """
		{
	 	   "organizer": "administrator@at05.local",
	  	   "subject": "Scrum Test Meetings",
	  	   "body": "Test meeting",
		   "start": "2017-04-21T20:00:00.000Z",
		   "end": "2018-05-02T20:09:17.121Z",
		   "rooms": [
		     "room01@at05.local"
  		   ],
		   "attendees": [],
		   "optionalAttendees": []
		}
	  """
    	 And I keep the "id" as "$id_meeting" from the previous step
	When I execute the request with "$id_meeting" and the following info
    	 | owner                    | start                    | credentials                              |
         | administrator@at05.local | 2017-04-21T20:00:00.000Z | YXQwNVxhZG1pbmlzdHJhdG9yOlBhc3N3b3JkMTIz |
	Then I expect a response status code '200'

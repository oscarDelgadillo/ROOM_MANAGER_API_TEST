@CRUD
Feature: Retrieve Rooms
  Test successfully retrieving of Room(s)

  Background:
    Given I set ZnJhbmNvOlBhc3N3b3JkMTIz as credentials
    And I set POST to /meetings
    And I set the following meeting info
      | organizer         | subject                            | body | start                    | end                      | rooms             | attendees         | optionalAttendees |
      | franco@at05.local | Create meeting to Test room status | Test | 2018-02-09T15:00:00.000Z | 2018-02-09T16:00:00.000Z | room01@at05.local | franco@at05.local | marco@at05.local  |
    And I send the request

  Scenario: Verify that is possible to retrieve free rooms
    When I set GET to /rooms
    And I set the following params
      | from                     | to                       | status |
      | 2018-02-09T15:00:00.000Z | 2018-02-09T16:00:00.000Z | free   |
    And I send the request
    Then I should get a response with status code 200
    And I should get an empty Json response
#    And I should get a Json response with the following info
#      | name   | displayName | email             | code | capacity | service                  | roomStatus | equipment | location |
#      | Room01 | Room01      | room01@at05.local |      | 0        | 5a720749d54ad40d1882f3e5 | busy       | []        |          |
#    And I should get a Json response with the following schema
#      | type  | uuid   | name   | displayName | email  | code   | capacity | roomStatus | equipment | location |
#      | array | string | string | string      | string | string | number   | string     | array     | string   |

#  Scenario: Verify that is possible to retrieve busy rooms
#    When I set GET to /rooms
#    And I set the following params
#      | from                     | to                       | status |
#      | 2018-02-09T15:00:00.000Z | 2018-02-09T16:00:00.000Z | busy   |
#    And I send the request
#    Then I should get a response with status code 200
#    And I should get a Json response with the following info
#      | name   | displayName | email             | code | capacity | service                  | roomStatus | equipment | location |
#      | Room01 | Room01      | room01@at05.local |      | 0        | 5a720749d54ad40d1882f3e5 | busy       | []        |          |
#    And I should get a Json response with the following schema
#      | type  | uuid   | name   | displayName | email  | code   | capacity | roomStatus | equipment | location |
#      | array | string | string | string      | string | string | number   | string     | array     | string   |

#  Scenario: Verify that is possible to retrieve room by Id
#    When I set GET to /rooms
#    And I set the room Id
#    And I send the request
#    Then I should get a response with status code 200
#    And I should get a Json response with the following info
#      | name   | displayName | email             | code | capacity | service                  | roomStatus | equipment | location |
#      | Room01 | Room01      | room01@at05.local |      | 0        | 5a720749d54ad40d1882f3e5 | busy       | []        |          |
#    And I should get a Json response with the following schema
#      | type  | uuid   | name   | displayName | email  | code   | capacity | roomStatus | equipment | location |
#      | array | string | string | string      | string | string | number   | string     | array     | string   |
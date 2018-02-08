@functional
Feature: Retrieve Rooms with query
  Test successfully retrieving of Room(s) with query

  Scenario Outline: Verify that is possible to retrieve free rooms with query
    When I GET to /rooms
      And I set the following params
      | from                     | to                       | status |
      | 2018-02-09T15:00:00.000Z | 2018-02-09T16:00:00.000Z | free   |
      And I set the following query
      | _id        | uuid         | name         | displayName         | email         | code         | capacity         | service         | roomStatus         | equipment         | location         |
      | <id_value> | <uuid_value> | <name_value> | <displayName_value> | <email_value> | <code_value> | <capacity_value> | <service_value> | <roomStatus_value> | <equipment_value> | <location_value> |
      And I send the request
    Then I should get a response with status code 200
      And I should get a response containing the params requested

    Examples:
      | id_value | uuid_value | name_value | displayName_value | email_value | code_value | capacity_value | service_value | roomStatus_value | equipment_value | location_value |
      | _id      |            |            |                   |             |            |                |               |                  |                 |                |
      | _id      | uuid       |            |                   |             |            |                |               |                  |                 |                |
      | _id      | uuid       | name       |                   |             |            |                |               |                  |                 |                |
      | _id      | uuid       | name       | displayName       |             |            |                |               |                  |                 |                |
      | _id      | uuid       | name       | displayName       | email       |            |                |               |                  |                 |                |
      | _id      | uuid       | name       | displayName       | email       | code       |                |               |                  |                 |                |
      | _id      | uuid       | name       | displayName       | email       | code       | capacity       |               |                  |                 |                |
      | _id      | uuid       | name       | displayName       | email       | code       | capacity       | service       |                  |                 |                |
      | _id      | uuid       | name       | displayName       | email       | code       | capacity       | service       | roomStatus       |                 |                |
      | _id      | uuid       | name       | displayName       | email       | code       | capacity       | service       | roomStatus       | equipment       |                |
      | _id      | uuid       | name       | displayName       | email       | code       | capacity       | service       | roomStatus       | equipment       | location       |
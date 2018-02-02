@smoke @rooms
Feature: Smoke - Get a specific room

  Scenario: Get a specific room, obtaining the "roomsId" of the database
    Given I have rooms created
      And I have obtained roomsId of the database
    When I GET to /rooms/roomsId
    Then I should get a response with status code 200

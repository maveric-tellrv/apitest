Feature: Test API Response
  In order to increase the ninja survival rate,
  As a ninja commander
  I want my ninjas to decide whether to take on an
  opponent based on their skill levels

  Scenario: Check Api status code 200 with mandatory parameters
    Given The Url for the API 
     When I check response for the valid endpoint function TIME_SERIES_WEEKLY_ADJUSTED and Valid APIKeys
     Then response should be 200 

  Scenario: Check Api status code with missing mandatory parameters
    Given The Url for the API
     When I check response for the valid endpoint TIME_SERIES_WEEKLY_ADJUSTED and valid APIKEYS
     Then response should be 200


  Scenario: Check Api status code with invalid mandatory parameters
    Given The Url for the API
     When I check response for the invalid endpoint function  TIME_SERIES_WEEKLY_ADJUSTED and valid APIKEYS
     Then response should be 200

  Scenario: Check Api status code with mandatory parameters and Invalid APIKEYS
    Given The Url for the API
     When I check response for the valid endpoint TIME_SERIES_WEEKLY_ADJUSTED and Invalid APIKEYS
     Then response should be 200

  

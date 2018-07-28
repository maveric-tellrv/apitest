Feature: Test API Response for www.alphavantage.co

  @rest_client
  Scenario: Check Api status code 200 with mandatory parameters
    Given The Url for the API
    """
    200 implies that the response contains a payload that represents the status of the requested resource
    """
    When I check response for the endpoint function "TIME_SERIES_WEEKLY_ADJUSTED" and "MSFT" with "Valid" APIKeys
    Then response should be "200"
    And I match the response metadata keys "TIME_SERIES_WEEKLY_ADJUSTED"
    And response body should be valid and non empty
    And Test data validation should pass
    And Recent and oldest datapoints returns valid value
    And I validate the respose data keys for function "Meta Data"
    And I validate the respose data keys for function "Weekly Adjusted Time Series"  


  Scenario: Check Api status code 400 with mandatory parameters with invalid API KEYS
    Given The Url for the API
    """
    Expected status code is 400 due to invalid API keys
    """
    When I check response for the endpoint function "TIME_SERIES_WEEKLY_ADJUSTED" and "MSFT" with "InValid" APIKeys
    Then response should be "400"

  Scenario: Check Api status code 400 with missing mandatory parameters
    Given The Url for the API
    """
    Expected to go wrong while processing GET payload, the right status code is 400  
    """
    When I check response for the endpoint function "TIME_SERIES_WEEKLY_ADJUSTED" and " " with "InValid" APIKeys
    Then response should be "400"

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

  


  Scenario: Check response body is valid
    Given The Url for the API
    """
    This test test for valid non empty response body
    """
    When I check response for the endpoint function "TIME_SERIES_WEEKLY_ADJUSTED" and "MSFT" with "Valid" APIKeys
    Then response should be "200"
    And I match the response metadata keys "TIME_SERIES_WEEKLY_ADJUSTED"
    And response body should be valid and non empty

  
  Scenario: Validate response data with sample datapoints
    Given The Url for the API
    """
    This test validates the response metadata with sample valid datapoints
    """
    When I check response for the endpoint function "TIME_SERIES_WEEKLY_ADJUSTED" and "MSFT" with "Valid" APIKeys
    Then response should be "200"
    And Test data validation should pass


  Scenario: Validate the recent and the oldest datapoints values they sould not be none or empty
    Given The Url for the API
    """
    This test fails if the recent and oldest datapoints have  empty or blank values
    """
    When I check response for the endpoint function "TIME_SERIES_WEEKLY_ADJUSTED" and "MSFT" with "Valid" APIKeys
    Then response should be "200"
    And Recent and oldest datapoints returns valid value


   Scenario: Check the keys for response of Meta data field
    Given The Url for the API
    """
    Current Api return meta data as one response so this test validate  the keys in its response 
    """
    When I check response for the endpoint function "TIME_SERIES_WEEKLY_ADJUSTED" and "MSFT" with "Valid" APIKeys
    Then response should be "200"
    And Test data validation should pass
    And I validate the respose data keys for function "Meta Data"

  
   Scenario: Check the keys for response of Weekly Adjusted Time Series field
    Given The Url for the API
    """
    Current Api return Weekly Adjusted Time Series field as one response so this test validate  the keys in its response 
    """
    When I check response for the endpoint function "TIME_SERIES_WEEKLY_ADJUSTED" and "MSFT" with "Valid" APIKeys
    Then response should be "200"
    And Test data validation should pass
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

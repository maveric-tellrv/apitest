https://www.alphavantage.co/documentation/#time-series-data
API_key=13HOROS7Z6WRX1Q5




# Sample Test Run 


"""
rovyas@rovyas  ~/Documents/relayr/bddProject/features   master ●  behave apitest/test2.feature
Feature: Test API Response for www.alphavantage.co # apitest/test2.feature:1

  @rest_client
  Scenario: Check Api status code 200 with mandatory parameters                                                   # apitest/test2.feature:4
    Given The Url for the API                                                                                     # steps/rest_client.py:7 0.000s
      """
      200 implies that the response contains a payload that represents the status of the requested resource
      """
    When I check response for the endpoint function "TIME_SERIES_WEEKLY_ADJUSTED" and "MSFT" with "Valid" APIKeys # steps/rest_client.py:11 9.098s
    Then response should be "200"                                                                                 # steps/rest_client.py:31 0.000s
    And I match the response metadata keys "TIME_SERIES_WEEKLY_ADJUSTED"                                          # steps/rest_client.py:73 0.000s
    And response body should be valid and non empty                                                               # steps/rest_client.py:35 0.000s
    And Test data validation should pass                                                                          # steps/rest_client.py:174 0.000s
    And Recent and oldest datapoints returns valid value                                                          # steps/rest_client.py:123 0.033s
    And I validate the respose data keys for function "Meta Data"                                                 # steps/rest_client.py:87 0.000s
    And I validate the respose data keys for function "Weekly Adjusted Time Series"                               # steps/rest_client.py:87 0.000s

  Scenario: Check response body is valid                                                                          # apitest/test2.feature:21
    Given The Url for the API                                                                                     # steps/rest_client.py:7 0.000s
      """
      This test test for valid non empty response body
      """
    When I check response for the endpoint function "TIME_SERIES_WEEKLY_ADJUSTED" and "MSFT" with "Valid" APIKeys # steps/rest_client.py:11 3.735s
    Then response should be "200"                                                                                 # steps/rest_client.py:31 0.000s
    And I match the response metadata keys "TIME_SERIES_WEEKLY_ADJUSTED"                                          # steps/rest_client.py:73 0.000s
    And response body should be valid and non empty                                                               # steps/rest_client.py:35 0.000s

  Scenario: Validate response data with sample datapoints                                                         # apitest/test2.feature:32
    Given The Url for the API                                                                                     # steps/rest_client.py:7 0.000s
      """
      This test validates the response metadata with sample valid datapoints
      """
    When I check response for the endpoint function "TIME_SERIES_WEEKLY_ADJUSTED" and "MSFT" with "Valid" APIKeys # steps/rest_client.py:11 4.097s
    Then response should be "200"                                                                                 # steps/rest_client.py:31 0.000s
    And Test data validation should pass                                                                          # steps/rest_client.py:174 0.000s

  Scenario: Validate the recent and the oldest datapoints values they sould not be none or empty                  # apitest/test2.feature:42
    Given The Url for the API                                                                                     # steps/rest_client.py:7 0.000s
      """
      This test fails if the recent and oldest datapoints have  empty or blank values
      """
    When I check response for the endpoint function "TIME_SERIES_WEEKLY_ADJUSTED" and "MSFT" with "Valid" APIKeys # steps/rest_client.py:11 4.097s
    Then response should be "200"                                                                                 # steps/rest_client.py:31 0.000s
    And Recent and oldest datapoints returns valid value                                                          # steps/rest_client.py:123 0.033s

  Scenario: Check the keys for response of Meta data field                                                        # apitest/test2.feature:52
    Given The Url for the API                                                                                     # steps/rest_client.py:7 0.000s
      """
      Current Api return meta data as one response so this test validate  the keys in its response 
      """
    When I check response for the endpoint function "TIME_SERIES_WEEKLY_ADJUSTED" and "MSFT" with "Valid" APIKeys # steps/rest_client.py:11 3.458s
    Then response should be "200"                                                                                 # steps/rest_client.py:31 0.000s
    And Test data validation should pass                                                                          # steps/rest_client.py:174 0.000s
    And I validate the respose data keys for function "Meta Data"                                                 # steps/rest_client.py:87 0.000s

  Scenario: Check the keys for response of Weekly Adjusted Time Series field                                      # apitest/test2.feature:63
    Given The Url for the API                                                                                     # steps/rest_client.py:7 0.000s
      """
      Current Api return Weekly Adjusted Time Series field as one response so this test validate  the keys in its response 
      """
    When I check response for the endpoint function "TIME_SERIES_WEEKLY_ADJUSTED" and "MSFT" with "Valid" APIKeys # steps/rest_client.py:11 6.305s
    Then response should be "200"                                                                                 # steps/rest_client.py:31 0.000s
    And Test data validation should pass                                                                          # steps/rest_client.py:174 0.000s
    And I validate the respose data keys for function "Weekly Adjusted Time Series"                               # steps/rest_client.py:87 0.000s

  Scenario: Check Api status code 400 with mandatory parameters with invalid API KEYS                               # apitest/test2.feature:75
    Given The Url for the API                                                                                       # steps/rest_client.py:7 0.000s
      """
      Expected status code is 400 due to invalid API keys
      """
    When I check response for the endpoint function "TIME_SERIES_WEEKLY_ADJUSTED" and "MSFT" with "InValid" APIKeys # steps/rest_client.py:11 2.783s
    Then response should be "400"                                                                                   # steps/rest_client.py:31 0.000s
      Traceback (most recent call last):
        File "/usr/lib/python2.7/site-packages/behave/model.py", line 1456, in run
          match.run(runner.context)
        File "/usr/lib/python2.7/site-packages/behave/model.py", line 1903, in run
          self.func(context, *args, **kwargs)
        File "steps/rest_client.py", line 33, in step_impl
          assert response_code == str(context.status)
      AssertionError


  Scenario: Check Api status code 400 with missing mandatory parameters                                          # apitest/test2.feature:83
    Given The Url for the API                                                                                    # steps/rest_client.py:7 0.000s
      """
      Expected to go wrong while processing GET payload, the right status code is 400  
      """
    When I check response for the endpoint function "TIME_SERIES_WEEKLY_ADJUSTED" and " " with "InValid" APIKeys # steps/rest_client.py:11 1.227s
    Then response should be "400"                                                                                # steps/rest_client.py:31 0.000s
      Traceback (most recent call last):
        File "/usr/lib/python2.7/site-packages/behave/model.py", line 1456, in run
          match.run(runner.context)
        File "/usr/lib/python2.7/site-packages/behave/model.py", line 1903, in run
          self.func(context, *args, **kwargs)
        File "steps/rest_client.py", line 33, in step_impl
          assert response_code == str(context.status)
      AssertionError



Failing scenarios:
  apitest/test2.feature:75  Check Api status code 400 with mandatory parameters with invalid API KEYS
  apitest/test2.feature:83  Check Api status code 400 with missing mandatory parameters

0 features passed, 1 failed, 0 skipped
6 scenarios passed, 2 failed, 0 skipped
36 steps passed, 2 failed, 0 skipped, 0 undefined
Took 0m34.869s
"""

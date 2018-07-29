
#  Project Title: Relayr [Task2]

##API Test fo Relayr Test Assignment [Task 2]

 I have picked one task from https://github.com/toddmotto/public-apis

API Tested for Below time-series
https://www.alphavantage.co/documentation/#time-series-data

These api test are writen using python behave "which is a BDD test framework"
[Refrence]: https://behave.readthedocs.io/en/latest/


### Apikeys generated
API_key=13HOROS7Z6WRX1Q5

## Getting Started


### Prerequisites

What things you need to install the software and how to install them

Clone the project and you will get below directory list

-- apitest
    |-- README.md
    |-- __pycache__
    |   |-- mock_data.cpython-34.pyc
    |   `-- vars_file.cpython-34.pyc
    |-- features
    |   |-- apitest
    |   |   |-- test.feature
    |   |   `-- test2.feature
    |   |-- png
    |   |   |-- Screenshot\ from\ 2018-07-28\ 21-19-56.png
    |   |   |-- Screenshot\ from\ 2018-07-28\ 21-20-08.png
    |   |   `-- Screenshot\ from\ 2018-07-28\ 21-20-19.png
    |   `-- steps
    |       |-- mock_data.py
    |       |-- mock_data.pyc
    |       |-- rest_client.py
    |       |-- vars_file.py
    |       `-- vars_file.pyc
    |-- requirement.txt
    `-- sample_result.txt

6 directories, 15 files




### Installing

A step by step series of examples that tell you how to get a development env running


pip install -r requirement.txt

## Running the tests

root@c96ced1009c9 apitest]# behave features/apitest/test2.feature



### Test Output in BDD format 

[root@c96ced1009c9 apitest]# behave features/apitest/test2.feature 
Feature: Test API Response for www.alphavantage.co # features/apitest/test2.feature:1

  @rest_client
  Scenario: Check Api status code 200 with mandatory parameters                                                   # features/apitest/test2.feature:4
    Given The Url for the API                                                                                     # features/steps/rest_client.py:7 0.002s
      """
      200 implies that the response contains a payload that represents the status of the requested resource
      """
    When I check response for the endpoint function "TIME_SERIES_WEEKLY_ADJUSTED" and "MSFT" with "Valid" APIKeys # features/steps/rest_client.py:11 7.301s
    Then response should be "200"                                                                                 # features/steps/rest_client.py:31 0.001s
    And I match the response metadata keys "TIME_SERIES_WEEKLY_ADJUSTED"                                          # features/steps/rest_client.py:73 0.000s
    And response body should be valid and non empty                                                               # features/steps/rest_client.py:35 0.000s
    And Test data validation should pass                                                                          # features/steps/rest_client.py:174 0.000s
    And Recent and oldest datapoints returns valid value                                                          # features/steps/rest_client.py:123 0.035s
    And I validate the respose data keys for function "Meta Data"                                                 # features/steps/rest_client.py:87 0.000s
    And I validate the respose data keys for function "Weekly Adjusted Time Series"                               # features/steps/rest_client.py:87 0.000s

  Scenario: Check response body is valid                                                                          # features/apitest/test2.feature:21
    Given The Url for the API                                                                                     # features/steps/rest_client.py:7 0.000s
      """
      This test test for valid non empty response body
      """
    When I check response for the endpoint function "TIME_SERIES_WEEKLY_ADJUSTED" and "MSFT" with "Valid" APIKeys # features/steps/rest_client.py:11 4.299s
    Then response should be "200"                                                                                 # features/steps/rest_client.py:31 0.000s
    And I match the response metadata keys "TIME_SERIES_WEEKLY_ADJUSTED"                                          # features/steps/rest_client.py:73 0.000s
    And response body should be valid and non empty                                


## Authors

* **Rohit Vyas** - *Initial work*


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details





















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


#  Scenario: Check Api status code 400 with mandatory parameters with invalid API KEYS                               # apitest/test2.feature:75
#    Given The Url for the API                                                                                       # steps/rest_client.py:7 0.000s
#      """
#      Expected status code is 400 due to invalid API keys
#      """
#    When I check response for the endpoint function "TIME_SERIES_WEEKLY_ADJUSTED" and "MSFT" with "InValid" APIKeys # steps/rest_client.py:11 2.783s
#    Then response should be "400"                                                                                   # steps/rest_client.py:31 0.000s
#      Traceback (most recent call last):
#        File "/usr/lib/python2.7/site-packages/behave/model.py", line 1456, in run
#          match.run(runner.context)
#        File "/usr/lib/python2.7/site-packages/behave/model.py", line 1903, in run
#          self.func(context, *args, **kwargs)
#        File "steps/rest_client.py", line 33, in step_impl
#          assert response_code == str(context.status)
#      AssertionError



#	Test run status 

#	0 features passed, 1 failed, 0 skipped
#	6 scenarios passed, 2 failed, 0 skipped
#	36 steps passed, 2 failed, 0 skipped, 0 undefined
#	Took 0m34.869s

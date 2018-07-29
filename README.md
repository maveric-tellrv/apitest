
#  Project Title: Relayr [Task2]

## API Test fo Relayr Test Assignment [Task 2]

 	I have picked one task from https://github.com/toddmotto/public-apis

	API Tested for Below time-series
	https://www.alphavantage.co/documentation/#time-series-data

These api test are writen using python behave "which is a BDD test framework"
[Refrence]: https://behave.readthedocs.io/en/latest/


# What all is tested [Test Scenario]

Basically I have automated the test to check following conditions:
1. like response code [200 / 400 and 500]
	observed that these api does not return 400 error even if user dont pass manadatory params.
2. This api already have a problem for perfomance i.e  server response  fails if API is consumed very often with less time gap
3. This api test also check ths response data format for only JSON  [I have not added the test to validate the csv format]
4. Api meta data valdation test check the valida response
5. Validation to check the response of history data with mock data 
6. Validated the keys reutned in api responses for each metadata

The Scenario file looks like below and is self explanatory

	Given The Url for the API
    	When I check response for the endpoint function "TIME_SERIES_WEEKLY_ADJUSTED" and "MSFT" with "Valid" APIKeys
    	Then response should be "200"
    	And I match the response metadata keys "TIME_SERIES_WEEKLY_ADJUSTED"
    	And response body should be valid and non empty
    	And Test data validation should pass
    	And Recent and oldest datapoints returns valid value
    	And I validate the respose data keys for function "Meta Data"
    	And I validate the respose data keys for function "Weekly Adjusted Time Series"

## screnshot png folder
	I have attached a screen shot of each test run 
        png
         Screenshot\ from\ 2018-07-28\ 21-19-56.png
         Screenshot\ from\ 2018-07-28\ 21-20-08.png
         Screenshot\ from\ 2018-07-28\ 21-20-19.png


### Apikeys generated
	
	Api keys are also menstioned in "vars_file"
 
	API_key=13HOROS7Z6WRX1Q5

## Getting Started
	

### Prerequisites

What things you need to install the software and how to install them

Clone the project and you will get below directory list

 	apitest
     	README.md
     	features
     		apitest
     			test.feature
     			test2.feature
     		png
     			Screenshot\ from\ 2018-07-28\ 21-19-56.png
     			Screenshot\ from\ 2018-07-28\ 21-20-08.png
     			Screenshot\ from\ 2018-07-28\ 21-20-19.png
     		steps
    			mock_data.py
    			mock_data.pyc
    			rest_client.py
    			vars_file.py
    			vars_file.pyc
   			requirement.txt
    			sample_result.txt

	6 directories, 15 files


### Installing

A step by step series of examples that tell you how to get a development env running


pip install -r requirement.txt

## Running the tests

root@c96ced1009c9 apitest]# behave features/apitest/test2.feature



### Test Output in BDD format 
"""
root@c96ced1009c9 apitest]# behave features/apitest/test2.feature 
Feature: Test API Response for www.alphavantage.co # features/apitest/test2.feature:1

  rest_client
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

"""
## Authors

* **Rohit Vyas** - *Initial work*


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


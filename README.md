
#  Project Title: Relayr [Task2]

## API Test for Relayr Test Assignment [Task 2]

 	I have picked one task from https://github.com/toddmotto/public-apis

	API Tested for Below time-series project
	https://www.alphavantage.co/documentation/#time-series-data

	## Tested API
	https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=MSFT&apikey=demo

These api test are writen using python behave "which is a BDD test framework"
[Refrence]: https://behave.readthedocs.io/en/latest/

	Dockerfile to build and run test

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

## screanshot png folder
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
	Dockerfile
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

	edit vars_file.py file for api key changes
	 vi apitest/features/steps/vars_file.py

	# Please change as per requirement
	apikey="13HOROS7Z6WRX1Q5"


### Build & Run Test using Docker Container:
	Build the conatiner from Dockerfile:
	
	docker build -t apitestContainer . 	
	docker run --name apiTestRun1 -d apitestContainer

	To view the Logs:
	docker logs apiTestRun1


## Running the tests

	Run test using behave

	root@c96ced1009c9 apitest]# behave features/apitest/test2.feature



## Test Output in BDD format 


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



	 Scenario: Check Api status code 400 with missing mandatory parameters                                          # features/apitest/test2.feature:83
   	 Given The Url for the API                                                                                    # features/steps/rest_client.py:7 0.000s
      	"""
      	Expected to go wrong while processing GET payload, the right status code is 400  
      	"""
    	When I check response for the endpoint function "TIME_SERIES_WEEKLY_ADJUSTED" and " " with "InValid" APIKeys # features/steps/rest_client.py:11 1.313s
    	Then response should be "400"                                                                                # features/steps/rest_client.py:31 0.000s
     	 Traceback (most recent call last):
        	File "/usr/lib/python2.7/site-packages/behave/model.py", line 1329, in run
          	match.run(runner.context)
        	File "/usr/lib/python2.7/site-packages/behave/matchers.py", line 98, in run
          	self.func(context, *args, **kwargs)
        	File "features/steps/rest_client.py", line 33, in step_impl
          	assert response_code == str(context.status)
      	AssertionError



	Failing scenarios:
  	features/apitest/test2.feature:75  Check Api status code 400 with mandatory parameters with invalid API KEYS
  	features/apitest/test2.feature:83  Check Api status code 400 with missing mandatory parameters

	0 features passed, 1 failed, 0 skipped
	6 scenarios passed, 2 failed, 0 skipped
	36 steps passed, 2 failed, 0 skipped, 0 undefined
	Took 0m41.260s


## Sample Test run Using Docker:
	
	docker run --name apirun1 --rm  apitest123456
	[This display the testrun logs in console and remove the container]

			or

	docker run --name apirun7 -d apitest123456
	4895ffce17f4af4f55fb4014e414352d9d27c5d34baac74ecf5365bb0d339426

 	⚡ rovyas@rovyas  /tmp/dockerrun  docker logs apirun7   
                    
	Feature: Test API Response for www.alphavantage.co # features/apitest/test2.feature:1
  		@rest_client
  		Scenario: Check Api status code 200 with mandatory parameters                                                   # features/apitest/test2.feature:4
    		Given The Url for the API                                                                                     # features/steps/rest_client.py:7
      		"""
      		200 implies that the response contains a payload that represents the status of the requested resource
      		"""
    		When I check response for the endpoint function "TIME_SERIES_WEEKLY_ADJUSTED" and "MSFT" with "Valid" APIKeys # features/steps/rest_client.py:11
    		Then response should be "200"                                                                                 # features/steps/rest_client.py:31
    		And I match the response metadata keys "TIME_SERIES_WEEKLY_ADJUSTED"                                          # features/steps/rest_client.py:73
    		And response body should be valid and non empty                                                               # features/steps/rest_client.py:35
    		And Test data validation should pass                                                                          # features/steps/rest_client.py:174
    		And Recent and oldest datapoints returns valid value                                                          # features/steps/rest_client.py:123
    		And I validate the respose data keys for function "Meta Data"                                                 # features/steps/rest_client.py:87
    		And I validate the respose data keys for function "Weekly Adjusted Time Series"                               # features/steps/rest_client.py:87

## Authors

* **Rohit Vyas** - *Initial work*


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


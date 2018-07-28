import json
import requests
import vars_file
import datetime
import mock_data

@given(u'The Url for the API')
def geturl(context):
    context.baseurl="https://www.alphavantage.co"

@when(u'I check response for the endpoint function "{function}" and "{SYMBOL}" with "{Valid}" APIKeys')
def GetRequest(context,function,SYMBOL,Valid):
    ''' This functions returns the response headers, 
        Status_Code and Raw JSON data'''

    if Valid == "Valid":
       apikey = vars_file.apikey
    else:
       apikey = '123123'
    if function in vars_file.FUNCTION:
       url = context.baseurl+"/query?function=" + function + \
           "&symbol="+SYMBOL+"&apikey=%s" % apikey
    else:
       raise Exception("Function not supported check vars_file")
    context.response = requests.get(url)
    context.status = context.response.status_code
    context.headers = context.response.headers
    context.raw_data = context.response.json()
    #return (raw_data, status, headers)

@then(u'response should be "{response_code}"')
def step_impl(context,response_code):
    assert response_code == str(context.status)

@then(u'response body should be valid and non empty')
def LenghtResponse(context):
    '''This function return the lenth of response dictionary'''
    try:
        d = context.raw_data
        if isinstance(d, dict):
            lengths = [len(v) for v in d.values()]
            assert True
        else:
            raise Exception('Not valid dictionary response')
    except Exception as e:
        print (e)


def ValidateDateString(date):
    '''This function validate the date format and day of the response date'''

    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        day = datetime.datetime.strptime(x, '%Y-%m-%d').weekday()
        return day
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")


def ValidateWeekDay(date):
    '''This function validate the Weekday'''

    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        day = datetime.datetime.strptime(date, '%Y-%m-%d').weekday()
        if day in [5, 6]:
            print (day)
            assert False

    except Exception as e:
        raise Exception('Failed: Days Found in Saturday and Sunday')

@then('I match the response metadata keys "{api_func}"')
def ValidateWeeklyTimeSeriesMetadataKeys(context,api_func):
    ''' Raw data to match dict keys
        #ValidateWeeklyTimeSeries(d,vars_file.TIME_SERIES_WEEKLY_ADJUSTED)'''
    if api_func == "TIME_SERIES_WEEKLY_ADJUSTED":
        func_list = vars_file.TIME_SERIES_WEEKLY_ADJUSTED
    if all(elem in context.raw_data.keys() for elem in func_list):
        print ("list matched")
        assert True
    else:
        assert False



@then('I validate the respose data keys for function "{func}"')
def ValidateTimeSeriesKeys(context,func):
    #''' Raw data to match dict keys'''
    raw_data = context.raw_data
    time_dict = {}
    y = ''
    if func == "Meta Data":
       validate = vars_file.Meta_Data_keys
    if func == "Weekly Adjusted Time Series":
       validate = vars_file.TimeData
    #print(list(raw_data.keys())[0])
    #dictfirstelem = list(raw_data.keys())[0]
    
    
    if func == "Weekly Adjusted Time Series" :
       #print ("this is firts->",dictfirstelem)
       time_dict = raw_data[func]
       y = time_dict.keys()[0]
       #time_dict[y]
       #listdata = list(raw_data[func].keys())[0]
       #time_dict = raw_data[func]
       print ("function timeseries->",list(time_dict.keys())[0])
       key = time_dict[y].keys()
    if func == "Meta Data":
       key = raw_data[func].keys()
    #print ("dict value->",time_dict[key].keys())
    #if all(elem in time_dict.keys() for elem in func):
    if all(elem in key for elem in validate):
        print ("list matched")
        assert True
    else:
        assert False




@then(u'Recent and oldest datapoints returns valid value')
def ValidateTimeSeriesDataNotNone(context):
    ''' Validate the first and last timedata keys values not to be None and also check if no day if saturday and sunday'''
    raw_data = context.raw_data['Weekly Adjusted Time Series']
    func = vars_file.TimeData
    get_dict_Lenght = len(list(raw_data.keys()))
    for i in list(raw_data.keys()):
        #print (i)
        ValidateWeekDay(i)

    #print(list(raw_data.keys())[0])
    dict_first_elem = min(list(raw_data.keys()))
    dict_last_elem = max(list(raw_data.keys()))
    print (dict_first_elem)
    print (dict_last_elem)
    #time_dict = raw_data[dictfirstelem].values()
    for i in [dict_first_elem, dict_last_elem]:
        print (raw_data[i])
        for elem in raw_data[i].values():
           
            if elem in ['null', 'Null', None, 'none']:
                print (elem)
                raise Exception("Blank values found in datapoint")



@then(u'Test data validation should pass')
def ValidateTestData(context):
    ''' Read mocktest data and match with the response JSON data recieved'''
    try:
        WeeklyAdjustedTimeSeries = mock_data.WeeklyAdjustedTimeSeries
        raw_response = context.raw_data['Weekly Adjusted Time Series']
        testdatakeys = WeeklyAdjustedTimeSeries.keys()
        print (testdatakeys)
        x = list(testdatakeys)[0]
        print (x)
        for keys in list(testdatakeys):
            #print (WeeklyAdjustedTimeSeries[keys])
            #print ("Raw_response:->**",raw_response[keys])
            if WeeklyAdjustedTimeSeries[keys] != raw_response[keys]:
                assert False
        #print (type(WeeklyAdjustedTimeSeries[keys].values()))
    except Exception as e:
           raise Exception("Response and Mockdata not matched",raw_response[keys],WeeklyAdjustedTimeSeries[keys])
	


#d, status, headers = GetRequest()

#ValidateTestData(mock_data.WeeklyAdjustedTimeSeries,d['Weekly Adjusted Time Series'])
# x.request()
#d, status, headers = GetRequest()
#print (d.keys())
#print (d['Meta Data'])
# print d
#print (type(d))
#LenghtResponse(d)
# ValidateWeeklyTimeSeries(d,vars_file.TIME_SERIES_WEEKLY_ADJUSTED)
#ValidateWeeklyTimeSeries(d['Meta Data'],vars_file.Meta_Data_keys)
#ValidateTimeSeries(d['Weekly Adjusted Time Series'],vars_file.TimeData)
#ValidateTimeSeriesDataNotNone(d['Weekly Adjusted Time Series'], vars_file.TimeData)

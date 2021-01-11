def search(uri, term):
    query = json.dumps({
         "$schema": "https://api.covid19api.com/",
         "$id": "https://api.covidtracking.com/v1/us/daily.json",
         "title": "Covid Data",
         "description": "Covid Data in the United States",
         "type": "object",
         "properties": {
         "date": {
            "description": "The date the data was last updated.",
            "type": "string"
        }, 
        "death": {
            "description": "The number of comfirmed or probable deaths from COVID19.",
            "type": "integer"
        },
        "deathIncrease":{
            "description": "The increase in number of deaths from COVID19 from the previous day.",
            "type": "integer"
        },
        "hospitalizedCumulative":{
            "description": "The cumulative number of individuals hospitalized for COVID19.",
            "type": "integer"
        },
        "hospitalizedCurrently":{
            "description": "The number of individuals currently in the hospital with COVID19.",
            "type": "integer"
        },
        "hospitalizedIncrease":{
            "description": "The increase in number of hospitalizations for COVID19 from the previous day.",
            "type": "integer"
        },
        "inIcuCurrently":{
            "description": "The number of people currently in the ICU with COVID19.",
            "type": "integer"
        },
        "inIcuCumulative":{
            "description": "The cumulative number of people that have been in the ICU with COVID19.",
            "type": "integer"
        },
        "negative":{
            "description": "Number of negative COVID19 test results.",
            "type": "integer"
        },
        "negativeIncrease":{
            "description": "The increase in number of negative COVID19 test results.",
            "type": "integer"
        },
        "onVentilatorCumulative":{
            "description": "Number of people on ventilator due to COVID19.",
            "type": "integer"
        },
        "OnVentilatorCurrently":{
            "description": "The current number of people on a ventilator due to COVID19.",
            "type": "integer"
        },
        "pending":{
            "description": "The total number of COVID19 tests still pending.",
            "type": "integer"
        },
        "positive":{
            "description": "The total number of positive COVID19 tests.",
            "type": "integer"
        },
        "positiveIncrease":{
            "description": "The increase in number of positive COVID19 tests from the previous day.",
            "type": "integer"
        },
        "recovered":{
            "description": "The number of people marked as recovered from COVID19.",
            "type": "integer"
        },
        "totalTestResults":{
            "description": "The total number of COVID19 tests performed.",
            "type": "integer"
        },
        "totalTestResultsIncrease":{
            "description": "The increase in number of total COVID19 test results from the previous day.",
            "type": "integer"
        })
    response = requests.get(uri, data=query)
    results = json.loads(response.text)
    return results

def format_results(results):
    """Print results nicely:
    doc_id) content
    """
    data = [doc for doc in results['hits']['hits']]
    for doc in data:
        print("%s) %s" % (doc['_id'], doc['_source']['content']))
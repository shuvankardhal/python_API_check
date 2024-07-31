import requests
import json


base_url="https://httpbin.org/"

def get_request():
    url=base_url + "/get"
    response=requests.get(url)
    json_response=response.json()
    json_str= json.dumps(json_response, indent=3)
    assert response.status_code==200
    print("GET response",json_str )



def post_request():
    url=base_url + "/post"
    data={
       "X-Amzn-Trace-Id": "Root=1-66aa270f-41fd80f25cc4b95b00b0715d" ,
       "name":"PQR",
       "id": 124,
       "user": "hello"
    }
    response=requests.post(url,json=data)
    json_response=response.json()
    json_str= json.dumps(json_response, indent= 5)
    assert response.status_code==200
    print("POST response",json_str )
    #asserting the post response
    print(json_response['json']["name"])
    assert json_response['json']["name"]=="PQR"


def delayed_response(delaytime):
    url = base_url+ f"/delay/{delaytime}"
    response=requests.get(url)
    json_response=response.json()
    json_str= json.dumps(json_response, indent=3)
    assert response.status_code==200
    print("Delayed  response",json_str )


#401 is unauthorized status code, but since httpbin is an open source won't get unauthorized code
def trying_unauthorized(code):
    url=base_url +  f"/status/{code}"
    response=requests.get(url)
    print(response.status_code)
    assert response.status_code==401


# Trying a get method with json data can be considered a negative scenario
# get method expects a url and authorization, no request body, returns response schema
def negative_scenario():
    url=base_url + "/get"
    data={
        "a":"ABC",
        "b": 123,
        "c": False
    }
    response=requests.get(url,json=data)
    json_response=response.json()
    json_str= json.dumps(json_response, indent=3)
    assert response.status_code==200
    print("response",json_str )
    #print(json_response['json']["a"])

# we passed json request data but in response no output is given





get_request()
post_request()
delayed_response(4)
trying_unauthorized(401)
negative_scenario()

# calculatorAsARESTfulService
## This code implements Calculator as a RESTful webservice

Rest API
=======

Rest API is one of the popular webservices in the world. This code implements Rest API for performing basic arthemetic operations like addition, subtraction, multiplication and division.

Usage
-----

### Making a request using POST or GET: ###

#### Arthemetic Operations ####
Here, we are providing REST API service for performing arthemetic operations.
In this service we are going to pass query parameters to the http url. "num1", "num2" and "opp" parameters are of string data-type which we use to send the two numbers and the type of arthemetic operation to be performed.
Below is the request for performing addition operation. you can use either GET or POST requests for the below url  
```API
http://ec2-54-213-242-184.us-west-2.compute.amazonaws.com/api?num1=2&num2=3&opp=add
```
If you open the above link in a web browser the result will be:
```Result
{
  "result": 5.0
}

```

One can inspect the element in browser and find the following information:

```Inspectelement
Request URL:http://ec2-54-213-242-184.us-west-2.compute.amazonaws.com/api?num1=2&num2=3&opp=add
Request Method:GET
Status Code:200 OK
Remote Address:54.213.242.184:80

Connection:Keep-Alive
Content-Length:20
Content-Type:application/json
Date:Wed, 02 Nov 2016 01:21:46 GMT
Keep-Alive:timeout=5, max=100
Server:Apache/2.4.18 (Ubuntu)

```
From the above it is clear that server response is in the form of json data type


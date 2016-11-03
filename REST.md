# calculatorAsARESTfulService
This code implements Calculator as a RESTful webservice

Rest API
=======

Rest API is one of the popular webservices in the world. This code implements Rest API for performing basic arthemetic operations like addition, subtraction, multiplication and division.

Usage
-----

#### Arthemetic Operations ####
Here, we are providing REST API service for performing arthemetic operations.
In this service we are going to pass query parameters to the http url. "num1" and "num2" parameters are of string data-type which we use to send the two numbers on which the required arthemetic operation is to be performed.
For convenience, here i am using data 5 and 2 in "num1" and "num2" respectively.

####Addition
Below is the request for performing addition operation.
```API
http://ec2-54-213-242-184.us-west-2.compute.amazonaws.com/api/add?num1=5&num2=2
```
If you open the above link in a web browser the result will be:
```Result
{
  "result": 7.0
}

```

One can inspect the element in browser and find the following information:

```Inspectelement
Request URL:http://ec2-54-213-242-184.us-west-2.compute.amazonaws.com/api/add?num1=5&num2=2
Request Method:GET
Status Code:200 OK
Remote Address:54.213.242.184:80

Connection:Keep-Alive
Content-Length:20
Content-Type:application/json
Date:Thu, 03 Nov 2016 00:29:22 GMT
Keep-Alive:timeout=5, max=100
Server:Apache/2.4.18 (Ubuntu)

```
From the above it is clear that server response is in the form of json data type.

####Subtraction
In a similar manner Subtraction can also be performed by using the below URL

```API
http://ec2-54-213-242-184.us-west-2.compute.amazonaws.com/api/sub?num1=5&num2=2
```

If you open the above link in a web browser the result will be:
```Result
{
  "result": 3.0
}
```

One can inspect the element in browser and find the following information:

```Inspectelement
Request URL:http://ec2-54-213-242-184.us-west-2.compute.amazonaws.com/api/sub?num1=5&num2=2
Request Method:GET
Status Code:200 OK
Remote Address:54.213.242.184:80
Response Headers
view source
Connection:Keep-Alive
Content-Length:20
Content-Type:application/json
Date:Thu, 03 Nov 2016 00:47:32 GMT
Keep-Alive:timeout=5, max=100
Server:Apache/2.4.18 (Ubuntu)

```
####Multiplication
In the same way, request for multiplication can be made from the below URL:

```API
http://ec2-54-213-242-184.us-west-2.compute.amazonaws.com/api/mul?num1=5&num2=2
```
and the result and inspect elements are below

```Result
{
  "result": 10.0
}
```
```Inspectelement
Request URL:http://ec2-54-213-242-184.us-west-2.compute.amazonaws.com/api/mul?num1=5&num2=2
Request Method:GET
Status Code:200 OK
Remote Address:54.213.242.184:80
Response Headers
view source
Connection:Keep-Alive
Content-Length:21
Content-Type:application/json
Date:Thu, 03 Nov 2016 00:51:23 GMT
Keep-Alive:timeout=5, max=100
Server:Apache/2.4.18 (Ubuntu)

```

####Division
Finally for division,

URL
```API
http://ec2-54-213-242-184.us-west-2.compute.amazonaws.com/api/div?num1=5&num2=2
```

Result will be
```Result
{
  "result": 2.5
}
```
```Inspectelement
Request URL:http://ec2-54-213-242-184.us-west-2.compute.amazonaws.com/api/div?num1=5&num2=2
Request Method:GET
Status Code:200 OK
Remote Address:54.213.242.184:80
Response Headers
view source
Connection:Keep-Alive
Content-Length:20
Content-Type:application/json
Date:Thu, 03 Nov 2016 00:52:41 GMT
Keep-Alive:timeout=5, max=100
Server:Apache/2.4.18 (Ubuntu)
```

#! /usr/bin/python3

print("Content-type:text/html \r\n\r\n")
import cgi 
formdata = cgi.FieldStorage()
a = formdata.getvalue("firstnum")
b = formdata.getvalue("secondnum")
op = formdata.getvalue("operation")
a = float(a)
b = float(b)


if(op == "subtraction"):
	c = a-b
elif (op == "addition"):
	c = a+b
elif (op == "multiplication"):
	c = a*b
else:
	c = a / b

print(c)

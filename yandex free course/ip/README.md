### Task Description 

In this task, you have to answer the question whether 
the given input string is a valid IPv4 or IPv6 address. 
Solve the problem without using regular expressions.

A valid IPv4 address has the following format: 
s_1.s_2.s_3.s_4, where s_i is an integer from 0 to 255. 
The s_i numbers must not have leading zeros.

A valid IPv6 address has the following format: 
s_1:s_2:s_3:s_4:s_5:s_6:s_7:s_8, 
where s_i is the hexadecimal number representation, 
consisting of no more than four characters. 
Each number may contain leading zeros. 
Allowed characters are 0-9, a-f, A-F. 
s_i cannot be an empty character sequence.

Note: in reality, in an IPv6 address, 
it is permissible to replace a group of null fields with ::, 
but for simplicity, this rule does not need to be taken 
into account in this task.

### Input 

The input is a string consisting of Latin letters, 
numbers and symbols "." and ":". 
The string length does not exceed 100 characters.

### Output

Print "IPv4" if the string is a valid IPv4 address.

Print "IPv6" if the string is a valid IPv6 address.

Print "Error" if the string is not a valid IP address.

### Solution Description

Checking if string matches ip_v6 or ip_v4 template using 
```pattern_break``` solution.
Then checking numbers in address.

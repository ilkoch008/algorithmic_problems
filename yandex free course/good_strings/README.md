### Task Description 

We call a string good if it does not contain two adjacent letters that differ only in case. 
For example, the string "abba" is good, but the string "aBba" is not.

A string can be converted: if two adjacent characters denote the same letter, 
but are written in different registers, then they can be deleted. 
In this case, the string will “collapse”, that is, 
no spaces will be formed during deletion.

A chain of such transformations can turn any string into a good one.
Given a string, find a good string to turn it into.

### Input 

The input is a string consisting of uppercase and lowercase Latin letters. 
The string length does not exceed 10^5.

### Output

Output a good string that the given one can be turned into.

### Solution Description

We're inserting characters one by one into result, checking if last inserted character and 
current are good. If they are bad we pop last added character and don't add current. 

### Task Description 

You are given a number written in Roman numerals. Get the same number in normal notation (in Arabic numerals).
Roman notation for numbers may include the following characters:

- 'I' - 1
- 'V' - 5
- 'X' - 10
- 'L' - 50
- 'C' - 100
- 'D' - 500
- 'M' - 1000

1. The numbers 'I', 'X', 'C' and 'M' cannot be used more than three times in a row. 
2. The digits 'V', 'L', and 'D' cannot be used more than once in the entire notation of the number.
3. The numbers are usually written in descending order from left to right. For example, the number 350 would be written as 'CCCL'.

However, there are exceptions:

To get '4' or '9', put 'I' before 'V' or 'X' respectively
To get '40' or '90', put 'X' before 'L' or 'C'.
To get '400' or '900', put 'C' before 'D' or 'M'.

### Input 

The single line contains the number in Roman numerals. The record length does not exceed 15.

### Output

Output the number written in Arabic numerals. If the notation of the number is incorrect, then print -1.

### Solution Description

First I check the first two rules. Then I decompose number character by character 
(or by two characters if it's possible and necessary), 
checking third rule and exceptions. 

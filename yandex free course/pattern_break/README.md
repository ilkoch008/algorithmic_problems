### Task Description 

In this task, you need to determine if a string matches a particular pattern. 
The template is specified in the following format:

- Symbol "?" matches one occurrence of any character;
- The character "*" matches an arbitrary number of any characters, including zero characters;
- The rest of the pattern characters must match the characters in the string.

### Input 

The first line is a template. The second is the string to be checked.
The pattern and string cannot exceed 2000 characters in length and cannot be empty.

The string consists only of lowercase Latin letters. 
The template consists of lowercase Latin letters and signs "?" and "*".

### Output

Print "YES" if the string matches the pattern, and "NO" if it doesn't.

### Solution Description

#### Recursive (with stack)

This one exceeds time limit.

One by one we take characters from string and from template until we face "*".

After facing "*" we add to stack every tail substring that remains. 

#### DP

Idea is the same: using star we can jump through as many symbols as we need.
But here we represent this idea in other way: 
imagine matrix of zeros (```False``` bools) with size [size_of_template x size_of_string]. 
We can move ```True``` diagonally if current part of template is equal to current
part of string, and we can move in three directions (down, diagonally and right) if we 
face "*". 

Also, to optimise memory use we can store only two last rows instead of whole matrix.

To make start easier I add spaces at the beginning of template and string.
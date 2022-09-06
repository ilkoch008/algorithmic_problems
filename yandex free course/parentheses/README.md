### Task Description 

In this problem, a regular bracket sequence (RBS) is a regular 
bracket sequence of parentheses and square brackets, 
where no pair of square brackets can contain a pair of parentheses.

For the given number n print all the RBSs from n brackets in lexicographic order.
The order of characters is as follows: ’(’ < ’[’ < ’)’ < ’]’.

### Input 

The single line contains the number of brackets n, 0≤n≤16.

### Output

Print the correct bracket sequences in lexicographic order, 
one per line. Parentheses within the same line are consecutive 
and are not separated by spaces.

### Solution Description

Recursively generate all possible sequences using stack to ensure
their correctness. 

Correct lexicographic order obtains with correct order of ```yield```s.

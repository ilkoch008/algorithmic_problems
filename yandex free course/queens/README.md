### Task Description 

Determine all arrangements of n queens on an n×n chessboard 
where the queens cannot attack each other.

As an answer to the problem print on the first line the number of arrangements, 
and then all the arrangements in the following format: 
one arrangement is described by n numbers. i-th number describes i -th line of the board, 
namely, it is equal to the number of the cell in which the queen stands on the current line.
Lines are numbered from top to bottom from 1 to n. 
Cells within a row are numbered from 1 to n from left to right.

### Input 

The input is a single number n (1≤n≤13).

### Output

Print a single number — the number of possible arrangements. 
Then print the arrangements one per line in random order.

### Solution Description

We try to put queen into every cell in row: first we check if there is no other queen on
current diagonals and column, then if we can put queen in this cell, we put it there
and add current diagonals and column to already occupied. Then we continue recursion.
We stop recursion when we checked last row.

My solution exceeds time limit on n=13.
In order to optimize it I tried using dictionary instead of list for saving
occupied columns and diagonals(not set because
order preservation is only guaranteed for dictionary).
This trick gave 31% speedup on n=12, but it's still not enough for n=13.

### Task Description 

Cards are laid out on the table in a row, each card has a natural number written on it. 
In one move, it is allowed to take a card either from the left or from the right end of the row. 
There are k moves in total. The final score is equal to the sum of the numbers on the selected cards. 
Determine the maximum score you can get at the end of the game.

### Input 

The first line contains the number of cards n (1≤n≤10^5).
The second line contains the number of moves k (1≤k≤n).
The third line contains the numbers written on the cards separated by a space.
The i-th number is written on the i-th card from the left. All numbers are natural and do not exceed 10^4.

### Output

Print a single integer — the maximum amount of points that can be scored after making k moves.

### Solution Description

Sliding window.

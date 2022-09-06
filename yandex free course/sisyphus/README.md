### Task Description 

In this task, you will move stones. Initially there are n piles of stones. 
Pile i weighs a_i kilograms. Heaps can be combined. 
When combining heaps i and j, a_i+a_j units of energy are spent, 
while the two initial heaps disappear and a heap of weight a_i+a_j appears. 

Determine the least amount of energy that must be expended 
to combine all the piles into one.

### Input 

The first line contains a number n (1≤n≤10^5).
The next line contains the masses of heaps separated by spaces — a_i (1≤a_i≤10^6).

### Output

Print a single number — the minimum energy that must be spent to unite all the heaps.

### Solution Description

Greedy. Choose two smallest piles, combine them into one and put it back. 
Repeat until we get one pile in heap.

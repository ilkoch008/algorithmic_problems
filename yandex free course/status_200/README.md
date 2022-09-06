### Task Description 

You are given an array of natural numbers a_i.
Find the number of such pairs of elements (a_i, a_j) 
where ```|a_i-a_j|%200 == 0``` and i<j.

### Input 

The first line gives the size of the array n (1≤n≤200000).
The second line contains the elements of the array separated by a space a_i (1≤a_i≤10^9).

### Output

Print a single integer — the number of pairs matching the above condition.

### Solution Description

```|a_i-a_j|%200 == 0``` is equivalent to ```|(a_i-a_j)%200| == 0```. 
So for every number we get remainder of the division by 200 and check how many same remainders we already got.

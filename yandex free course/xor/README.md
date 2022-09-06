### Task Description 

In this task, it is required to 
find two elements x_i and x_j (1≤i≤j≤n) 
from a given array of length n, which would give the maximum value 
of the function x_i⊕x_j, where ⊕ means the bitwise exclusive “or” 
operation (xor).

### Input 

The first line contains the size of the array n (1≤n≤10^5).

The second line contains n space-separated integers x_i (1≤x_i≤2^31−1).

### Output

Print a single number — the maximum xor value that can be obtained.

### Solution Description

```
m = a ^ b 
m ^ b = a ^ b ^ b
m ^ b = a
```
So we 31 times try to increase potential max xor
(using mask to obtain prefixes of initial numbers).

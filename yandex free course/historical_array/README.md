### Task Description 

In this task, you need to implement a historical array data structure. 
The historical array initially has size n and is filled with zeros. 
It supports the following operations:

- set(index, value) - set the element at position i to value
- begin_new_era(era_id) - this operation starts a new era with era_id number. 
Only one era is active at any given time. The initial era has index era_id=0. 
When a new era begins, the previous one ends.
- get(index, era_id) - get the value of the element at position index 
at the end of the era_id era.

### Input 

The first line contains the size of the historical array n (1≤n≤100000).
The second line gives the number of operations performed on the array — q (1≤q≤100000)
The following q lines contain operations, one per line. 
There are three types of operations:
- set index value (0≤index≤n−1, 0≤value≤10^9)
- begin_new_era era_id (1≤era_id≤10^9)
- get index era_id (0≤index≤n−1, 0≤era_id≤10^9)

It is guaranteed that when requesting a value from a specific era, this era has already ended.

It is guaranteed that when creating an era with the era_id identifier, this identifier has not yet been used.

### Output

For each operation of the third type, it is necessary to output on a separate line 
the value that the array element with index number contained at the end of the era_id era.

### Solution Description

Historical array is represented by an array of dictionaries. 
In dictionary stored era_num (key) and value.
era_ids are mapped to era_nums in another dictionary.
To find necessary value by index and era_id we find dictionary in array by index. 
Then we map era_id to era_num and trying to find value by era_num.
If necessary era_num is not in dictionary we find suitable era_num using
modified binary search.

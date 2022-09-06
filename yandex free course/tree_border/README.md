### Task Description 

Given a rooted binary tree on N vertices. Let's say that a node v is on the edge of the tree if it fits any of the following conditions:

- v is a leaf;
- let v be at a distance h from the root. Then
v is the leftmost or rightmost vertex among all vertices at distance h from the root.

Find all vertices that are on the boundary of the tree.

### Input 

The first line contains two integers: 
the number of vertices in the tree n (1≤n≤2⋅10^5) 
and root_id (0≤root_id≤n−1) — the number of the root vertex.

The next n lines describe the vertices. 
Each vertex is described by two numbers separated by a space: 
the id of the left child and the id of the right child. 
All id's are in the range [0;n−1]. 
If the vertex does not have any child, 
then its id will be -1 instead. 

It is guaranteed that the input data is correct.

### Output

In a single line, print in any order, separated by a space, 
all the id's of the vertices that are on the border of the tree. 
Each vertex must be drawn at most once.

### Solution Description

Going down the tree using BFS and adding first and last nodes 
at each level.

Leaf nodes are added while reading tree.
But it didn't save situation :)

This solution exceeds time limit.

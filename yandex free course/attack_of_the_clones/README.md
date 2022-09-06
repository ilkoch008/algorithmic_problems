### Task Description 

In this task, you need to create a copy of a connected graph. 
The original graph is given by one vertex. 
The vertex contains its unique value, value, and a list of neighbors. 
A graph will be considered a copy if the copy graph has a connection 
between vertices with values v_1 and v_2 if and only if it exists in the original graph. 
All vertices of the copy graph must be recreated, that is, 
vertices from the original graph cannot be reused. 
Create new vertices using public constructors and factory methods specified in templates.

### Input 

The ```cloneGraph``` function takes a starting vertex that belongs to the original graph.
You will find the exact signatures in the templates located on the disk.
It is guaranteed that the number of vertices and edges of the graph does not exceed 10^5.

### Output

The ```cloneGraph``` function must return a vertex that is a copy 
of the starting vertex in the original graph.

### Solution Description

BFS with old to new mapping:
in cycle we get new node from map using old node popped from stack,
then check all neighbours of old node, if node already in the map we 
add it in neighbours list of new node, else we create new node 
(copy of current neighbour) and add it everywhere 
(to the map, to the stack, to the neighbours list of new node).

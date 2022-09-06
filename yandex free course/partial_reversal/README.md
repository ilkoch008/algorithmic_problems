### Task Description 

In this problem, you need to reverse part of a linked list. 
Each vertex of the list is described by a Node structure, 
each instance stores a pointer to the next vertex, 
or null (nullptr, None, nil) if the vertex is the last one. 
At the given indexes from and to, expand all vertices on the segment from ```from```
to ```to``` inclusive. Note that the numbering in the ```from``` 
and ```to``` indices starts from one.

### Solution Description

Using window with three nodes reverse whole needed part and
in the end change edge node links.

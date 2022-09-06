### Task Description 

Given a rooted tree on N vertices and a number X. 
Each vertex contains a number — its weight.
Let's call the ascending path a_i, p(a_i), p(p(a_i)), ..., 
where p is the parent of the vertex a.

In other words, an ascending path is a path that starts at some vertex 
and moves towards the root (not necessarily reaching it). 
The path can consist of one vertex.
The weight of a path is the total weight of the vertices on this path.

Find the number of ascending paths with weight X.

### Input 

The first line gives the number of vertices and the number X.
The next n lines contain vertices, one per line.
The i-th vertex is given by two numbers — p_i and w_i, separated by a space.
p_i is either the number of the parent node of node i, in this case 0≤p_i≤n−1, or −1 if node i is the root.
w_i is the weight of vertex i (−10^4≤w_i≤10^4).

### Output

Print one integer — the number of ascending paths of weight X.

### Solution Description

DFS with prefix sum: store in dictionary prefix sums that we already have seen 
(and their number).

In each node we check if we can compose X with some of seen prefix sums 
and current prefix sum (X = current_prefix_sum - some_of_previous_prefix_sum).
And add number of suitable seen_prefix_sums to result.

### Note

In order to reduce memory use I tried to avoid recursion and stack.
That is why my implementation may seem strange.

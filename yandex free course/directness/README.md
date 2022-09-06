### Task Description 

You are given n points located on a plane. 
Determine if all these points lie on the same line.

### Input 

The first line contains the number of points n (2≤n≤10^5).

The next n lines contain the points themselves, one per line. 
Each point is given by two coordinates - x_i, y_i, 
written with a space. 
Coordinates are integers not exceeding 10^12 in absolute value. 
The points may coincide with each other.

### Output

Print "YES" if all n points lie on the same line, and "NO" otherwise.

### Solution Description

We take the first two points with different coordinates, 
and then just check the others.

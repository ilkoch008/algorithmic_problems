### Task Description 

You are given two sequences of segments. 
Each segment is specified by the start and end coordinates — [start_i, end_i]. 
The segments of each sequence are sorted from left to right and do not have common points.

Find the intersection of two sequences of line segments. 
That is, the third sequence of segments, such that:

- Each segment is contained in some segment of both the first and second sequences;
- No segment can be increased;
- The segments of this sequence have no common points;
- The segments in the sequence are also sorted in ascending order.

### Input 

The first line contains the number of segments in the first sequence n (0≤n≤100000).
The next n lines contain segments of the first sequence, one per line. 
Each segment is written in the start_i end_i format, 
the start and end coordinates are non-negative integers 
not exceeding 10^9 in absolute value.

Line n+2 contains the length of the second sequence m, (0≤m≤100000).

The next m lines contain segments of the second sequence.

It is guaranteed that end_i<start_{i+1} and also that end_i−start_i>0.

### Output

Print, one per line, the sorted segments from the intersection 
of the sequences in the same format as in the input. Note that 
the length of the segments at the intersection can be zero, 
in which case start_i=end_i.

### Solution Description

Store both sequences in class that have one helper method: ```get_next_point```. 
This method returns next nearest point. Current position is represented by 
4 pointers:

```n_seg1``` - current number of segment in 1-st sequence

```n_seg2``` - current number of segment in 2-nd sequence

```p_seg1``` - current number of point in current segment from 1-st sequence

```p_seg2``` - current number of point in current segment from 2-nd sequence

Also, this method adds to result segments with zero length (dots).

Using ```p_seg1``` and ```p_seg2``` we can understand if we are into 
intersection of segments or not.

To get intersection of two sequences we call ```get_next_point``` checking 
if we are into intersection (and storing intersection if we are)
until we come to the end of one of sequences.
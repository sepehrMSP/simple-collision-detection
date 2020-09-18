
# Space Partitioning 

We intend to implement a _space_ _partioning_ algorithm. To introduce with _space_ _partitioning_ algorithms and data structures you use [this link](https://en.wikipedia.org/wiki/Space_partitioning) and [this link](cs.ucf.edu/~dcm/Teaching/COT4810-Spring2011/Presentations/JonLeonardSpacePartitioningDataStructures.pdf
). Also, a list of data structures that can be used in _space_ _partitioning_ is provided in [this link](https://en.wikipedia.org/wiki/List_of_data_structures).

My code is an implementation of _quad_ _tree_.

## Problem Description

A list of rectangles is given. you must output all rectangles which have an intersection with each other and use a _space_ _partitioning_ data structure in your algorithm. Also using multithreading is forbidden and your program must execute sequentially. 

### Input and Output

In every line a rectangle is give in the format of $(x_{min}, x_{max}, y_{min}, y_{max})$ and the end comes $end$. Coordinates of every triangle is in interval of $(-1000,1000)$. In each line of output, an intersection is printed in the format of $(index_1, index_2)$ which $index$es are the number of corresponding rectangles. The number of rectangles is in the order of their input and starts at $0$. Note that coordinates of rectangles are not necessarily integers.

***example:***
```
# input 
1 3 0 4
5 9 4 7
1 7 0 5
2 12 2 8
1 5 0 10
1 3 0 4
5 9 4 7
end
# output
1 2
1 3
2 6
4 5
0 2
0 3
0 5
2 3
3 6
0 4
1 6
2 5
3 4
2 4
3 5
```

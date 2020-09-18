
# Space Partitioning 

We intend to implement a _space_ _partioning_ algorithm. To introduce with _space_ _partitioning_ algorithms and data structures you use [this link](https://en.wikipedia.org/wiki/Space_partitioning) and [this link](cs.ucf.edu/~dcm/Teaching/COT4810-Spring2011/Presentations/JonLeonardSpacePartitioningDataStructures.pdf
). Also, a list of data structures that can be used in _space_ _partitioning_ is provided in [this link](https://en.wikipedia.org/wiki/List_of_data_structures).

My code is an implementation of _quad_ _tree_.

## Problem Description

A list of rectangles is given. you must output all rectangles which have an intersection with each other and use a _space_ _partitioning_ data structure in your algorithm. Also using multithreading is forbidden and your program must execute sequentially. 

### Input and Output

In every line a rectangle is give in the format of <img src="/SpacePartitioning/tex/ca1f61b9abdbfd5631f4b94f7d379b60.svg?invert_in_darkmode&sanitize=true" align=middle width=174.28223009999996pt height=24.65753399999998pt/> and the end comes <img src="/SpacePartitioning/tex/be55d79488293e4d21476412b12358a3.svg?invert_in_darkmode&sanitize=true" align=middle width=26.07697784999999pt height=22.831056599999986pt/>. Coordinates of every triangle is in interval of <img src="/SpacePartitioning/tex/a9622cda00dcd820804974e427b58102.svg?invert_in_darkmode&sanitize=true" align=middle width=98.63042475pt height=24.65753399999998pt/>. In each line of output, an intersection is printed in the format of <img src="/SpacePartitioning/tex/5c8300f934edb2da264f649081b07f04.svg?invert_in_darkmode&sanitize=true" align=middle width=117.11062109999997pt height=24.65753399999998pt/> which <img src="/SpacePartitioning/tex/66c41bf4c6328a51db5435cb811467d8.svg?invert_in_darkmode&sanitize=true" align=middle width=41.13519299999999pt height=22.831056599999986pt/>es are the number of corresponding rectangles. The number of rectangles is in the order of their input and starts at <img src="/SpacePartitioning/tex/29632a9bf827ce0200454dd32fc3be82.svg?invert_in_darkmode&sanitize=true" align=middle width=8.219209349999991pt height=21.18721440000001pt/>. Note that coordinates of rectangles are not necessarily integers.

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

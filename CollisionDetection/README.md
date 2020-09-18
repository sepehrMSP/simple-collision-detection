
# Collision Detection

In this part, we intend to implement an algorithm for collision detection of 2 n-gon. For this problem read _pairwise_ _pruning_ section of [this link](https://en.wikipedia.org/wiki/Collision_detection). Two n-gons are given in the format of 2 lists of triangles (each n-gon is partitioned to triangles). These two n-gons have a collision if any of their triangles have collisions. So we must implement an algorithm to detect collision between two lists of triangles. To have an optimized implementation we should use _bounding_ _volume_ _hierarchy_ algorithms. [this link](http://www-ljk.imag.fr/Publications/Basilic/com.lmc.publi.PUBLI_Inproceedings@117681e94b6_1860ffd/bounding_volume_hierarchies.pdf) and [this link](https://cg.informatik.uni-freiburg.de/course_notes/sim_06_boundingVolumeHierarchies.pdf) can be helpful in this regard.
I've used _AABB_ algorithm cause of easier implementation. Also, there is an optimized (and dirty!) code that uses brute force to answer the question. Besides, there in `triangle_intersection.py` there is a python code to see whether two triangles collide or not in an optimized way. 
Using multithreading code is forbidden and code must execute sequentially. 

### Input and Output

In each testcase, 30 couple of n-gons are given. the following input will be given to your code 30 times:
At first triangles of first n-gons are inputted. In each line a triangle is given in the format of <img src="/CollisionDetection/tex/a5f26664ef2b5e2e7d971dde44622cb4.svg?invert_in_darkmode&sanitize=true" align=middle width=132.31751939999998pt height=14.15524440000002pt/>. After finishing the first n-gon's triangle there comes an `end1` and then triangles of the next n-gon are inputted in the same way. In the end, there comes an `end2`. If two n-gons had intersection `1` will print in output otherwise `0` will print. Therefore, your output must contain 30 lines of `1` or `0`.

***example 1:***
```
# input
1 1 1 2 2 1
1 2 2 1 3 3
end1
1 3 2 3 3 1
end2
# output
1
```

***example 2:***
```
# input 
1 1 1 3 2 3
end1
1 1 2 3 3 1
end2
# output
0
```



***NOTE: There is no access to all testcases***

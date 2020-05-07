# maximum-element-unique-position
This is a Python program to print the maximum element in each row in an array at unique positions. Suppose in a 3x3 array, the maximum element in the first row is at the position 2 (indexing starting from 1), the other rows can't select the maximum on position 2 even if it is the maximum in that row.
Let's understand this with another example. I take a 4x4 matrix by inputting n = 4 and passing 4 values in each of the 4 rows like this...
Enter the size of the matrix: 4
12 34 56 79
23 56 78 90
31 45 77 13
66 87 07 12
The output will be:
[3, 2, 1, 0] 
[79, 78, 45, 66]
The first row indicates the position of the maximum in each row. As you can see in this no position was repeated.
The second row indicates the values at those positions.

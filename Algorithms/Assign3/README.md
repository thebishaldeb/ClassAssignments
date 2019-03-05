## Assignment 3

<p style="text-align: justify"> <strong>a) </strong> A man has n apples A = {A0, A1, A2, ..., An1} in his bag where Ai is the size of the i-th apple. Suppose that no two apples are of the same size.The man will not tell you the size of any of the Ai’s. The man can however, can answer queries of the form IsLargeApples( i, j) which returns 1, −1 according to  whether Ai is bigger than Aj or Ai is smaller than Ai, respectively. Write a program to create an array S = {s0, s1, s2, · · · , sn−1} of indices such that {As0 < As1 < As2 < · · · < Asn−1 } is the sorted sequence of the apples in the order of their sizes. Modify merge sort to solve your problem. Your modification should use the array S to compare sizes of the apples. Here you move/swap/copy the indices instead of the sizes. For example, if si = j, then Asi is the j-th apple Aj (or the size of the j-th apple). But you cannot access Aj or its size, only IsLargeApples( i, j) can access the array A. However, you are free to make any modification to your own array S. 
</p>

<p style="text-align: justify"> <strong>b) </strong> The man also has n packets P0, P1, P2, · · · , Pn1. It is given that for every apple Ai there is a unique packet Pj such that Ai fits tightly in Pj. But Ai can also fit in a bigger packet,
but does not fit in a smaller packet. Write a program that finds the exact matching of the apples and packets, that is, you need to create an array M = {m0, m1, m2, · · · , mn−1} such that the ball Ai is the exact match for the box Pmi. In Part a), you have already sorted the apples according their sizes. Now if you can sort the packets, you can find the
matching. Unfortunately, the man will not tell you anything about the comparisons of packet sizes. Instead he will answer queries of the form TightFit(i,j). The answer is 0 if the packet Pj is the exact match for the ball Ai. If Ai fits in Pj but it is not tight, the answer is 1. The answer is a -1 if apple Ai is bigger than the packet Pj. Create M using modified version pf quick sort and Mergesort. You may or may not use the array S available from Part 1. Now, use TightFit( ) queries, but IsLargeApples( ) queries are not allowed. </p>

<br />

### Solution

* `probA.py` ha the solution of problem a
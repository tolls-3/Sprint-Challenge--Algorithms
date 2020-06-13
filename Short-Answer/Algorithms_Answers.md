#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Linear O(n)

b) O(n log n)


c) Linear O(n)

## Exercise II
Assumptions: say we have 10 floors
Using the binary search algorithm, and assumming we have numbers of floor in this building in a sorted order. 

In order to determine the floor (f) at which the number of dropped + broken egss is minimized?

We will take note of the lowest= 0 floor and highest floors= 10 floor at  each point of the proposed solution. 

Selecting a mid point of 5 floor. 
1. We drop an egg from the middle, if the egg breaks we know that floor f can not be a higher floor from here, we reduce our highest floor to = mid - 1

2. else if eggs does not break at middle floor, we know that floor f must be a higher floor and so we increase our lowest floor to = mid + 1

We repeat step 1 and 2 until we find highest floor that eggs do not break which will be floor f. 

This algorithm will run in O(log n) time complexity because at each point in the search the number of floors are halved and the relevant half is kept while the irrelevant half to our search is discarded. 


#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

```python
a)  a = 0 # 0(1)
    while (a < n * n * n): #0(n)
      a = a + n * n # 0(n)

    # time complexity of the algo is 0(n)
```

```py
b)  sum = 0 #0(1)
    for i in range(n): #0(n)
      j = 1 #0(1)
      while j < n: #0(n^2)
        j *= 2 #0(1)
        sum += 1 #0(1)

    # time complexity of the algo is 0(n^2) 
```

```py
c) def bunnyEars(bunnies):
      if bunnies == 0: #0(1)
        return 0

      return 2 + bunnyEars(bunnies-1) #0(n)

      # time complexity of the algo is 0(n)
```
## Exercise II

```
Assuming floors in n-story building are in a sorted order. Using the binary search technique. 

Since eggs will only break from floor n and above, first select a mid point amongst the list of floors in the building, then drop an egg, if egg breaks, then remove all floors from midpoint above from experiments and reselect a mid point from the remaining floors in the building again, repeat this until you get to a floor where egg does not break when dropped and this will be the value of f in which broken eggs are minimized. 

Essentially, we want to sort through the list of sorted floors in order to find the optimal floor. 

best case: 0(1)
worst case and average case: 0(log(n))
```



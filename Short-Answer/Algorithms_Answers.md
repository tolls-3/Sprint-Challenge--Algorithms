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



Renders Mandelbrot sets. Best if used in an Ipython notebook.

![](https://i.imgur.com/PN6JcGP.png)


The recurrence relations can also be modified to give rise to new fractals. For example:

```
def iterate(c, max_iterations=25):
    z = [0,0,c]
    n = 2
    for _ in range(max_iterations):
        if z[n].mag > 6:
            return n-2
        z.append(z[n]**2 + z[n-1])
        n+=1
    return n-2
```
This yields the set.

![](https://i.imgur.com/YGKDiRW.png)


To do:
+ Add high-precision floating point library
+ GPU acceleration

Renders Mandelbrot sets. Best if used in an Ipython notebook.

![](https://i.imgur.com/PN6JcGP.png)


The recurrence relations can also be modified to give rise to new fractals. For example:

```
def iterate(c, max_iterations=25):
    z = [0,0,c]
    n = 3
    i = 0
    for _ in range(max_iterations):
        if z[n-1].mag > 6:
            return i
        #z.append(z[n-1] + z[n-3]**2 + z[2] )
        z.append(z[n-1]**2 + z[n-2])
        n+=1
        i+=1
    return i
```
This yields the set.

![](https://i.imgur.com/YGKDiRW.png)

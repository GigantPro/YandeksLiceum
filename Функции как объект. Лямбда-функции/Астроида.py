import math
 
 
def dr(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step
 
        
def dist(t):
    return math.hypot(0.7500 - t[0], 0 - t[1])
 
 
coords = [(math.cos(t) * math.cos(t) * math.cos(t),
           math.sin(t) * math.sin(t) * math.sin(t))
          for t in dr(0, 2 * 3.1416, 0.01)]
dists = [round(dist(x), 4) for x in coords]
print(min(dists))
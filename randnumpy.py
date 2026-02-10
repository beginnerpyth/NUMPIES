import numpy as np
ra=np.random.default_rng(seed=1)#if you use seed it reprdouces same integers
print(ra.integers(low=1,high=7,size=(3,2)))
#np.random.seed(seed=1)#reproduce same foat
print(np.random.uniform(low=1,high=22,size=(3,3)))
#if you want to shuffle the elements from array then this is fnction used 
g=np.random.default_rng()
c=np.array([1,2,3,4,5,6,8,0,4,5,6,2,1])

g.shuffle(c)
print(c)
h=np.random.default_rng()
c=h.choice(c)
print(c)
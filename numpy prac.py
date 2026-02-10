import numpy as np
a=np.array([[1,2],[4,8],[9,6]])
b=np.array([[2,3,4],[5,6,7]])
c=np.matmul(a,b)
print(c)
m=np.random.randint(2,4,size=8)
print(m[[0,1,2]])#we can use list indexing here
print(m[1])
k=a.reshape(6,1)
print(k)
d=np.identity(5)
g=np.linalg.det(d)
print(g)
v1=([29,34,556,878,89])
v2=([323,454,56,343,43])
h=np.vstack((v1,v2))
print(h)
i=np.hstack((v1,v2))
print(i)
#miscellaneous data
l=np.genfromtxt('emp.txt',delimiter=',')
l=l.astype('int32')
print(l)
#advanced indexing booleam and advanced indexing
print(l>50)
print(l[l>50])#dvanced indxing
n=np.any(l>50,axis=1)#any means that if anyobe of condition is true then it is true
print(n)
o=np.all(l>50,axis=1)#if anyof this condition is false then everyting io salso false
print(o)
p=((l>50) & (l<100))
print(p)   
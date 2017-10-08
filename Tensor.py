import numpy as np
a1=[0,0,0,0]
a2=[[0],
    [0],
    [0],
    [0]]
sx=[[0,1],[1,0]]
sy=[[0,-1j],[1j,0]]
sz=[[1,0],[0,-1]]
c=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
s=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
h2=[[0,0,0,0],[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]]
hinverse=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
l=[[1,0],[0,1]]
def tensor(a,b):
    for i in range(4):
        for j in range(4):
            c[i][j]=(a[(i)//2][(j)//2]*b[(i)%2][(j)%2])
    return c
def sm(x,y):
    for i in range(4):
        for j in range(4):
            s[i][j]=(x[i][j])+(y[i][j])
    return s

t1=np.copy(tensor(sx,sx))
t2=np.copy(tensor(sy,sy))
t3=np.copy(tensor(sz,sz))
s1=np.copy(sm(t1,t2))
h=np.copy(sm(s1,t3))
for i in range(4):
    for j in range(4):
        h[i][j]=0.25*h[i][j]
           
print(np.linalg.eig(h))
h2=np.linalg.eig(h)
for i in range(4):
    for j in range(4):
        hinverse[i][j]=h2[1][j][i]
t4=np.copy(tensor(sz,l))
for i in range(4):
    for j in range(4):
        a1[j]=hinverse[i][j]
        a2[j]=hinverse[j][i]
    print("value of sz:",end="")
    print(np.dot(np.dot(a1,t4),a2))
        


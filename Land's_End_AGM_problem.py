#!/usr/bin/env python
# coding: utf-8

# ## Supriya Movva
# ### Master's in Business Analytics (Business Data Science)
# ### University of Connecticut
# ### 908-283-3134

# In[ ]:


import numpy as np
import pandas as pd
def agm(x,y):
    if((np.around(x,10)==np.around(y,10)).all()):
        return(np.around(x,10))
    else:
        return(agm((x+y)/2,(x*y)**0.5))


# In[2]:


agm(6,24)


# In[3]:


rnge=range(2,10,1)
lst = list(rnge)
lst


# In[4]:


x=[]
y=[]
agm_lst = []
for i in lst:
    for j in lst:
        x.append(i)
        y.append(j)
        agm_lst.append(agm(i,j))


# In[5]:


from mpl_toolkits import mplot3d
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')

X, Y = np.meshgrid(x, y)
Z=agm(X, Y)

ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.scatter3D(X, Y, Z, c=Z, cmap='hsv')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('AGM');
plt.show()


# In[6]:


X, Y = np.meshgrid(x, y)
Z=agm(X, Y)

fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot_wireframe(X, Y, Z, color='green')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('AGM')

ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='winter', edgecolor='none')

plt.show()


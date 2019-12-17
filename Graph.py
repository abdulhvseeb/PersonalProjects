# importing the required modules 
import matplotlib.pyplot as plt 
import numpy as np 
  
# setting the x - coordinates 
x = np.arange(-2*(np.pi), 2*(np.pi), 0.1) 
# setting the corresponding y - coordinates 
y = np.sin(x) 
z = np.cos(x)
  
# potting the points 
plt.plot(x, y) 
plt.plot(x,z)  
# function to show the plot 
plt.show() 


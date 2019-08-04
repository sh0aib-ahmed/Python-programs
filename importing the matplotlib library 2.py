# importing the matplotlib library 
import matplotlib.pyplot as plt 

# defining the values of X 
x =[0, 1, 2, 3, 4, 5, 6] 

# defining the value of Y 
y =[0, 1, 3, 6, 9, 12, 17] 

# creating the canvas with class 'fig' 
# and it's object 'axes' with '1' row 
# and '2' columns 
fig, axes = plt.subplots(2, 2) 

# plotting graph for 1st element 
axes[0, 0].plot(x, y, 'g--o') 

# plotting graph for 2nd element 
axes[0, 1].plot(y, x, 'm--o') 

# plotting graph for 3rd element 
axes[1, 0].plot(x, y, 'b--o') 

# plotting graph for 4th element 
axes[1, 1].plot(y, x, 'r--o') 

# Gives a clean look to the graphs 
fig.tight_layout()

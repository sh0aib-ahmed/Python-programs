# importing the matplotlib library 
import matplotlib.pyplot as plt 

# defining the values of X 
x =[0, 1, 2, 3, 4, 5, 6] 

# defining the value of Y 
y =[0, 1, 3, 6, 9, 12, 17] 

# creating the canvas with class 'fig' 
# and it's object 'axes' with '1' row 
# and '2' columns 
fig, axes = plt.subplots(1, 2) 

# plotting graph for 1st column 
axes[0].plot(x, y, 'g--o') 

# plotting graph for second column 
axes[1].plot(y, x, 'm--o') 

# Gives a clean look to the graphs 
fig.tight_layout()

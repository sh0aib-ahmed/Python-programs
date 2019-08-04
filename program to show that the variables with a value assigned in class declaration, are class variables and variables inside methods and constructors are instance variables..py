# Class for Computer Science Student 
class CSStudent: 
  
    # Class Variable 
    stream = 'cse'             
  
    # The init method or constructor 
    def __init__(self, roll): 
    
        # Instance Variable     
        self.roll = roll        
   
# Objects of CSStudent class 
a = CSStudent(101) 
b = CSStudent(102) 
   
print(a.stream)  # prints "cse" 
print(b.stream)  # prints "cse" 
print(a.roll)    # prints 101 
   
# Class variables can be accessed using class 
# name also 
print(CSStudent.stream) # prints "cse"     

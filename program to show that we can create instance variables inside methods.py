# Class for Computer Science Student 
class CSStudent: 
      
    # Class Variable 
    stream = 'cse'      
      
    # The init method or constructor 
    def __init__(self, roll): 
          
        # Instance Variable 
        self.roll = roll             
  
    # Adds an instance variable  
    def setAddress(self, address): 
        self.address = address 
      
    # Retrieves instance variable     
    def getAddress(self):     
        return self.address    
  
# Driver Code 
a = CSStudent(101) 
a.setAddress("Noida, UP") 
print(a.getAddress()) 


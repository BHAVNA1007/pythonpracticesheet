'''
ASSIGNMENT 3: Online Shopping System (Hierarchical Inheritance)
Scenario
An e-commerce company sells multiple categories of products.
Create a base class Product.
Common Details
Product ID
Product Name
Price
Derived Classes
Electronics
Brand
Warranty
Clothing
Size
Fabric Type
Grocery
Expiry Date
Weight
Functional Requirements
========== Online Shopping ==========
1. Add Electronics Product
2. Add Clothing Product
3. Add Grocery Product
4. Display Electronics
5. Display Clothing
6. Display Grocery
7. Exit
Sample Input
Choice : 1

Product ID : 501
Product Name : Laptop
Price : 65000

Brand : Dell
Warranty : 2 Years
Sample Output
Electronics Product

Product ID : 501
Product Name : Laptop
Brand : Dell
Warranty : 2 Years
Price : ₹65000
'''

class Product:
   
   def __init__(self, p_id, p_name, p_price):
       
       self.p_id = p_id
       self.p_name = p_name
       self.p_price = p_price
      
   def display(self):
 
       print("Product ID: ", self.p_id)
       print("Product Name: ", self.p_name)
       print("Product Price: ", self.p_price)
 
class Electronics(Product):

   def __init__(self, p_id, p_name, p_price, brand, warranty):
      super().__init__(p_id, p_name, p_price)

      self.brand = brand
      self.warranty = warranty


   def ele_info(self):
       
       print("Brand: ", self.brand)  
       print("Warranty: ", self.warranty)    
    

class Clothing(Product):
   
   def __init__(self, p_id, p_name, p_price, size, fabric_type):
   
          
      super().__init__(p_id, p_name, p_price)

      self.size = size
      self.fabric_type = fabric_type

   def cloth_info(self):
       
       print("Size: ", self.size)  
       print("Fabric Type: ", self.fabric_type)    

class Grocery(Product):

   def __init__(self, p_id, p_name, p_price, exp_date, weight):
     
      super().__init__(p_id, p_name, p_price)

      self.exp_date = exp_date
      self.weight = weight

   def groc_info(self):
       
       print("Expiry Date: ", self.exp_date)  
       print("Weight: ", self.weight)    

e = None
c = None
g = None
while True:

   print("\n========== Online Shopping ==========\n")
   print("1. Add Electronics Product")
   print("2. Add Clothing Product")
   print("3. Add Grocery Product")
   print("4. Display Electronics")
   print("5. Display Clothing")
   print("6. Display Grocery")
   print("7. Exit")

   choice = int(input("\nEnter choice: "))

   match choice:

       case 1:
             print("\nElectronic Product\n") 
             id = int(input("Enter Product Id: "))
             name = input("Enter Name: ")
             price = int(input("Enter Price: "))
             brand = input("Enter Brand: ")
             warr = int(input("Enter Warranty: "))

             e = Electronics(id, name, price, brand, warr)
       
             print("\nElectronic Product added successfully")

       case 2:
             print("\nClothing Product\n") 
             id = int(input("Enter Product Id: "))
             name = input("Enter Name: ")
             price = int(input("Enter Price: "))
             size = input("Enter Size: ")
             fabric = input("Fabric Type: ")

             c = Clothing(id, name, price, size, fabric)
       
             print("\nClothing Product added successfully")


       case 3:
             print("\nGrocery Product\n") 
             id = int(input("Enter Product Id: "))
             name = input("Enter Name: ")
             price = int(input("Enter Price: "))
             exp_d = input("Expiry Date: ")
             weight = float(input("Weight: "))

             g = Grocery(id, name, price, exp_d, weight)
       
             print("\nGrocery Product added successfully")


       
       case 4:
             if e:
                e.display()
                e.ele_info()

             else:
                print("You have no electronic items") 
                

       case 5:
             if c:
                c.display()
                c.cloth_info()

             else:
                print("You have no Clothing items") 
                
       case 6:
             if g:
                g.display()
                g.groc_info()

             else:
                print("You have no Grocery items") 

       case 7:
             print("Exit............")
  
             break


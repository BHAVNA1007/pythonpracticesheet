'''
Question 3: Online Shopping System
Scenario

An e-commerce company wants to calculate the final amount payable by customers after applying discounts.

Requirements

Create a class named Product with:

product_id
product_name
quantity
price_per_item

Initialize the values using a constructor.

Calculations
Total Amount = Quantity × Price Per Item
If Total Amount > ₹5000, Discount = 10%
Otherwise, Discount = 5%
Final Amount = Total Amount − Discount
Sample Input
Enter Product ID : P101
Enter Product Name : Laptop
Enter Quantity : 2
Enter Price Per Item : 35000
Sample Output
------ Shopping Bill ------
Product ID        : P101
Product Name      : Laptop
Quantity          : 2
Price Per Item    : 35000.0
Total Amount      : ₹70000.0
Discount          : ₹7000.0
Final Amount      : ₹63000.0
'''
class Product:

    def __init__(self, product_id, product_name, quantity, price_per_item):

         self.id = product_id
         self.name = product_name
         self.quan = quantity
         self.price = price_per_item
          
         self.total = self.price * self.quan
      
         if  self.total > 5000:
              
              self.dis = self.total * 0.1

         else:
              self.dis = self.total * 0.05

         self.final_amount = self.total + self.dis

def main():
  
    product_id = input("Enter Product ID :")
    product_name = input("Enter Product Name :")
    quantity = int(input("Enter Quantity :"))
    price_per_item = float(input("Enter Price Per Item :"))  
  
    p =  Product(product_id, product_name, quantity, price_per_item)

    print("------ Shopping Bill ------") 
    print("Product ID        :", p.id)
    print("Product Name      :", p.name)
    print("Quantity          :", p.quan)
    print("Price Per Item    :", p.price)
    print("Total Amount      :", p.total)
    print("Discount          :", p.dis)
    print("Final Amount      :", p.final_amount)

main()



             



'''
3.ONLINE SHOPPING SYSTEM

Scenario:

An e-commerce company wants to develop an Online Shopping System. The application should be menu-driven and should demonstrate different types of arguments used in Python functions.

MENU

1. Customer Registration
2. Product Information
3. Generate Invoice
4. Add Multiple Products
5. Display Customer Profile
6. Exit

Requirements

Choice 1 – Customer Registration

* Accept Customer Name, Email, and Mobile Number.
* Pass the values to a function using Positional Arguments.
* Display the registered customer details.

Choice 2 – Product Information

* Accept Product Name, Price, and Category.
* Call the function using Keyword Arguments.
* Display the product details.

Choice 3 – Generate Invoice

* Accept Product Name and Price.
* Tax Percentage should have a default value.
* Use Default Arguments while generating the invoice.
* Display the final amount.

Choice 4 – Add Multiple Products

* Allow the user to enter any number of product prices.
* Pass all prices to a function using Variable Length Arguments (*args).
* Calculate and display the total bill amount.

Choice 5 – Display Customer Profile

* Accept any number of customer details such as Name, City, Email, Mobile, Membership Type, etc.
* Pass the details using Arbitrary Keyword Arguments (**kwargs).
* Display all customer information.

Choice 6 – Exit

Sample Execution

Enter Choice : 1

Enter Name : Ajay
Enter Email : [ajay@gmail.com](mailto:ajay@gmail.com)
Enter Mobile : 9876543210

Customer Registered Successfully

---

Enter Choice : 2

Enter Product Name : Laptop
Enter Price : 55000
Enter Category : Electronics

Product Details Displayed Successfully

---

Enter Choice : 3

Enter Product Name : Laptop
Enter Price : 55000

Invoice Generated Successfully

---

Enter Choice : 4

Enter Number of Products : 4

Enter Price 1 : 100
Enter Price 2 : 200
Enter Price 3 : 300
Enter Price 4 : 400

Total Bill Amount : 1000

---

Enter Choice : 5

Customer Profile Displayed Successfully

---

Enter Choice : 6

Thank You. Program Terminated.

Important Instructions

1. Choice 1 must use Positional Arguments.
2. Choice 2 must use Keyword Arguments.
3. Choice 3 must use Default Arguments.
4. Choice 4 must use Variable Length Arguments (*args).
5. Choice 5 must use Arbitrary Keyword Arguments (**kwargs).
6. Use separate functions for each menu option.
7. Implement the solution using a menu-driven approach.
8. Maintain proper code readability and formatting.

Note:
Marks will be awarded based on the correct usage of the specified argument type in each menu option.
'''
def cust_reg(name, email, mo_n):
    
    print("\nCustomer Registered Successfully")
    print("Name: ", name)
    print("Email: ", email)
    print("Mobile: ", mo_n)

def product_info(**info):

    for k, v in info.items():
        print(k, ":", v)
  
    print("\nProduct Details Displayed Successfully")

def gen_invo(prod_name, price, tax=20):
     f_amount = price + (price * tax /100)
     print("Product Name: ",prod_name)   
     print("Price :", price)
     print("Final Amount :", f_amount)
     
     print("\nInvoice Generated Successfully") 

def mul_product(*prod):
    total = 0
    for i in prod:
         total = total + i
    return total

def cust_profile(**profile):

    for k, v in profile.items():
        print(k, ":", v)

     
def main():
  print("\nMENU ")

  print("1. Customer Registration")
  print("2. Product Information")
  print("3. Generate Invoice")
  print("4. Add Multiple Products")
  print("5. Display Customer Profile")
  print("6. Exit")
 
  while True:
      choice = int(input("\nEnter choice: "))
      match choice:
            case 1:
                 print("\n1. Customer details ") 
                 n = input("\nEnter Name :") 
                 e = input("Enter Email :") 
                 m = int(input("Enter mobile no :"))
                 cust_reg(n, e, m)
   
            case 2:   
                  print("\n2. Product Information")
                  p_n = input("\nEnter Product Name :") 
                  p_p = input("Enter Price :") 
                  p_c = input("Enter Category :")
                  print()
                  product_info(p_name = p_n, price=p_p,category = p_c)
           
            case 3:
                  print("\n3. Generate Invoice")
                  p_name = input("Enter Product Name: ")
                  p_price = int(input("Enter Product Price: "))
                  gen_invo(p_name, p_price)

            case 4:
                  print("4. Add Multiple Products")
                  n = int(input("Enter Number of Products :"))

                  prices = []
                  for i in range(n):
                      p = int(input(f"Enter Price {i+1} : "))
                      prices.append(p)
               
                  total = mul_product(*prices)
                  print("Total Price: ", total)
                  
            case 5: 
                  print("5. Display Customer Profile")  
                  c_n = input("\nEnter Customer Name :") 
                  c_e = input("Enter Customer email :") 
                  c_m = int(input("Enter Customer Mobile No :"))
                  print()
                  cust_profile(c_name = c_n, c_email=c_e, c_mobile = c_m)

            case 6:
                  print("Thank You. Program Terminated.")
                  break
main()
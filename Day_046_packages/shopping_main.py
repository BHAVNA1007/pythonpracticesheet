from online_shopping_package import customer_reg, generate_invo, multiple_product,product_details

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
                 customer_reg.cust_reg(n, e, m)
   
            case 2:   
                  print("\n2. Product Information")
                  p_n = input("\nEnter Product Name :") 
                  p_p = input("Enter Price :") 
                  p_c = input("Enter Category :")
                  print()
                  product_details.product_info(p_name = p_n, price=p_p,category = p_c)
           
            case 3:
                  print("\n3. Generate Invoice")
                  p_name = input("Enter Product Name: ")
                  p_price = int(input("Enter Product Price: "))
                  generate_invo.gen_invo(p_name, p_price)

            case 4:
                  print("4. Add Multiple Products")
                  n = int(input("Enter Number of Products :"))

                  prices = []
                  for i in range(n):
                      p = int(input(f"Enter Price {i+1} : "))
                      prices.append(p)
               
                  total = multiple_product.mul_product(*prices)
                  print("Total Price: ", total)
                  
            case 5: 
                  print("5. Display Customer Profile")  
                  c_n = input("\nEnter Customer Name :") 
                  c_e = input("Enter Customer email :") 
                  c_m = int(input("Enter Customer Mobile No :"))
                  print()
                  customer_reg.cust_reg(c_n, c_e,c_m)

            case 6:
                  print("Thank You. Program Terminated.")
                  break
main()
def gen_invo(prod_name, price, tax=20):
     f_amount = price + (price * tax /100)
     print("Product Name: ",prod_name)   
     print("Price :", price)
     print("Final Amount :", f_amount)
     
     print("\nInvoice Generated Successfully") 
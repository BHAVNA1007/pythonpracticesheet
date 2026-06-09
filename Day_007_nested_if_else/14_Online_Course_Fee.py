'''
14. Online Course Fee System

An online platform offers courses with fixed fees:

* Programming → ₹5000
* Design → ₹4000
* Marketing → ₹3000
  Discount is applied based on user type:
* Student → 20% discount
* Working Professional → 10% discount
* Others → No discount

Write a Python program to calculate final course fee.

Input:
Enter course category: Programming
Enter user type: Student

Output:
Final Course Fee: ₹4000
'''

course = input("Enter course category: ")
user = input("Enter user type: ")

if course == 'Programming' and user == 'Student':
     dis = 5000 * 20/100
     fee = 5000 - dis 
     print(f"Final Course Fee: ₹{fee}")
else:
    if course == 'Programming' and user == 'Working':
        dis = 5000 * 10/100
        fee = 5000 - dis 
        print(f"Final Course Fee: ₹{fee}")
    else:
        if course == 'Design' and user == 'Student':
            dis = 4000 * 20/100
            fee = 4000 - dis 
            print(f"Final Course Fee: ₹{fee}")
        else:
            if course == 'Design' and user == 'Working':
                dis = 4000 * 10/100
                fee = 4000 - dis 
                print(f"Final Course Fee: ₹{fee}")
            else:
                if course == 'Marketing' and user == 'Student':
                    dis = 3000 * 20/100
                    fee = 3000 - dis 
                    print(f"Final Course Fee: ₹{fee}")
                else:
                    if course == 'Marketing' and user == 'Working':
                        dis = 3000 * 10/100
                        fee = 3000 - dis 
                        print(f"Final Course Fee: ₹{fee}")
                    else:
                        print("No discount ") 

                  
            

            
   



     



from com_package import emp_ages, emp_name, sen_emp, longest_name,sec_highest_salary,startswith_vowel,unique_age
def main():
    n = int(input("Enter N: "))

    names = emp_name.emp_names(n)
    ages = emp_ages.emp_age(n)
    
    print("Employee Ages:", ages)

    while True:
         print("\n_____Menu_____")
         print("\n========== EMPLOYEE DATA PROCESSING SYSTEM ==========")
         print("0. names: ")
         print("1.ages: ") 
         print("2. Find Second Highest Employee Age")
         print("3. Count Senior Employees")
         print("4. Remove Duplicate Ages")
         print("5. Count Names Starting with a Vowel")
         print("6. Find Longest Employee Name")
         print("7. Exit")
         print("====================================================")

         choice = int(input("\nEnter your choice: "))

         match choice:
               case 0:
                     print("\nEmployee Names: ")
                     for name in names:
                         print(name,end=" ")    
               case 1:
                     print("\nEmployee Ages: ")
                     for age in ages:
                         print(age,end=" ")        
               
               case 2:
                    print("\nSecond Highest Age:", sec_highest_salary.find_second_highest_age(ages))
 
               case 3:
                    print("\nSenior Employees :",sen_emp.count_senior_employees(ages))
 
               case 4:
                    print("\nUnique Ages :", unique_age.remove_duplicate_ages(ages))

               case 5:
                    print("\nNames Starting with Vowel :",startswith_vowel.count_names_starting_with_vowel(names))
                

               case 6:
                    print("\nLongest Employee Name :", longest_name.longest_name(names))

               case 7:
                    print("\nThank you... program terminated") 
                    break
main()




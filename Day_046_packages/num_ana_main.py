from num_ana_sys_package import factor_of_num, factorial_num,perfect_number,prime_number,reverse_number


def main():
    print("MENU")

    print("1. Check Perfect Number")
    print("2. Check Prime Number")
    print("3. Find Reverse of a Number")
    print("4. Calculate Factorial")
    print("5. Display Factors of a Number")
    print("6. Exit")

    
    
    while True:
       choice = int(input("\nEnter choice: "))
       match choice:
          case 1:
                print("\n1. Check Perfect Number")
                n = int(input("\nEnter Number: "))
                if perfect_number.perfect_num(n):
                   print(n," is a Perfect Number")
                else:  
                   print(n," is a Perfect Number") 
          case 2:
                print("\n2. Check Prime Number")
                n = int(input("\nEnter Number: "))
                print(prime_number.prime_num(n))

          case 3:
                print("\n3. Find Reverse of a Number")
                n = int(input("\nEnter Number: "))
                print("Reverse: ",reverse_number.reverse_num(n)) 

          case 4:
                print("\n4. Calculate Factorial")
                n = int(input("\nEnter Number: "))
                print("Factorial: ",factorial_num.factorial(n))  
            
          case 5:
                print("\n5. Display Factors of a Number")
                n = int(input("\nEnter Number: "))
                print("Factors: ",factor_of_num.factor(n))
          case 6:
                print("\n6. Exit...............")  
                break
main() 
                
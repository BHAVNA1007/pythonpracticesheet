'''
80 Print list items containing all characters of a given word. 

List = ["apple", "plea"], Word = "pal" 

output:
"apple", "plea"

'''

List = input("Enter words for list: ").split()
word = input("Enter a word: ")
print(List)

itms = ''
for i in List:
    
    for j in word:

        found = False
        if j not in i:
            break
        else:
            found = True
    if found:
        itms= itms+i+" "  
print(itms)  
   
      
          
    
       
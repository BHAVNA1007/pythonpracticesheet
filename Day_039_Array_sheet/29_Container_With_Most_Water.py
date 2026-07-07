'''
29 Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
'''

'''
def most_water_container(n, height):

   max_area = 0
   right = n-1
   left = 0

   while left < right:

       width = right - left
       h = min(height[left], height[right])
       area = width * h

       if area > max_area:
          max_area = area

       if height[left] < height[right]:
          left += 1

       else:
          right -= 1
    
   return max_area

def main():

   n = int(input("Enter n: "))
   height = []
   for i in range(n):
       height.append(int(input(f"element {i+1}: ")))
   print(height)
   print(most_water_container(n, height))
main()
   
'''
    





















''' this solution for most water trap only not for contatiner  output is 19'''

'''
def most_water(n, height):
  
    l_max = r_max = total = 0
    l = 0
    r = n-1

    while l < r :
       if height[l] <= height[r]:
          if l_max > height[l]:
              total += l_max - height[l]
          else:
              l_max = height[l] 
          l = l + 1
       else:
          if r_max > height[r]:
              total += r_max - height[r] 
          else:
              r_max = height[r]
          r = r - 1
       
    return total 


def main():
     n = int(input("Enter the size: "))
     height = []

     for i in range(n):

         height.append(int(input(f"element {i+1}: ")))

     print(height)
     print(most_water(n,height))
main()
'''


'''
def m_w_c(n,list):
   
    max_a = 0
    l = 0
    r = n-1

    while l < r:
        
        w = r - l
        h = min(list[l],list[r])

        area = w * h

        if max_a < area:
           max_a = area

        if list[l] < list[r]:
            l += 1
        else:
            r -= 1

    return max_a

def main():
     n = int(input("Enter the size: "))
     list = []

     for i in range(n):

         list.append(int(input(f"element {i+1}: ")))

     print(list)
     print(m_w_c(n,list))
main()
'''




def con(n, list):

    max_area = 0
    l = 0
    r = n-1

    while l < r:
    
         w = r -l
         h = min(list[l], list[r])
         a = w * h
 
         if max_area < a:
            max_area = a
         
         if list[l] < list[r]:
            l += 1
         else:
            r -= 1
       
    return max_area

def main():
     n = int(input("Enter the size: "))
     list = []

     for i in range(n):

         list.append(int(input(f"element {i+1}: ")))

     print(list)
     print(con(n,list))
main()

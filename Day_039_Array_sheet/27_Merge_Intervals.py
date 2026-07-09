'''
27 Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
Example 3:

Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.
'''

row = int(input('Enter row: '))
col = int(input("Enter col: "))

intervals = []

for r in range(row):
  row = [] 
  for c in range(col):
     row.append(int(input(f"ele: [{r}][{c}] ")))
  intervals.append(row)
print(intervals)
  

sorted_interval = sorted(intervals)

#print(sorted_interval)

res = [intervals[0]]

for curr in intervals[1:]:

    last = res[-1]
    
    if curr[0] <= last[1]:
       last[1] = max(last[1], curr[1])

    else:
       res.append(curr)
print(res)
 
     

     
     
   

 
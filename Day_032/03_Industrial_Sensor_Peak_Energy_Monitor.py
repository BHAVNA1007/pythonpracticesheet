'''
03_Industrial_Sensor_Peak_Energy_Monitoring_System

Problem Statement

A factory machine records energy consumption at regular intervals.

A peak is defined as a value greater than or equal to its neighbors.

Tasks:

Find all peak energy values
Compute sum of squares of peak values
Compute average of peak values
Return difference between max peak and min peak
If no peaks, return -1

Test Case 1

Input:
energy = [20, 40, 30, 60, 50]

Output:
Peaks = [40, 60]
Sum of squares = 5200
Average = 50
Difference = 20

Test Case 2

Input:
energy = [10, 20, 15, 25, 20, 30]

Output:
Peaks = [20, 25, 30]
Sum of squares = 1525
Average = 25
Difference = 10

Test Case 3

Input:
energy = [5]

Output:
Peaks = [5]
Sum of squares = 25
Average = 5
Difference = 0
'''
n = int(input('Enter the size: '))
print("plz enter ele...")

energy = []
for i in range(n):
    energy.append(int(input()))
print(energy)

peak = -1

peaks = []
for i in range(n):
    if i == 0:
        if n == 1 or energy[i] >= energy[i+1]:
             peak = i
             peaks.append(energy[peak])
    elif i == n-1:
        if energy[i] >= energy[i-1]:
             peak = i
             peaks.append(energy[peak]) 
    else:
        if energy[i]>=energy[i-1] and energy[i]>=energy[i+1]:
             peak = i
             peaks.append(energy[peak])  
if peak != -1:
    print("Peaks: ",peaks)
else:
    print("no peak found...")
         

sum = 0
for i in peaks:
    sq = i**2
    sum += sq 
print("Sum of squares = ",sum)

sum1 = 0
avg = 0
count = 0
for i in peaks:
    sum1 += i
    count += 1
    agv = sum1 // count
print("Average = ",agv)

max = peaks[0]
for i in range(1,len(peaks)):
    if peaks[i] > max:
       max = peaks[i]

min = peaks[0]
for i in range(1,len(peaks)):
    if peaks[i] < min:
       min = peaks[i]

diff = abs(max) - abs(min)

print("Difference =",diff)

     
               
    
    


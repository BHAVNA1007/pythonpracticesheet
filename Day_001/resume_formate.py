
'''3. Resume Format
Write a program to display:
=== Resume ===
Name       : Alice Johnson
Email      : alice@example.com
Skills     :
  - Java
  - HTML & CSS
  - Problem Solving
Experience : 2 years at XYZ Ltd.'''


print("=== Resume ===")
name,email="Alice Johnson","alice@example.com"
s1,s2,s3="Java", "HTML & CSS", "Problem Solving"
print("Name :",name)
print("Email :",email)
print("Skills :", s1, s2, s3,sep="\n-")
print("Experience : 2 years at XYZ Ltd.")


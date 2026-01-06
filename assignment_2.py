# Write a Python program that does the following:

# Ask the user to enter marks of 5 subjects (one by one).

# Store the marks in a list.

# Calculate and print:

# Total marks

# Average marks

# Highest mark

# Lowest mark

# If the average ≥ 40, print "Pass", else print "Fail".

a = int(input("enter the marks of math :"))
b = int(input("enter the marks of Science :"))
c = int(input("enter the marks of SST :"))
d = int(input("enter the marks of English :"))
e = int(input("enter the marks of PED :"))

list_1=[a,b,c,d,e]

average_marks=(a+b+c+d+e)/5

max_marks=max(list_1)

low_marks=min(list_1)
print(list_1)
print(average_marks)
print(max_marks)
print(low_marks)


if average_marks>= 40:
    print("Pass")
else:print("Fail")




50


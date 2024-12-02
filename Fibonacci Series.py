#This program will use the while loop to print fibonacci series

n = int(input("How many terms? "))
n1, n2 = 0, 1   #On this step we initiate the starting two numbers of our fibonacci series
token = 0
print("Fibonacci sequence:")
while token < n:
       print(n1)
       nth = n1 + n2
       n1 = n2         # To update values
       n2 = nth
       token += 1
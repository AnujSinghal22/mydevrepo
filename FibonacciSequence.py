# Generic Python Program to display the Fibonacci sequence up to n-th level

nterms = int(input("How many terms? "))

# first two terms initilization
n1, n2 = 0, 1
count = 0

# check if the number of terms are valid or not
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, then return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate Fibonacci sequence of numbers up to 8 terms
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values by adding
       # Each subsequent number is the sum of the previous two.
       n1 = n2
       n2 = nth
       count += 1

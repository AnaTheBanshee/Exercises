# Python program to display the Fibonacci sequence

def rec_fibonacci(n):
   if n <= 1:
       return n
   else:
       return(rec_fibonacci(n-1) + rec_fibonacci(n-2))

""" Fibonacci: n1 = 0;
               n2 = 1;
               every number after is considered a sequence of sum between 2 spots before and 1 spot before
               n3= n1 + n2 = 0 + 1 = 1  
               and so  on
"""
print("Please enter number of sequences:\n")
nterms = input()
n_times = int(nterms)  #used so it could be used as integer value for if/else
# If its 0 or negative integer its invalid
if n_times <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(n_times):
       print(rec_fibonacci(i))
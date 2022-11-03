# Write code for algorithm 1 below: Write a program that takes a positive number as an argument and prints the numbers from n to zero.

# We want to define a function that takes a number (n), prints it, and calls itself again with the value of n-1.

def count_down(n):
    if n == 0:
        return 
    else:
        print(n)
        count_down(n-1)

n=4
count_down(n)
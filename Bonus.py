# Write a function that when given two numbers, finds their greatest common divisor. 
#The greatest common divisor of two integers is the largest positive inter that divides both of the intergers. EG 10 and 15: 10 can be divided by 1, 5, and 10; 15 can be divided by 1, 3, 5, and 15. 5 is the greatest common divisor.

def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

print("gcd of 15 and 10:", gcd(15,10))
print("gcd of 46 and 12:", gcd(46,12))
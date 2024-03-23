import math 
n = numbers = [ int(x) for x in input().split(' ') ]

a = n[2]
m = n[1]
n = n[0]

print ((n // a + (n % a > 0)) * (m // a + (m % a > 0)))
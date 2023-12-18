# A simple generator for Fibonacci Numbers 
#user input
n = int(input())

def fib(n):
  # Initialize first two Fibonacci Numbers 
  a = 0
  b = 1
  # One by one yield next Fibonacci Number
  while a < n:
    yield a
    a,b = b,a+b
    
# Iterating over the generator object using for 
# in loop.    
for i in range(n):
  print(i)
    
  
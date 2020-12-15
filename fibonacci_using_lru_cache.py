from functools import lru_cache
# Python fibonacci series display using memorization
@lru_cache()
def fibonacci(n):
    if(type(n)!=int):
        raise TypeError("n must be a positive integer")
    elif(n<1):
        raise ValueError("n must be a positive integer")
    elif(n==1):
        return 1
    elif (n==2):
        return 1
    elif(n>2):
        return fibonacci(n-1) + fibonacci(n-2)
    
for n in range(1,500):
    print(n, ";", fibonacci(n))





#we only need to find the factors up to the sqrt.
#when finding factors of a number, if placed in key:value pairs
#going up to the sqrt will find the first half of the factor pairs
#the factor pairs on the left,the key, the low factors are going to include the prime numbers
#the factors pairs on the right, the value, are going to be divisble by something
#i.e. factors of 16
#{1, 16}
#{2, 8}
#{4, 4}
#{8, 2}
#{16, 1}
#only the numbers under 4, the sqrt of 16, are prime

#i.e.
#96
#{1, 96}
#{2, 48}
#{3, 32}
#{4, 24}
#{6, 16}
#{8, 12}
#{12, 8}

import math
import time

TARGET = 600851475143
listOfPrimes = [3]

mySqrt = math.sqrt(TARGET)

def isPrime(number, listOfPrimes):
    mySqrt = math.sqrt(number)    
    cost = 0
    
    if (number < 3):
        return True
    
    for prime in listOfPrimes:
        
        if prime > mySqrt:
            listOfPrimes.append(number)
            return True
        cost += 1
        
        if number % prime == 0:
            return False
    listOfPrimes.append(number)
    return True

def isFactor (x, y):  
    if (y % x) == 0:
        
        return True
    
    return False


for i in range(1, int(mySqrt), 2):
    
    if (i - 1) % 1000000 == 0:
        print("testing " + str(i))
    
    if isFactor(i, TARGET):
        if (isPrime(i, listOfPrimes)):
            print(i)
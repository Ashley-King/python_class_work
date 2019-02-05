'''
    Assignment: 5 - Functions
    Author: Ashley King
    Date: 2019-02-05
    Description: Creating and calling functions
'''
# PART 1 - code to test for prime numbers

'''
Algorithm, Part 1
1. loop through a list of integers
2. for each integer (num), modulo it by every number between 2 and num - 1
3. if the remainder is 0, print that the number is prime
4. else, print that the number is prime
'''
candidatePrimes = [10, 12, 15, 17, 31, 89, 97, 7919, 982_451_653]
# this takes a really long time to run
for num in candidatePrimes:
    for i in range(2,num):
        if num % i == 0:
            print(str(num) + " is not prime")
            break
    else:
        print(str(num) + " is prime")
        continue

''' -----------------OUTPUT PART 1 ------------------
10 is not prime
12 is not prime
15 is not prime
17 is prime
31 is prime
89 is prime
97 is prime
7919 is prime
982451653 is prime
-----------------------------------------------------'''

# PART 2 - function to test for prime numbers
'''
Algorithm - Part 2
1. define function that accepts an integer, p
2. for each number in range 2 to p - 1, modulo p by the number
3. if the remainder is 0, return 0 (the number is not prime)
4. if the remainder is not 0, return the number (the number is prime)
'''

def isPrime(p):
    for i in range(2, p):
        if p % i == 0:
            return 0
    return p

''' -----------------OUTPUT PART 2 ------------------
no output unless called

-----------------------------------------------------'''

# PART 3 - use function to find first 3 prime numbers after 1000
'''
Algorithm - Part 3
1. set counter to 0
2. loop through a range of numbers between 1000 and 1500
3. set answer variable = to return value of isPrime(number in range)
4. if answer variable == 0, continue loop
5. if answer variable != 0, check to see if counter is >= 3
6. if counter < 3, increment counter and print answer (prime number)
7. if counter >= 3, break out of loop without printing (you've already found 
   3 primes)
'''
counter = 0
for i in range(1000, 1501):
    ans = isPrime(i)
    if ans != 0:
       if counter >= 3:
           break
       print(str(ans))
       counter += 1

''' -----------------OUTPUT PART 3 ------------------
1009
1013
1019
-----------------------------------------------------'''
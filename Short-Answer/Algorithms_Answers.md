#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The runtime is O(1+n*1) == O(n) a = 0 # O(1) while (a < n * n * n): # O(n) a = a + n * n # O(1)
The control variable a increases everytime with n^2. But the while loop checks if the a < n^3. Basically it checks n^2 < n^3 which gives a complexity of O(n). 

Ans. I would say that this is a runtime of O(n). My reasoning is that while 'a' is less than 3n (O(n)), 'a' will be 'a' + 2N (O(n)). As long as 'a' is less than 3n the loop will run, meaning that this is O(n).

b) O(1+n*(1+log(n)*(1+1))) == O(nlog(n)) sum = 0 
# O(1) for i in range(n): 
# O(n) j = 1 
# O(1) while j < n: 
# O(log n) j *= 2 
# O(1) sum += 1 # O(1)
#while j < n has O(log n) complexity because the control variable j is alway multiplied by 2

Ans. I think that this runtime is O(nlogn) because in a range of n, while 'j' is less than 'n' it will multiply by 2 until it reaches the point where it is larger than n, anytime I see something multiplying by 2 I think logn because we are closing that gap faster and faster, like Binary sort. So, logn times n times another n. O(2nlogn) take out the constant and O(nlogn).

c) O(1+1+n) == O(n) def bunnyEars(bunnies): if bunnies == 0: # O(1) return 0 # O(1)
return 2 + bunnyEars(bunnies-1) # O(n)
The function will recurse n times until n=0.

Ans. My answer, O(n). The first two lines of the function are O(1) because it's saying if this condition, return this constant (Base Case). Else, 2 + function(n - 1) (Recursive Case). Since the only option is to recurse if bunnies isn't 0, n would grow linearly.

## Exercise II
# Base case:
Start on the ground floor
Get the middle floor between the start point and the top floor (n)
run until floor f:
# drop the egg
# if the egg breaks:
    # move to the middle point between current location and the ground
# otherwise:
    # move to the middle point between current location and the top floor
return floor f
floor f is the highest floor where the egg doesn't break

This is the best approach to solve this and it  is similar to a binary search, so the runtime complexity is O(log n)

However, another way of solving this is first, if I go floor by floor until I find the floor where I can drop eggs from (for i in n, egg + 1) n would grow at a linear rate. This is O(n).

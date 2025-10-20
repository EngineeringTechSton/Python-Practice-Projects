
import math
def sqr_root(num):
    guess=int(input("Guess any number that can be its sqrt: "))
    if guess==math.sqrt(num):
        print("Yes! it is the sqrt of ",num)
    else:
        while guess != math.sqrt(num):
           guess=(guess+(num/guess))/2
        print(f"Exact sqrt of {num} is {round(guess)}")   
    return 0
n=int(input("Enter a number whose sqrt you want to find: ")) 
sqr_root(n)


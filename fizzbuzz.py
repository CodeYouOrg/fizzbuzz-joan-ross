# Write a Python program that prints the numbers from 1 to 100. 
# If the number is dividable by 3 print Fizz, 
# if the number is dividable by 5 print Buzz instead of the number. 
# If the number is dividable by 3 and 5 print FizzBuzz instead of the number.

def fb_challenge(s):
    for number in range(1,101):
        if number % 3 == 0 :
            return ('Fizz')
        elif number % 5 == 0 :
            return('Buzz')
        elif number % 3 == 0 and number % 5 == 0:
            return('FizzBuzz')
            print(s)

    return s


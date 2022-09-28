#"Fizz buzz" is a word game we will use to teach the robots about division. Let's learn computers.
#You should write a function that will receive a positive integer and return:
#"Fizz Buzz" if the number is divisible by 3 and by 5;
#"Fizz" if the number is divisible by 3;
#"Buzz" if the number is divisible by 5;
#The number as a string for other cases.
#Input: A number as an integer.
#Output: The answer as a string.
#Example:
#assert checkio(15) == "Fizz Buzz"
#assert checkio(6) == "Fizz"
#assert checkio(10) == "Buzz"
#assert checkio(7) == "7"
#1
#2
#3
#4
#How it is used: Here you can learn how to write the simplest function and work with if-else statements.

#Precondition: 0 < number ≤ 1000

def checkio(number: int) -> str:
    if not number % 15:
        return "Fizz Buzz"
    elif not number % 3:
        return "Fizz"
    elif not number % 5:
        return "Buzz"
    else: 
        return str(number)



print("Example:")
print(checkio(15))

assert checkio(15) == "Fizz Buzz"
assert checkio(6) == "Fizz"
assert checkio(10) == "Buzz"
assert checkio(7) == "7"

print("The mission is done! Click 'Check Solution' to earn rewards!")

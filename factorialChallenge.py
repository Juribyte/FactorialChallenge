#FactorialChallenge
print('Find the Factorial of: ')
number = int(input())
factorial = 1
if number == 0 or number == 1:
    print('The factorial of ' + str(number) + ' is ' + str(factorial))
else:
    for i in range(number):
        factorial = factorial * (i + 1)
print('The factorial of ' + str(number) + ' is ' + str(factorial))

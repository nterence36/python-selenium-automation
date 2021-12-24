# sum of digits from 1 to input number n entered by user.
# example n = 5, Result = 1+2+3+4+5 =15

n = int(input('Enter a number: '))
result = 0
for i in range(1, n + 1):
    result += i

print(f'The sum of digits of {n} is {result}')

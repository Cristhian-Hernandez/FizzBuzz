# This program will print a list of 100 numbers where:
# Multiples of 3 will print 'Fizz', multiples of 5 print 'Buzz'
# And multiples of both, 3 and 5, will print 'FizzBuzz'
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)
        
# I used '101' because otherwise it wouldn't include the number '100'
print(",\n".join(fizzbuzz(n) for n in range(1, 101)))
import itertools

def isDivisibleBy(num, divisor):
    return num % divisor == 0

def isEven(num):
    return isDivisibleBy(num, 2)

def isOdd(num):
    return not isDivisibleBy(num, 2)

def fibonacciGenerator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def isPrime(num):
    if num <= 3:
        return num >= 2
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, int(num ** 0.5) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True

def primeGenerator():
    i = 3
    yield 2
    while True:
        if isPrime(i):
            yield i
        i += 2

def triangularGenerator():
    num, i = 1, 2
    while True:
        yield num
        num += i
        i += 1

def factorize(num):
    factorSet = set()

    for i in xrange(1, int((num ** 0.5)) + 1):
        if num % i == 0:
            factorSet.add(i)
            factorSet.add(num // i)
            
    return factorSet

def isPalindrome(sequence):
    return sequence == sequence[::-1]

def nthItem(sequence, n):
    return next(itertools.islice(sequence, n - 1, None))

def collatz(num):
    count = 1
    while num != 1:
        count += 1
        if num % 2 == 0:
            num /= 2
        else:
            num = 3 * num + 1

    return count

def digitSum(num):
    return sum([int(x) for x in str(num)])

def factorial(num):
    return reduce(lambda x, y: x * y,
                  xrange(1, num + 1))

def combination(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

def sumOfProperDivisors(num):
    return sum(factorize(num)) - num

def abundantGenerator():
    num = 12
    while True:
        if sumOfProperDivisors(num) > num:
            yield num

        num += 1

def digitPow(num, power):
    return sum([int(x)**power for x in str(num)])

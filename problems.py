import itertools

def pe001():
    from tools import isDivisibleBy

    return sum(filter(lambda x: isDivisibleBy(x, 3) or isDivisibleBy(x, 5),
                      xrange(0, 1000)))
               
def pe002():
    from tools import fibonacciGenerator, isEven

    return sum(filter(isEven,
                      itertools.takewhile(lambda x: x < 4000000,
                                          fibonacciGenerator())))

def pe003():
    from tools import isPrime, factorize

    return max(filter(isPrime,
                      factorize(600851475143)))

def pe004():
    from tools import isPalindrome

    pmax = 0
    for i in xrange(100, 1000):
        for j in xrange(i, 1000):
            p = i * j
            if isPalindrome(str(p)) and p > pmax:
                pmax = p
                
    return pmax

def pe005():
    from tools import isDivisibleBy

    num = 2520
    while not reduce(lambda x, y: isDivisibleBy(num, y) and x,
                     xrange(11, 21),
                     True):
        num += 2520

    return num

def pe006():
    sum_of_squares = reduce(lambda x, y: x + y**2,
                            xrange(1, 101),
                            0)
    
    square_of_sum = sum(xrange(1, 101))**2

    return square_of_sum - sum_of_squares

def pe007():
    from tools import primeGenerator, nthItem
    
    return nthItem(primeGenerator(), 10001)

def pe008():
    sequence = str(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)

    product, largestProduct = 0, 0
    for i in xrange(0, len(sequence) - 13):
        product = reduce(lambda x, y: int(x) * int(y),
                         sequence[i: i + 13])
        if product > largestProduct:
            largestProduct = product

    return largestProduct

def pe009():
    for i in xrange(0, 334):
        for j in xrange(i + 1, 667):
            for k in xrange(j + 1, 1001):
                if i**2 + j**2 == k**2 and i + k + j == 1000:
                    return i*j*k

def pe010():
    from tools import primeGenerator

    return sum(itertools.takewhile(lambda x: x < 2000000,
                                   primeGenerator()))

# Find the largest product of four consecutive numbers in a 20x20 matrix
def pe011():
    matrix = list()
    with open('pe011data.txt', 'rb') as infile:
        for line in infile:
            matrix.append([int(x) for x in line.split()])

    maxProduct = 0
    for i in xrange(0, len(matrix)):
        for j in xrange(0, len(matrix[i])):

            try:
                column = matrix[i][j] * matrix[i+1][j] * matrix[i+2][j] * matrix[i+3][j]
            except IndexError:
                column = 0

            try:
                row = matrix[i][j] * matrix[i][j+1] * matrix[i][j+2] * matrix[i][j+3]
            except IndexError:
                row = 0

            try:
                diagonalRight = matrix[i][j] * matrix[i+1][j+1] * matrix[i+2][j+2] * matrix[i+3][j+3]
            except IndexError:
                diagonalRight = 0

            try:
                diagonalLeft = matrix[i][j] * matrix[i+1][j-1] * matrix[i+2][j-2] * matrix[i+3][j-3]
            except:
                diagonalLeft = 0
        
            maxProduct = max(column, row, diagonalRight, diagonalLeft, maxProduct)

    return maxProduct

# Find the smallest triangular number with over 500 divisors
def pe012():
    from tools import triangularGenerator, factorize

    gen = triangularGenerator()
    while True:
        num = next(gen)
        if len(factorize(num)) > 500:
            return num

# Find the sum of one-hundred 50 digit numebrs
def pe013():
    numList = list()
    with open('pe013data.txt', 'rb') as infile:
        numList = [int(line) for line in infile]

    return sum(numList)

# Find the number under one-million with the longest collatz-chain
def pe014():
    from tools import collatz
    
    longestChain = [0, 0]
    for i in xrange(1, 1000000, 2):
        chain = collatz(i)
        if chain > longestChain[0]:
            longestChain[0] = chain
            longestChain[1] = i

    return longestChain[1]

# Find the number of paths from the top-left to the bottom-right of a
# 20x20 grid
def pe015():
    from tools import combination

    return combination(40, 20)

# Find the sum of the digits of the number 2^1000
def pe016():
    from tools import digitSum

    return digitSum(2**1000)

# Find the number of letters needed to spell all of the numbers from 1 to 1000 
def pe017():

    # Letter counts of the numbers 1 -> 20, 30, 40 ... 90
    oneToNine = [3, 3, 5, 4, 4, 3, 5, 5, 4]
    tenToNineteen = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
    twentyToNinety = [6, 6, 5, 5, 5, 7, 6, 6]

    # Gets us the letter count from 1 -> 99
    letters = sum(oneToNine)
    letters += sum(tenToNineteen)
    letters += sum(oneToNine) * len(twentyToNinety) + sum(twentyToNinety) * (len(oneToNine) + 1)

    # Gets us the letter count from 100 -> 999
    letters += sum([(x + len('hundred')) * 100 for x in oneToNine]) + len('and') * 891 + letters * 9

    # Add in 1000
    letters += len('onethousand')

    return letters
    
# Find the maximum possible sum of adjacent vertical numbers in a triangle
def pe018():
    triangle = list()
    with open('pe018data.txt', 'rb') as infile:
        for line in infile:
            triangle.append([int(x) for x in line.split()])

    for i in xrange(len(triangle) - 1, 0, -1):
        for j in xrange(0, len(triangle[i]) - 1):
            triangle[i-1][j] = max(triangle[i-1][j] + triangle[i][j],
                                   triangle[i-1][j] + triangle[i][j+1])

    return triangle[0][0]

# Find the number of times between 1901 and 2000 (inclusive) where Sunday
# occurred on the first of the month
def pe019():
    import calendar
    
    count = 0
    for year in xrange(1901, 2001):
        for month in xrange(1, 13):
            if calendar.weekday(year, month, 1) == 6:
                count += 1

    return count

# Find the digit-sum of 100!
def pe020():
    from tools import factorial, digitSum

    return digitSum(factorial(100))

# Find the sum of all amicable pairs below 10000
def pe021():
    from tools import sumOfProperDivisors

    amicableNumSet = set()
    for a in xrange(1, 10000):
        if a not in amicableNumSet:
            b = sumOfProperDivisors(a)
            if a != b and sumOfProperDivisors(b) == a:
                amicableNumSet.add(a)
                amicableNumSet.add(b)

    return sum(amicableNumSet)

# Find the sum of the Alphabetical Values of the names in the provided datafile
def pe022():
    import string

    with open('pe022data.txt', 'rb') as infile:
        names = sorted([x.strip('"') for x in infile.read().split(',')])

        charValue = {c:v for v,c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ", start = 1)}

        totalScore, count = 0, 1
        for name in names:
            totalScore += sum([charValue[x] for x in string.upper(name)]) * count
            count += 1

    return totalScore

# Find the sum of all positive numbers that cannot be represented as the sum
# of two abundant numbers. (Upper bound adjusted from original problem)
def pe023():
    from tools import abundantGenerator

    abundants = list(itertools.takewhile(lambda x: x < 20162,
                                         abundantGenerator()))

    sumOfTwoAbundants = set()
    for i in abundants:
        for j in abundants:
            sumOfTwoAbundants.add(i+j)

    return sum([x for x in xrange(1, 20162) if x not in sumOfTwoAbundants])

# DONE
def pe024():
    pass

# DONE
def pe025():
    pass

def pe026():
    pass

def pe027():
    from tools import isPrime
    
    # a, b, n
    longestChain = [0, 0, 0]
    
    for a in xrange(-1000, 1001):
        for b in xrange(-1000, 1001):
            n = 0
            while isPrime(n**2 + a*n + b):
                n += 1
            if n > longestChain[2]:
                longestChain[0] = a
                longestChain[1] = b
                longestChain[2] = n

    return longestChain[0] * longestChain[1]

# Find the sum of the diagonals of a 1001x1001 spiral matrix starting at 1
def pe028():
    totalSum, num, skip, count = 1, 3, 2, 0
    while num < 1001**2 + 1:
        totalSum += num
        count += 1
        if count == 4:
            skip += 2
            count = 0
        num += skip

    return totalSum

# Find the numeber of distinct numbers a^b for the range(2, 101)
def pe029():
    distinctSet = set()
    for a in xrange(2, 101):
        for b in xrange(2, 101):
            distinctSet.add(a**b)

    return len(distinctSet)

def pe030():
    from tools import digitPow
    
    return sum([x for x in xrange(10, 9**5 * 6) if x == digitPow(x, 5)])

def pe031():
    pass

def pe032():
    pass

def pe033():
    pass

def pe041():
    pass
    
def pe048():
    return reduce(lambda x, y: x + y**y,
                  xrange(1, 1001))

# Find the maximum possible sum of adjacent vertical numbers in a triangle
def pe067():
    triangle = list()
    with open('pe067data.txt', 'rb') as infile:
        for line in infile:
            triangle.append([int(x) for x in line.split()])

    for i in xrange(len(triangle) - 1, 0, -1):
        for j in xrange(0, len(triangle[i]) - 1):
            triangle[i-1][j] = max(triangle[i-1][j] + triangle[i][j],
                                   triangle[i-1][j] + triangle[i][j+1])

    return triangle[0][0]

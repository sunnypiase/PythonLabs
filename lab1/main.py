import math


def isPrime(number: int) -> bool:
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def getPrimeNumbers(a: int, b: int):
    return [i for i in range(a, b, 1 if a < b else -1) if isPrime(i)]


def fib(k):
    if k < 1:
        return []
    if k == 1:
        return [0]
    if k >= 2:
        result = [0, 1]
        for i in range(1, k - 1):
            result.append(result[i] + result[i - 1])
        return result


def run_tests():
    print("Testing isPrime:")
    print("isPrime(0) =", isPrime(0))
    print("isPrime(1) =", isPrime(1))
    print("isPrime(2) =", isPrime(2))
    print("isPrime(17) =", isPrime(17))
    print("isPrime(100) =", isPrime(100))

    print("\nTesting getPrimeNumbers:")
    print("getPrimeNumbers(10, 1) =", getPrimeNumbers(10, 1))
    print("getPrimeNumbers(-10, 100) =", getPrimeNumbers(-10, 100))

    print("\nTesting fib:")
    print("fib(-1) =", fib(-1))
    print("fib(0) =", fib(0))
    print("fib(1) =", fib(1))
    print("fib(10) =", fib(10))


if __name__ == '__main__':
    run_tests()

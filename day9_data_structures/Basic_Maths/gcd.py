# T(n) = O(min(n1,n2)) ==> Linear Complexity
def gcd(a: int, b: int) -> int:
    for i in range(min(a, b), -1, -1):
        if a % i == 0 and b % i == 0:
            finalAns = i
            return finalAns


# Euclidean Algorithm
def euclideanAlgorithmGCD(a: int, b: int) -> int:
    # gcd(a,b) = gcd(a-b, b) where a >= b ==> T(n) = min(a,b)

    # More Optimised Euclidean Algorithm ==> gcd(a,b) = gcd(a%b, b) where a > b
    """
    T(n) = O(log(min(a,b))) ==> Base would be variable dependent on smaller number in each iteration
    """
    if min(a, b) == 0:
        return max(a, b)
    return euclideanAlgorithmGCD(max(a, b) % min(a, b), min(a, b))


if __name__ == "__main__":
    firstNum, secondNum = int(input()), int(input())
    # print(gcd(firstNum, secondNum))
    print(euclideanAlgorithmGCD(firstNum, secondNum))

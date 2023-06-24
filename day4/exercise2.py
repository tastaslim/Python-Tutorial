def highest_even(arr):
    maxi = 0
    for element in arr:
        if element % 2 == 0:
            maxi = max(maxi, element)
    return maxi


def main():
    ans = highest_even([1, 2, 30, 23, 65, 42, 5])
    print(ans)


main()

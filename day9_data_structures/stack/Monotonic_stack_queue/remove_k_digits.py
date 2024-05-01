from queue import LifoQueue


def removeKDigits(num: str, k: int) -> str:
    if len(num) == k:
        return "0"
    ans = ""
    stack = LifoQueue()
    for element in num:
        while not stack.empty() and stack.queue[-1] > element and k > 0:
            stack.get()
            k -= 1
        stack.put(element)

    # If string is already sorted
    while not stack.empty():
        top = stack.get()
        if k <= 0:
            ans += top
        k -= 1

    j = len(ans) - 1
    # If there are tailing 0s
    while ans[j] == '0' and j > 0:
        j -= 1

    return "".join(list(reversed(ans[:j + 1])))


if __name__ == "__main__":
    print(removeKDigits("1432219", 3))

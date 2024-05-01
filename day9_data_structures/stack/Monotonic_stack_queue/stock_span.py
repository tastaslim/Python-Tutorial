"""Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for
the current day.

The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going
backward) for which the stock price was less than or equal to the price of that day.

For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today is 2,
then the span of today is 4 because starting from today, the price of the stock was less than or equal 2 for 4
consecutive days. Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock
today is 8, then the span of today is 3 because starting from today, the price of the stock was less than or equal 8
for 3 consecutive days."""

from queue import LifoQueue


def findStockSpans(prices: list[int]) -> list[int]:
    ans = []
    # for i in range(len(prices)):
    #     count = 1
    #     for j in range(i - 1, -1, -1):
    #         if prices[j] < prices[i]:
    #             count += 1
    #         else:
    #             break
    #     ans.append(count)

    stack = LifoQueue()
    for i in range(len(prices)):
        count = 1
        while not stack.empty() and stack.queue[-1] < prices[i]:
            count += 1
            stack.get()
        ans.append(count)
        stack.put(prices[i])
    return ans


if __name__ == "__main__":
    print(findStockSpans([100, 80, 60, 70, 60, 75, 85]))

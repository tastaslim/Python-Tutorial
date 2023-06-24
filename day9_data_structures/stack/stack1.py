class Stack2:
    arr = []
    index = 0

    def push(self, data) -> list:
        self.arr.append(data)
        self.index += 1
        return self.arr

    def pop(self) -> None:
        if not self.is_empty():
            self.arr.pop()
            self.index -= 1

    def peek(self):
        return self.arr[self.index - 1]

    def is_empty(self) -> bool:
        return self.index == 0

    def print_stack(self) -> None:
        for element in self.arr:
            print(element, end=" ")

    def size(self) -> int:
        return self.index


"""
Complexities of Stack Operations#
Let’s look at the time complexity of each stack operation.
----------------------------------------
Operation	     |   Time Complexity
----------------------------------------
push(element)	        O(1) (Can be O(n) when list is full and it has to double it's space and move all elements to new list)
pop()	                O(1)
peek()	                O(1)
is_empty()	            O(1)
size()	                O(1)
"""

class MinStack:

    def __init__(self):
        self._stack = []
        self._min = None

    # @param x, an integer
    # @return an integer
    def push(self, x):
        if self._min is None:
            self._min = x
        self._stack.append(x - self._min)
        # self._min = min(x, self._min)
        if x < self._min:
            self._min = x
        return x

    # @return nothing
    def pop(self):
        if not self._stack:
            return
        temp = self._stack.pop()
        if not self._stack:
            self._min = None
        elif temp < 0:
            self._min -= temp

    # @return an integer
    def top(self):
        temp = self._stack[-1]
        if temp > 0:
            return temp + self._min
        else:
            return self._min

    # @return an integer
    def getMin(self):
        return self._min


class MinStack1:

    def __init__(self):
        self._stack = []
        self._minStack = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        if not self._minStack or x <= self._minStack[-1]:
            self._minStack.append(x)
        self._stack.append(x)
        return x

    # @return nothing
    def pop(self):
        if self._stack:
            temp = self._stack.pop()
            if not self._stack:
                self._minStack = []
            elif temp == self._minStack[-1]:
                self._minStack.pop()

    # @return an integer
    def top(self):
        return self._stack[-1]

    # @return an integer
    def getMin(self):
        return self._minStack[-1]

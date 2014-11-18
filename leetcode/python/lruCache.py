class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self._cache = dict()
        self._keyMap = dict()
        self._root = root = []
        root[:] = [root, root, None]
        self._capacity = capacity

    def _setItem(self, key, value):
        root = self._root
        last = root[0]
        last[1] = root[0] = self._keyMap[key] = [last, root, key]
        self._cache[key] = value

    def _delItem(self, key):
        prev, suc, _ = self._keyMap.pop(key)
        prev[1], suc[0] = suc, prev
        del self._cache[key]

    # @return an integer
    def get(self, key):
        value = -1
        if key in self._cache:
            value = self._cache[key]
            self.set(key, value)
        return value

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self._cache:
            self._delItem(key)
        elif len(self._cache) == self._capacity:
            self._delItem(self._root[1][2])
        self._setItem(key, value)

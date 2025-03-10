class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # stores key-value pairs
        self.freq = {}  # stores access frequencies

    def get(self, key):
        if key in self.cache:
            self.freq[key] = self.freq.get(key, 0) + 1
            print("Cached element found with key: {}".format(key))
            return self.cache[key]
        return None

    def exists(self, key):
        if key in self.cache:
            print("Cached element found with key: {}".format(key))
            return True
        return None

    def put(self, key, value):
        if self.capacity <= 0:
            return

        # If key exists, update value and frequency
        if key in self.cache:
            self.cache[key] = value
            self.freq[key] = self.freq.get(key, 0) + 1
            return

        # If cache is full, remove least frequently used item
        if len(self.cache) >= self.capacity:
            # Find key with minimum frequency
            min_freq = float('inf')
            lfu_key = None

            for k, f in self.freq.items():
                if f < min_freq:
                    min_freq = f
                    lfu_key = k

            if lfu_key:
                del self.cache[lfu_key]
                del self.freq[lfu_key]

        # Add new item
        self.cache[key] = value
        self.freq[key] = 1

    def clear(self):
        self.cache = {}
        self.freq = {}

    def __str__(self):
        return str(self.cache)

class HashTable:

    def __init__(self):
        self.Max = 100
        self.arr = [[] for i in range(self.Max)]
    
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)

        return h % self.Max
    
    def add(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def get (self, key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val) 
                found = True
                return
        if not found:    
               self.arr[h].append((key, val))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]
        self.arr[h] = None

    
if __name__ == '__main__':
    t = HashTable()

    print(t.get_hash('ac'))
    print(t.get_hash('ca'))
    t['ac'] = 78

    t['ca'] = 200
    print(['ac'])
    print(t['ac'])
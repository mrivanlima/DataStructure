class MaxHeap:
    def __init__(self):
        self.H = [None]
        
    def size(self):
        return len(self.H)-1
    
    def __repr__(self):
        return str(self.H[1:])
        
    def satisfies_assertions(self):
        for i in range(2, len(self.H)):
            assert self.H[i] <= self.H[i//2],  f'Maxheap property fails at position {i//2}, parent elt: {self.H[i//2]}, child elt: {self.H[i]}'
    
    def max_element(self):
        return self.H[1]
    
    def bubble_up(self, index):
        # your code here
        if index == 1:
            return
        parent_index = index // 2

        if(self.H[parent_index] < self.H[index]):
            self.H[parent_index], self.H[index] = self.H[index], self.H[parent_index]
            self.bubble_up(parent_index)
        
        
            
    
    def bubble_down(self, index):
        
        size = len(self.H) -1
        # your code here
        left_child_index = index * 2
        right_child_index = index * 2 + 1
        index_to_pass = None

        lchild_value = self.H[left_child_index] if left_child_index < len(self.H) else float('-inf')
        # set up the value of right child to the element at that index if valid, or else make it +Infinity
        rchild_value = self.H[right_child_index] if right_child_index < len(self.H) else float('-inf')
  
        if (lchild_value > rchild_value and self.H[index] < lchild_value and lchild_value != float('-inf')):
            self.H[index], self.H[left_child_index] = self.H[left_child_index], self.H[index] 
            index_to_pass = left_child_index
        elif(rchild_value > lchild_value and self.H[index] < rchild_value and rchild_value != float('-inf')):
            self.H[index], self.H[right_child_index] = self.H[right_child_index], self.H[index]
            index_to_pass = right_child_index
        else:
            return
        self.bubble_down(index_to_pass)

            
        
        
        
    
    # Function: insert
    # Insert elt into minheap
    # Use bubble_up/bubble_down function
    def insert(self, elt):
        # your code here
        self.H.append(elt)
        size = len(self.H) - 1
        self.bubble_up(size)
        
        
    # Function: delete_max
    # delete the largest element in the heap. Use bubble_up/bubble_down
    def delete_max(self):
        # your code here
        if(len(self.H) == 1):
            return
        size = len(self.H) - 1
        self.H[size], self.H[1] = self.H[1], self.H[size]
        self.H.remove(self.H[-1])
        self.bubble_down(1)


h = MaxHeap()
print('Inserting: 5, 2, 4, -1 and 7 in that order.')
h.insert(5)
print(f'\t Heap = {h}')
assert(h.max_element() == 5)

h.insert(2)
print(f'\t Heap = {h}')
assert(h.max_element() == 5)

h.insert(4)
print(f'\t Heap = {h}')
assert(h.max_element() == 5)

h.insert(-1)
print(f'\t Heap = {h}')
assert(h.max_element() == 5)

h.insert(7)
print(f'\t Heap = {h}')
assert(h.max_element() == 7)

h.satisfies_assertions()

print('Deleting maximum element')
h.delete_max()
print(f'\t Heap = {h}')
assert(h.max_element() == 5)
h.delete_max()
print(f'\t Heap = {h}')
assert(h.max_element() == 4)
h.delete_max()
print(f'\t Heap = {h}')
assert(h.max_element() == 2)
h.delete_max()
print(f'\t Heap = {h}')
assert(h.max_element() == -1)
# Test delete_max on heap of size 1, should result in empty heap.
h.delete_max()
print(f'\t Heap = {h}')
print('All tests passed: 5 points!')

class MinHeap:
    def __init__(self):
        self.H = [None]
 
    def size(self):
        return len(self.H)-1
    
    def __repr__(self):
        return str(self.H[1:])
        
    def satisfies_assertions(self):
        for i in range(2, len(self.H)):
            assert self.H[i] >= self.H[i//2],  f'Min heap property fails at position {i//2}, parent elt: {self.H[i//2]}, child elt: {self.H[i]}'
    
    def min_element(self):
        return self.H[1]

    ## bubble_up function at index
    ## WARNING: this function has been cut and paste for the next problem as well 
    def bubble_up(self, index):
        assert index >= 1
        if index == 1: 
            return 
        parent_index = index // 2
        if self.H[parent_index] < self.H[index]:
            return 
        else:
            self.H[parent_index], self.H[index] = self.H[index], self.H[parent_index]
            self.bubble_up(parent_index)
    
    ## bubble_down function at index
    ## WARNING: this function has been cut and paste for the next problem as well 
    def bubble_down(self, index):
        assert index >= 1 and index < len(self.H)
        lchild_index = 2 * index
        rchild_index = 2 * index + 1
        # set up the value of left child to the element at that index if valid, or else make it +Infinity
        lchild_value = self.H[lchild_index] if lchild_index < len(self.H) else float('inf')
        # set up the value of right child to the element at that index if valid, or else make it +Infinity
        rchild_value = self.H[rchild_index] if rchild_index < len(self.H) else float('inf')
        # If the value at the index is lessthan or equal to the minimum of two children, then nothing else to do
        if self.H[index] <= min(lchild_value, rchild_value):
            return 
        # Otherwise, find the index and value of the smaller of the two children.
        # A useful python trick is to compare 
        min_child_value, min_child_index = min ((lchild_value, lchild_index), (rchild_value, rchild_index))
        # Swap the current index with the least of its two children
        self.H[index], self.H[min_child_index] = self.H[min_child_index], self.H[index]
        # Bubble down on the minimum child index
        self.bubble_down(min_child_index)
        
        
    # Function: heap_insert
    # Insert elt into heap
    # Use bubble_up/bubble_down function
    def insert(self, elt):
        self.H.append(elt)
        self.bubble_up(len(self.H) - 1)
        
        
    # Function: heap_delete_min
    # delete the smallest element in the heap. Use bubble_up/bubble_down
    def delete_min(self):
        size = len(self.H) - 1
        self.H[1], self.H[size] = self.H[size], self.H[1]
        self.H.remove(self.H[-1])

        if (len(self.H) - 1) < 1:
            return
        self.bubble_down(1)

class MedianMaintainingHeap:
    def __init__(self):
        self.hmin = MinHeap()
        self.hmax = MaxHeap()
        
    def satisfies_assertions(self):
        if self.hmin.size() == 0:
            assert self.hmax.size() == 0
            return 
        if self.hmax.size() == 0:
            assert self.hmin.size() == 1
            return 
        # 1. min heap min element >= max heap max element
        assert self.hmax.max_element() <= self.hmin.min_element(), f'Failed: Max element of max heap = {self.hmax.max_element()} > min element of min heap {self.hmin.min_element()}'
        # 2. size of max heap must be equal or one lessthan min heap.
        s_min = self.hmin.size()
        s_max = self.hmax.size()
        assert (s_min == s_max or s_max  == s_min -1 ), f'Heap sizes are unbalanced. Min heap size = {s_min} and Maxheap size = {s_max}'
    
    def __repr__(self):
        return 'Maxheap:' + str(self.hmax) + ' Minheap:'+str(self.hmin)
    
    def get_median(self):
        if self.hmin.size() == 0:
            assert self.hmax.size() == 0, 'Sizes are not balanced'
            assert False, 'Cannot ask for median from empty heaps'
        if self.hmax.size() == 0:
            assert self.hmin.size() == 1, 'Sizes are not balanced'
            return self.hmin.min_element()
        # your code here
        if self.hmax.size() == self.hmin.size():
            median = (self.hmax.max_element() + self.hmin.min_element()) / 2.0 
        else:
            median = self.hmin.min_element()
        return median
        
    
    # function: balance_heap_sizes
    # ensure that the size of hmax == size of hmin or size of hmax +1 == size of hmin
    # If the condition above does not hold, move the max element from max heap into the min heap or
    # vice versa as needed to balance the sizes.
    # This function could be called from insert/delete_median methods
    def balance_heap_sizes(self):
        # your code here
        min_size = self.hmin.size()
        max_size = self.hmax.size()
        if min_size == max_size or min_size == max_size + 1:
            return
        self.hmax.insert(self.hmin.min_element())
        self.hmin.delete_min()
        return
        
        
        
        
    
    def insert(self, elt):
        # Handle the case when either heap is empty
        if self.hmin.size() == 0:
            # min heap is empty -- directly insert into min heap
            self.hmin.insert(elt)
            return 
        if self.hmax.size() == 0:
            # max heap is empty -- this better happen only if min heap has size 1.
            assert self.hmin.size() == 1
            if elt > self.hmin.min_element():
                # Element needs to go into the min heap
                current_min = self.hmin.min_element()
                self.hmin.delete_min()
                self.hmin.insert(elt)
                self.hmax.insert(current_min)
                # done!
            else:
                # Element goes into the max heap -- just insert it there.
                self.hmax.insert(elt)
            return 
        # Now assume both heaps are non-empty
        # your code here
        self.hmin.insert(elt)
        self.balance_heap_sizes()


        
        
    def delete_median(self):
        self.hmax.delete_max()
        self.balance_heap_sizes()


m = MedianMaintainingHeap()
print('Inserting 1, 5, 2, 4, 18, -4, 7, 9')

m.insert(1)
print(m)
print(m.get_median())
m.satisfies_assertions()
assert m.get_median() == 1,  f'expected median = 1, your code returned {m.get_median()}'

m.insert(5)
print(m)
print(m.get_median())
m.satisfies_assertions()
assert m.get_median() == 3,  f'expected median = 3.0, your code returned {m.get_median()}'

m.insert(2)
print(m)
print(m.get_median())
m.satisfies_assertions()
assert m.get_median() == 2,  f'expected median = 2, your code returned {m.get_median()}'

m.insert(4)
print(m)
print(m.get_median())
m.satisfies_assertions()
assert m.get_median() == 3,  f'expected median = 3, your code returned {m.get_median()}'

m.insert(18)
print(m)
print(m.get_median())
m.satisfies_assertions()
assert m.get_median() == 4,  f'expected median = 4, your code returned {m.get_median()}'

m.insert(-4)
print(m)
print(m.get_median())
m.satisfies_assertions()
assert m.get_median() == 3,  f'expected median = 3, your code returned {m.get_median()}'

m.insert(7)
print(m)
print(m.get_median())
m.satisfies_assertions()
assert m.get_median() == 4, f'expected median = 4, your code returned {m.get_median()}'

m.insert(9)
print(m)
print(m.get_median())
m.satisfies_assertions()
assert m.get_median()== 4.5, f'expected median = 4.5, your code returned {m.get_median()}'

print('All tests passed: 15 points')

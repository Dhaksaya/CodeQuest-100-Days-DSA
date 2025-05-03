# Python Core Data Types Explained

## 1. Strings (`str`)
**Immutable** sequence of Unicode characters

```python
s = "Hello Python"

# Key Features:
- Indexing: s[0] → 'H'
- Slicing: s[1:5] → 'ello'
- Concatenation: s + "!" → "Hello Python!"
- Methods: s.upper(), s.split(), s.replace()

# Common Methods:
.lower()       # Convert to lowercase
.upper()       # Convert to uppercase
.strip()       # Remove whitespace
.split()       # Split into list
.join()        # Combine list into string
.format()      # String formatting
f-strings      # f"Value: {variable}"

# Example:
name = "Alice"
print(f"Hello {name}!")  # Hello Alice!
```

## 2. Lists (`list`)
**Mutable** ordered sequence

```python
my_list = [1, 2, 3, 'a', 'b']

# Key Features:
- Ordered (maintains insertion order)
- Changeable: my_list[0] = 99
- Allows duplicates
- Can contain mixed types

# Common Operations:
.append(x)     # Add item to end
.insert(i,x)   # Insert at position
.remove(x)     # Remove first occurrence
.pop()         # Remove and return last item
.sort()        # Sort in place
.reverse()     # Reverse in place
len(my_list)   # Get length

# Example:
fruits = ['apple', 'banana']
fruits.append('orange')  # ['apple', 'banana', 'orange']
```

## 3. Tuples (`tuple`)
**Immutable** ordered sequence

```python
my_tuple = (1, 2, 3, 'a')

# Key Features:
- Faster than lists
- Immutable (cannot change after creation)
- Often used for fixed collections
- Can be used as dictionary keys

# Common Operations:
.count(x)      # Count occurrences
.index(x)      # Find first index
len(my_tuple)  # Get length

# Example:
coordinates = (45.0, -90.0)
x, y = coordinates  # Tuple unpacking
```

## 4. Dictionaries (`dict`)
**Mutable** key-value pairs

```python
my_dict = {'name': 'Alice', 'age': 25}

# Key Features:
- Unordered (before Python 3.7)
- Keys must be immutable (strings, numbers, tuples)
- Values can be any type
- Fast lookups

# Common Operations:
.keys()        # Get all keys
.values()      # Get all values
.items()       # Get key-value pairs
.get(key)      # Safely get value
.update()      # Merge dictionaries

# Example:
person = {'name': 'Bob', 'age': 30}
person['job'] = 'Developer'  # Add new key
```

## 5. Sets (`set`)
**Mutable** unordered unique collection

```python
my_set = {1, 2, 3}

# Key Features:
- Unordered
- No duplicates
- Mathematical set operations
- Faster membership testing than lists

# Common Operations:
.add(x)        # Add element
.remove(x)     # Remove element
.union()       # |
.intersection() # &
.difference()  # -
.symmetric_difference() # ^

# Example:
primes = {2, 3, 5, 7}
primes.add(11)  # {2, 3, 5, 7, 11}
```

## 6. Range (`range`)
Immutable sequence of numbers

```python
range(5)        # 0,1,2,3,4
range(1,6)      # 1,2,3,4,5
range(10,0,-1)  # 10,9,...,1

# Key Features:
- Memory efficient (generates numbers on demand)
- Commonly used in for loops
- Supports slicing

# Example:
for i in range(3):
    print(i)  # 0 1 2
```

## 7. Bytes/Bytearray
For binary data

```python
bytes_data = b'hello'
bytearray_data = bytearray(b'hello')

# Key Differences:
- bytes: immutable
- bytearray: mutable
```

## Type Conversion
```python
int('10')      # String to integer
float('3.14')  # String to float
str(100)       # Number to string
list('abc')    # String to list → ['a','b','c']
tuple([1,2,3]) # List to tuple → (1,2,3)
set([1,1,2])   # List to set → {1,2}
dict([('a',1)]) # List of tuples to dict → {'a':1}
```

## Memory Comparison
| Type      | Mutable | Ordered | Indexed | Duplicates |
|-----------|---------|---------|---------|------------|
| List      | ✔       | ✔       | ✔       | ✔          |
| Tuple     | ✖       | ✔       | ✔       | ✔          |
| String    | ✖       | ✔       | ✔       | ✔          |
| Set       | ✔       | ✖       | ✖       | ✖          |
| Dictionary| ✔       | ✔*      | ✖       | Keys: ✖    |

* Ordered since Python 3.7

## When to Use Each
- **List**: When you need a modifiable ordered collection
- **Tuple**: For fixed data that shouldn't change
- **Set**: When you need unique elements/fast membership tests
- **Dictionary**: For key-value relationships
- **String**: All text processing


# Python Core Data Types Explained

## 1. Strings (`str`)
**Immutable** sequence of Unicode characters

```python
s = "Hello Python"

# Key Features:
- Indexing: s[0] → 'H'
- Slicing: s[1:5] → 'ello'
- Concatenation: s + "!" → "Hello Python!"
- Methods: s.upper(), s.split(), s.replace()

# Common Methods:
.lower()       # Convert to lowercase
.upper()       # Convert to uppercase
.strip()       # Remove whitespace
.split()       # Split into list
.join()        # Combine list into string
.format()      # String formatting
f-strings      # f"Value: {variable}"

# Example:
name = "Alice"
print(f"Hello {name}!")  # Hello Alice!
```

## 2. Lists (`list`)
**Mutable** ordered sequence

```python
my_list = [1, 2, 3, 'a', 'b']

# Key Features:
- Ordered (maintains insertion order)
- Changeable: my_list[0] = 99
- Allows duplicates
- Can contain mixed types

# Common Operations:
.append(x)     # Add item to end
.insert(i,x)   # Insert at position
.remove(x)     # Remove first occurrence
.pop()         # Remove and return last item
.sort()        # Sort in place
.reverse()     # Reverse in place
len(my_list)   # Get length

# Example:
fruits = ['apple', 'banana']
fruits.append('orange')  # ['apple', 'banana', 'orange']
```

## 3. Tuples (`tuple`)
**Immutable** ordered sequence

```python
my_tuple = (1, 2, 3, 'a')

# Key Features:
- Faster than lists
- Immutable (cannot change after creation)
- Often used for fixed collections
- Can be used as dictionary keys

# Common Operations:
.count(x)      # Count occurrences
.index(x)      # Find first index
len(my_tuple)  # Get length

# Example:
coordinates = (45.0, -90.0)
x, y = coordinates  # Tuple unpacking
```

## 4. Dictionaries (`dict`)
**Mutable** key-value pairs

```python
my_dict = {'name': 'Alice', 'age': 25}

# Key Features:
- Unordered (before Python 3.7)
- Keys must be immutable (strings, numbers, tuples)
- Values can be any type
- Fast lookups

# Common Operations:
.keys()        # Get all keys
.values()      # Get all values
.items()       # Get key-value pairs
.get(key)      # Safely get value
.update()      # Merge dictionaries

# Example:
person = {'name': 'Bob', 'age': 30}
person['job'] = 'Developer'  # Add new key
```

## 5. Sets (`set`)
**Mutable** unordered unique collection

```python
my_set = {1, 2, 3}

# Key Features:
- Unordered
- No duplicates
- Mathematical set operations
- Faster membership testing than lists

# Common Operations:
.add(x)        # Add element
.remove(x)     # Remove element
.union()       # |
.intersection() # &
.difference()  # -
.symmetric_difference() # ^

# Example:
primes = {2, 3, 5, 7}
primes.add(11)  # {2, 3, 5, 7, 11}
```

## 6. Range (`range`)
Immutable sequence of numbers

```python
range(5)        # 0,1,2,3,4
range(1,6)      # 1,2,3,4,5
range(10,0,-1)  # 10,9,...,1

# Key Features:
- Memory efficient (generates numbers on demand)
- Commonly used in for loops
- Supports slicing

# Example:
for i in range(3):
    print(i)  # 0 1 2
```

## 7. Bytes/Bytearray
For binary data

```python
bytes_data = b'hello'
bytearray_data = bytearray(b'hello')

# Key Differences:
- bytes: immutable
- bytearray: mutable
```

## Type Conversion
```python
int('10')      # String to integer
float('3.14')  # String to float
str(100)       # Number to string
list('abc')    # String to list → ['a','b','c']
tuple([1,2,3]) # List to tuple → (1,2,3)
set([1,1,2])   # List to set → {1,2}
dict([('a',1)]) # List of tuples to dict → {'a':1}
```

## Memory Comparison
| Type      | Mutable | Ordered | Indexed | Duplicates |
|-----------|---------|---------|---------|------------|
| List      | ✔       | ✔       | ✔       | ✔          |
| Tuple     | ✖       | ✔       | ✔       | ✔          |
| String    | ✖       | ✔       | ✔       | ✔          |
| Set       | ✔       | ✖       | ✖       | ✖          |
| Dictionary| ✔       | ✔*      | ✖       | Keys: ✖    |

* Ordered since Python 3.7

## When to Use Each
- **List**: When you need a modifiable ordered collection
- **Tuple**: For fixed data that shouldn't change
- **Set**: When you need unique elements/fast membership tests
- **Dictionary**: For key-value relationships
- **String**: All text processing


This covers:
- Detailed explanations of each core type
- Key characteristics (mutability, ordering, etc.)
- Common operations and methods
- Performance considerations
- Conversion between types
- Practical usage examples


## 1. Mutability Explained

### Immutable Objects (Cannot be changed after creation)
```python
x = 10        # int
y = 3.14      # float
s = "hello"   # str
t = (1, 2)    # tuple
frozenset({1,2}) # frozen set
```

**Key Points:**
- Any operation that "modifies" creates a new object
- Memory efficient (Python may reuse objects)
- Thread-safe
- Can be used as dictionary keys

```python
a = "hello"
b = a         # Both point to same object
a += " world" # Creates NEW string object
print(b)      # Still "hello"
```

### Mutable Objects (Can be changed after creation)
```python
lst = [1, 2]      # list
d = {'a': 1}      # dict
s = {1, 2}        # set
byte_arr = bytearray(b'hello')
```

**Key Points:**
- Modified in-place (same memory address)
- Cannot be dictionary keys
- Require synchronization in multi-threading

```python
lst1 = [1, 2]
lst2 = lst1    # Both reference same list
lst1.append(3) # Modifies shared object
print(lst2)    # [1, 2, 3]
```

## 2. DSA-Relevant Properties

### Time Complexity Cheat Sheet

| Operation       | List | Tuple | Set/Dict | String |
|----------------|------|-------|----------|--------|
| Index Access   | O(1) | O(1)  | N/A      | O(1)   |
| Append         | O(1) | N/A   | N/A      | N/A    |
| Insert         | O(n) | N/A   | N/A      | N/A    |
| Delete         | O(n) | N/A   | O(1)     | N/A    |
| Search         | O(n) | O(n)  | O(1)*    | O(n)   |
| Slice         | O(k) | O(k)  | N/A      | O(k)   |

*Average case for hash tables (sets/dicts)

### Memory Allocation

```python
# Fixed-size (more efficient):
- int, float, tuple, str (immutable)

# Dynamic-size (overhead):
- list, dict, set (store pointers to elements)
```

## 3. DSA Use Cases

### Lists
- **Stack**: `append()`/`pop()` (LIFO)
- **Queue**: (Use `collections.deque` for O(1) ops)
- **Dynamic arrays**: Automatic resizing

```python
# Stack implementation
stack = []
stack.append(1)  # push
stack.pop()      # pop
```

### Tuples
- **Fixed-size records**: `point = (x, y)`
- **Dictionary keys**: When you need compound keys
- **Function arguments**: `*args` is a tuple

### Sets
- **Duplicate removal**: `unique = set(list_with_dupes)`
- **Membership testing**: `if x in large_set:`
- **Mathematical operations**: Union, intersection

```python
# Find common elements
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1 & set2)  # {2, 3}
```

### Dictionaries
- **Hash maps**: Fast lookups by key
- **Counting**: `counts[item] = counts.get(item, 0) + 1`
- **Memoization**: Store computed results

```python
# Word frequency counter
text = "hello world hello"
count = {}
for word in text.split():
    count[word] = count.get(word, 0) + 1
```

## 4. Advanced Concepts

### Shallow vs Deep Copy
```python
import copy

lst = [1, [2, 3]]
shallow = lst.copy()       # Or lst[:]
deep = copy.deepcopy(lst)  # Creates all new objects
```

### Interning (Small Integer/String Caching)
```python
a = 256
b = 256
a is b  # True (Python caches small integers)

x = "hello"
y = "hello"
x is y  # Usually True due to string interning
```

### Hashability Requirements
```python
valid_key = ("immutable", "tuple")  # OK
invalid_key = ["mutable", "list"]   # TypeError
```

## 5. Practical DSA Examples

### 1. Anagram Check (Using dict/set)
```python
from collections import defaultdict

def is_anagram(s1, s2):
    counts = defaultdict(int)
    for c in s1: counts[c] += 1
    for c in s2: counts[c] -= 1
    return all(v == 0 for v in counts.values())
```

### 2. LRU Cache (Using OrderedDict)
```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
```

### 3. Graph Representation
```python
# Adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': [],
    'D': []
}

# Matrix (2D list)
matrix = [
    [0, 1, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
```

## 6. Memory Diagram Example

```
Immutable (int)          Mutable (list)
┌─────────┐             ┌─────────┐
│ x = 10  │             │ lst =   │
└─────────┘             │  ┌───┬───┬───┐
                        │  │ 1 │ 2 │ 3 │
                        │  └───┴───┴───┘
                        └─────────┘
After modification:
x = x + 5               lst.append(4)
(NEW object created)     (Same object modified)
```

## Key Takeaways
1. **Choose data structures based on:**
   - Required operations (lookup/insertion/deletion)
   - Memory constraints
   - Thread safety needs

2. **Optimization guidelines:**
   - Use tuples for fixed-size data
   - Prefer sets for membership testing
   - Use dicts for key-value relationships with fast lookups
   - Lists for dynamic arrays (but deque for queues)


This covers:
- Deep dive into mutability with memory diagrams
- Time/space complexity analysis
- Practical DSA applications
- Advanced Python-specific behaviors
- Real-world optimization examples


# Python Garbage Collection & Data Types

## 1. Memory Management Fundamentals

### Reference Counting (Primary Mechanism)
```python
x = [1, 2, 3]  # Reference count = 1
y = x          # Ref count = 2
del x          # Ref count = 1
y = None       # Ref count = 0 → Memory freed
```

**How it works:**
- Every object has a counter of references to it
- When count drops to 0, memory is immediately reclaimed
- Affects ALL Python objects regardless of type

### Generational Garbage Collection (Secondary Mechanism)
```python
import gc
gc.collect()  # Manually trigger collection
```

**Purpose:**
- Handles **reference cycles** (e.g., `a = []; a.append(a)`)
- Three generations (0=young, 1=medium, 2=old)
- Objects that survive collections get promoted

## 2. Garbage Collection by Data Type

### Immutable Types (int, float, str, tuple)
```python
a = 100
b = 100  # Often reuses same object (interning)
```

**Behavior:**
- Frequently reused via interning (-5 to 256 integers, short strings)
- No reference cycles possible with pure immutable objects
- Memory freed immediately when refcount=0

### Mutable Types (list, dict, set)
```python
lst = [1, [2, 3]]  # Nested mutable structure
lst.append(lst)     # Creates reference cycle
```

**Behavior:**
- Can create reference cycles (requires generational GC)
- Higher memory overhead (store pointers + growth space)
- Special cases:
  ```python
  # Dictionary key deletion doesn't immediately shrink memory
  d = {k: None for k in range(10_000)}
  del d[0]  # Memory not immediately freed
  ```

## 3. Special Cases & Optimizations

### String Interning
```python
a = "hello_world"
b = "hello_world"
a is b  # May be True for certain strings
```

**Rules:**
- Automatically interns:
  - All identifiers (variable/function names)
  - Strings containing only [a-zA-Z0-9_]
- Manual interning: `sys.intern()`

### Tuple vs List Memory
```python
import sys
lst = [1, 2, 3]
tup = (1, 2, 3) 
sys.getsizeof(lst)  # Typically larger than tuple
```

**Why:**
- Tuples allocate exact size needed
- Lists overallocate to allow O(1) appends

## 4. Circular References & GC

### How Cycles Happen
```python
class Node:
    def __init__(self):
        self.parent = None

a = Node()
b = Node()
a.parent = b
b.parent = a  # Cycle created
```

**Collection Process:**
1. Generational GC runs periodically
2. Traces objects starting from roots (globals, stack)
3. Identifies unreachable cycles
4. Calls `__del__` methods (if exists)
5. Frees memory

## 5. Controlling Garbage Collection

### Manual Control
```python
import gc

gc.disable()  # Pause automatic GC
gc.enable()   # Resume
gc.collect()  # Force full collection
```

### Tuning Parameters
```python
gc.set_threshold(700, 10, 10)  # (gen0, gen1, gen2)
```

**Default Thresholds:**
- Generation 0: 700 allocations
- Generation 1: 10 collections of gen0
- Generation 2: 10 collections of gen1

## 6. Memory Profiling Example

```python
import tracemalloc

tracemalloc.start()
# Your code here
snapshot = tracemalloc.take_snapshot()
for stat in snapshot.statistics('lineno'):
    print(stat)
```

## 7. Best Practices

1. **For large datasets:**
   - Use generators (`yield`) instead of lists
   - Prefer `array.array` for homogeneous numeric data
   - Consider `__slots__` for classes with many instances

2. **Avoid memory leaks:**
   - Break cycles manually when possible
   - Use weak references (`weakref`) for caches
   - Close file handles/responses explicitly

3. **Performance-critical code:**
   - Reuse objects when possible
   - Minimize temporary object creation
   - Consider manual GC control during batches

## Real-world Example: Cache Implementation

```python
import weakref

class Cache:
    def __init__(self):
        self._storage = weakref.WeakValueDictionary()
    
    def store(self, key, value):
        self._storage[key] = value
```

**Why WeakRef?**
- Allows cached objects to be garbage collected
- Automatically removes entries when objects are gone
- Prevents memory leaks in long-running applications
```

Key takeaways:
1. **Immediate cleanup** happens via reference counting for all objects
2. **Generational GC** handles cyclic references (mostly affects mutable types)
3. **Special optimizations** exist for immutable types
4. **Memory management** differs significantly between:
   - Large vs small objects
   - Short-lived vs long-lived objects
   - Cyclic vs acyclic structures




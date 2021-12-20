## Data Types
### I. Numeric Types
There are three python numeric types - integer, float, and complex. Additionally, Boolean is a subtype of integers. Numbers are created by numeric literals or as a result of built-in functions and operators. Python fully supports mixed arithmetic: for instance, operations between integers and floats will first convert the integers to float then proceed with the operation. Type casting between different numeric types can be done simply by calling:
- ```int()```: converts to integer
- ```float()```: converts to float
- ```complex()```: converts to complex

The following operations are supported by numeric types in Python: 
- ```x+y```: addition
- ```x-y```: subtraction
- ```x*y```: multiplication
- ```x/y```: division
- ```x//y```: floored division. -i.e. $5//2 =2$
- ```x%y```: modulo - i.e $5\%2=1$
- ```abs(x)```: absolute
- ```divmod(x,y)```: returns a tuple of ```(x//y,x%y)```
- ```pow(x,y)```: return x to the power of y
- ```x**y```:return x to the power of y

### II. Iterator and Iterable
#### 2.1 Sequence Types - List, Tuple, Range
##### 2.1.1 List
Lists are mutable sequences, usually used to store homogeneous items. However, it is possible to store data of diferent types in a list.

List can be constructed by: 
- ```[]```: using square brackets to denote an empty list.
- ```[a,b,c]```: using square brackets with items separated by commas.
- ```[i for i in iterable]```: using list comprehension.
- ```list(iterable)```: using the list constructor.

List comprehension: a Pythonic way to create a list from an iterable. This is usually done is some simple operations are applied on every member of an iterable. A list comprehension consists of brackets containing an expression followed by a `for` clause, then zero or more `for` or `if` clauses. For example:
- Get a list whose values are the square from 0 to 5: ```x = [i**2 for i in range(6)]```.
	- Note that this is equivalent to writting:
	```Python
	x = []
	for i in range(6):
		x.append(i**2)
	```
- Get a list of csvs who have the same roots but different names: ```csv_list = [os.path.join(root_dir,filename) for filename in filenames]```
	- Note that this is equivalent to writting:
	```Python
	csv_list = []
	for filename in filenames:
		name = os.path.join(root_dir,filename)
		csv_list.append(name)
	```
- Get a list of numbers from a given list that is divisible by 11:```x = [i for i in A if i % 11 == 0]```
- Get a meshgrid of x and y: ```coords = [(i,j) for i in x_coords for j in y_coords]```. 
	- Note that this is equivalent to writting:
	```Python
	coords = []
	for i in x_coords:
		for j in y_coords:
			coords.append((i,j))
	```

List comprehension can also be nested to create a list of list:
- For example, to create a 3x3 identity matrix: ```matrix = [[1 if row == col else 0 for col in range(3)] for row in range(3)]``` 

#### 2.1.2 Tuples
Similar to list, tuples is also a sequence data type. Tuple's values are enclosed in circular brackets. Unlike mutable sequences list like, tuples are immutable, meaning that its values cannot be modified. Tuples can be constructed by: 
- Using a pair of circular brackets to denote empty tuples: `()`.
- Using trailing comma for singleton tuples: `a,` or `(a,)`
- Separating items with commas: `a,b,c` or `(a,b,c)`
- Using the `tuple` constructor: `tuple(iterable)`
```Python
>>>list_array = [1,2,3]
>>>list_array[0]=5
>>>list_array
[5,2,3]
>>>tuple_array=(1,2,3)
>>>tuple_array[0]=5
TypeError: tuple object does not support item assignment.
```
Note that tuple can contain mutable object:
```Python
>>>x = ([1,2,3],[4,5,6])
>>>x[0][1]=5
>>>x
([1,5,3],[4,5,6])
```
Tuples are usually used for packing and unpacking objects of different types (i.e. outputs of functions):
```Python
>>>tuple_array = 1,2,3 #Tuple packing
>>>x,y,z = tupple_array #Tuple unpacking
>>>print(x,y,z)
1 2 3
```
Empty tuples are constructed by an empty set of circle brackets, a singleton tuple must have a trailing comma.
```Python
>>>empty=() #Empty tuple
>>>singleton= 1, #Singleton tuple
```

#### 2.1.3 Ranges
The `range` type represents an immutable sequence of numbers and is commonly used for looping a specific number of times in `for` loops. Range can be constructed by:
- `range(stop)`: create an immutable sequence of values from `0` to `stop`. 
- `range(start,stop,step)`: immutable sequence of values from `start` to `stop` in `step`.

Note that the `range` operation creates a generator object, which is more memory efficient than `list` or `tuple`, since it will always take the same amount of memory, no matter the size of the object it represents. 

#### 2.1.4 Common sequence operations:
The following operations are supported by most sequence types, including mutable and immutable.
- `value in array`: check if the given value appears in the array - return Boolean result.
- `value not in array`: check if given values does not appear in the array - return Boolean result.
- `array_1 + array_2`: concatenation of `array_1` and `array_2`.
- `array*n`: concatenation of `array` by itself `n` times.
- `array[i]`: get the i-th value of the array.
- `array[i:j]`: slice the array from index `i` to `j`.
- `array[i:j:k]`: slice the array from `i` to `j` with step `k`.
- `len(array)`: get the length of the array.
- `min(array)`: find the minimum value.
- `max(array)`: find the maximum value.
- `array.count(value)`: count the number of times the value appear in the array.
- `array.index(value,start_index,end_index)`: find the index of the first occurence of the value in the array starting from the `start_index` to the `end_index`.
 
 #### 2.1.4 Mutable sequence operations:
The following operations are supported by mutable sequence types. Calling them on immutable sequences will return an error. All of the following operations will alter the values of the sequence, hence not defined for immutable types.
- ```array.append(x)```: add item ```x``` to the end of the array
- ```array.extend(iterable)```: extend the array by appending all items in ```iterable```.
- ```array.insert(index,value)```: insert the value at the given index.
- ```array.pop(index)```:remove the value at the given index and return it. If no index is provided, pop the last value.
- ```array.remove(value)```: remove the first item from the array whole value is given. The flag ValueError will be raised if no such value is available. 
- ```array.reverse()```: reverse the element of the list inplace. 
- ```array.sort()```: sort the list inplace.
- ```array.copy()```: create a shallow copy of the list.
- ```array.clear()```: remove all items from the array.
- ```array[i]=value```: reassign value at index `i`.
- ```array[i:j]=t```: reassign values from `i` to `j` by values in the iterable `t`. Note that `t` must have the same length as the array it replaces.
 
 #### 2.1.5 Dictionaries
Unlike sequences which are indexed by numbers, dictionaries are indexed by `keys`, which can be `string`. Tuples can be used as keys if they contain only strings, number or tuples: if a tuple contains any mutable object either directly or indirectly. List cannot be used as keys. 


### Class Iterator, Iterable, Generator
#### 2.2.1 Iterable
Iterable is an object that is capable of returning its member one at a time - i.e. native sequence types likes `list,tuples` are iterator. Classes defined with an `__iter__()` method or a `__getitem__()` method are also iterables. 

When an iterable object is passed as an argument to the built in function `iter()`, it returns an iterator, which is used to run one pass over the object. Note that when using a `for` loop  you don't need to use the `iter` function.

#### 2.2.2 Iterator
An object representing a stream of data. Repeated calls to the iterator’s `__next__()` method (or passing it to the built-in function `next()` return successive items in the stream. When no more data are available a `StopIteration` exception is raised instead. At this point, the iterator object is exhausted and any further calls to its `__next__()` method just raise `StopIteration` again. Iterators are required to have an `__iter__()` method that returns the iterator object itself so every iterator is also iterable and may be used in most places where other iterables are accepted. One notable exception is code which attempts multiple iteration passes. A container object (such as a `list`) produces a fresh new iterator each time you pass it to the `iter()` function or use it in a `for` loop. Attempting this with an iterator will just return the same exhausted iterator object used in the previous iteration pass, making it appear like an empty container.

#### 2.2.3 Generator

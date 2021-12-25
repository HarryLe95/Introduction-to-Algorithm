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
Unlike sequences which are indexed by numbers, dictionaries are indexed by `keys`, which can be `string`. Dictionary maps hashable values (`keys`) to arbitrary mutable objects (`values`). Since dictionary keys are hashable - its value never changes in its lifetime, number and string literals, and tuples (which contains immutable objects) can be used as `keys`. `List` cannot be used as `keys`. Dictionary keys cannot be duplicates. 

Dictionaries can be created using a list of `key: value` pairs separated by commas. For instance:
```Python
bulba_evolution = {1:"bulbasaur",2:"ivysaur",3:"venusaur"}
char_evolution = {'first':'charmander','second':'charmanleon','third':'charizard'}
```
Dictionaries can also be created using dictionary comprehension:
```Python
stage = ['first','second','third']
name = ['squirtle','wartotle','blastoise']
squirt_evolution = {key:val for (key,val) in zip(stage,name)}
```
Or by using the dictionary constructor:
```Python
abra_evolution = dict(zip(['first','second','third'],['abra','kadabra','alakazam']))
dict_list = dict(one=1,two=2,three=3)
```

Common dictionary operations:
- `d.keys()`: return the keys of the dictionary `d`.
- `d.values()`: return the values of the dictionary `d`.
- `d.items()`: return tuples of `(key,value)` in `d`.
- `d.clear()`: clear all items in `d`.
- `d.copy()`: return a shallow copy of `d`.
- `d.update(new_dict)`: update `d` with key-value pairs from new_dict
- `d.pop(key)`: remove the value of `d[key]` and return its value.
- `d.popitem()`: remove an return a key:value pair in a last in first out order.
- `iter(d)`: return an iterator over the keys of `d`.
- `reversed(d)`: return a reverse iterator over the keys of `d`.

*Note* Dictionary preserve insertion order - i.e. keys are arranged by order of creation and are not sorted. Updating a key does not change its order. 

Some examples:
```Python
#Creating dictionaries
>>alkali_metals_1 = {'Li':"Lithium",'Na':'Sodium','K':'Potassium'}
>>alkali_metals_1
{'Li': 'Lithium', 'Na': 'Sodium', 'K': 'Potassium'}
>>alkali_metals_2 = {'Rb':'Rubidium'}
>>alkali_metals_2

#Getting values:
>>print(alkali_metals_1['Li'])
Lithium

#Checking if an item is in dictionary - keys:
>>print("Be" in alkali_metals_1)
False
>>print("Na" in alkali_metals_1)
True

#Adding new element:
>>alkali_metals_2['Cs']='Caesium'
>>alkali_metals_2['Be']='Beryllium'
>>alkali_metals_2['Mg']='Magnesium'
>>print(alkali_metals_2)
{'Rb': 'Rubidium', 'Cs': 'Caesium', 'Be': 'Beryllium', 'Mg': 'Magnesium'}

#Removing an element:
>>alkali_metals_2.pop('Be')
'Beryllium'
>>del alkali_metals_2['Mg']
>>print(alkali_metals_2)
{'Rb': 'Rubidium', 'Cs': 'Caesium'}

#Updating one dictionary with another:
>>alkali_metals_1.update(alkali_metals_2)
>>alkali_metals_1
{'Li': 'Lithium', 'Na': 'Sodium', 'K': 'Potassium', 'Rb': 'Rubidium', 'Cs': 'Caesium'}

#Using dictionary in a for loop:
for (key,value) in alkali_metals_1.items():
	print(keys,values)
```
#### 2.1.6 Sets
A _set_ object is an unordered collection of distinct hasble objects. Common uses include membership testing, removing duplicates from a sequence, and computing mathematical operations such as intersection, union, difference, and symmetric difference.

Being an unordered collection, list does not record order of insertion or element position. As such, you can't get set elements by indexing. There are two set types:
- `set`: mutable - you can `add` and `remove` items.
- `frozenset`: immutable - its contents can not be altered once set. 

Set creation:
- Using comma-separated list with curly brackets: `two_d_ops = {'parameter','area'}`.
- Using set constructor: `three_d_ops = set(['parameter','area','volume'])`
- Using set comprehension: `one_d_ops = {op for op in ['lenth']}`

Supported operations:
- `len(s)` : get length
- `x in s`: check for inclusion
- `s1.isdisjoint(s2)`: return True if two sets `s1`,`s2` are disjoint -i.e. having no common member.
- `s1.issubset(s2)`: return True if `s1` is a subset of `s2` - i.e. all elements in `s1` are in `s2`.
- `s1 <= s2`: same as `s1.issubset(s2)`.
- `s1 < s2`: check whether `s1` is a proper subset of `s2` -i.e if elements of `s1` are in `s2` but `s1` is not `s2`.
- `s1.issuperset(s2)`: return True if `s2` is a subset of `s1`.
- `s1>=s2`: same as `s1.issuperset(s2)`
- `s1>s2`: return True if `s2` is a proper super set of `s1`.
- `s1.union(s2)`: return the union of `s1` and `s2` - i.e. contains all elements of `s1` and `s2`.
- `s1|s2`: the same as `s1.union(s2)`.
- `s1.intersection(s2)`: return the intersection between `s1` and `s2` - i.e. elements in both `s1` and `s2`.
- `s1 & s2`: the same as `s1.intersection(s2)`.
- `s1.difference(s2)`: return elements in `s1` but not in `s2`.
- `s1 - s2`: same as `s1.difference(s2)`
- `s1.symmetric_difference(s2)`: return elements in either `s1` or `s2` but not both.
- `s1 ^ s2`: same as `s1.symmetric_difference(s2)`

Some examples: 
```Python
s1 = {1,2,3,4}
s2 = {2,3,4}
s3 = {3,4,5}

#Check subset
s1 < s2 #False
s1 > s2 #True
s1 >= s3 #False

#Get union
s1|s2 # {1,2,3,4}
s1|s3 # {1,2,3,4,5}

#Get intersection
s1&s2 # {2,3,4}
s1&s3 # {3,4}

#Get difference:
s1 - s2 #{1}

#Symmetric difference
s1 ^ s3 # {1,2,5}

```

Some operations available for `set` but not `frozenset`: 
- `s1.update(s2)`: update `s1` with elements of `s2`, similar to dictionary method `update`.
- `s1 |= s2`: same as `s1.update(s2)`
- `s1.intersection_update(s2)`: update but keep only the intersection
- `s1 &= s2`: same as `s1.intersection_update(s2)`.
- `s1 -= s2`: same as `s1.difference_update(s2)` update but remove the elements common with `s2`.
- `s1 ^= s2`: same as `s1.symmetric_difference_update(s2)` update but keep elements in either set not both.
- `s1.add(element)`: add `element` to `s1`.
- `s1.remove(element)`: remove `element` from `s1`.

###  Iterator, Iterable, Generator
SInce Iterator, Iterable and Generator are advanced concepts, they will be revisted in later chapters. 
#### 2.2.1 Iterable
Iterable is an object that is capable of returning its member one at a time - i.e. native sequence types likes `list,tuples` are iterator. Classes defined with an `__iter__()` method or a `__getitem__()` method are also iterables. 

When an iterator object is passed as an argument to the built in function `iter()`, it returns an iterator, which is used to run one pass over the object. Note that when using a `for` loop  you don't need to use the `iter` function.

#### 2.2.2 Iterator
An object representing a stream of data. Repeated calls to the iterator’s `__next__()` method (or passing it to the built-in function `next()` return successive items in the stream. When no more data are available a `StopIteration` exception is raised instead. At this point, the iterator object is exhausted and any further calls to its `__next__()` method just raise `StopIteration` again. Iterators are required to have an `__iter__()` method that returns the iterator object itself so every iterator is also iterable and may be used in most places where other iterables are accepted. One notable exception is code which attempts multiple iteration passes. A container object (such as a `list`) produces a fresh new iterator each time you pass it to the `iter()` function or use it in a `for` loop. Attempting this with an iterator will just return the same exhausted iterator object used in the previous iteration pass, making it appear like an empty container.

#### 2.2.3 Generator
Generator function is a function that returns a lazy iterator, which allows you to iterate over like a list. However, unlike a list, the evaluation is delayed until needed, which decouples the process of evaluation and the process of storage, effectively reducing memory footprint. Using a generator function, it is possible to create an infinite data structure. 
- Using `yield` in a function will make it return a generator object.
- Using *generator expression* -i.e. `x = (i for i in range(6))` returns a generator object. 
- You can extract data from a generator using a `for` loop or by using the `next` function.

### III. Strings
Textual data in Python is handled with `str` objects, or _strings_. Strings are immutable sequences of Unicode code points. Since there is no separate “character” type, indexing a string produces strings of length 1. Note that since string is immutable, you cannot change its value via common sequence indexing -i.e. 

```Python
var_1 = ['a','b','c']
var_1[0] = 'd' #Supported 

var_2 = 'abc'
var_2[0] = 'd' #TypeError - 'str' object does not support item assignment
```

Additionally, string methods will return a new string (the original string is left intact). Some useful string methods are:
- `s.lower()`: return a new string with all case characters uncapitalised.
- `s.upper()`: return a new string with all case characters capitalised.
- `s.capitalize()`: return a new string with the first character capitalised.
- `s.isalnum()`, `s.isdigit()`, `s.isalpha()`: check if string `s` contains alphanumeric characters (either alphabetic characters or numeric characters), numeric characters, or alphabetic characters. Additionally, `s` must not be empty to return True.
- `s.split(separator,maxsplit)`: return a list of words in the string separated by a separator. If `maxsplit` is set to -1 or not given, return all separations.
- `s.join(iterable)`: return a string that is a concatenation of all sub-strings in iterable separated by string `s`. `s` can be set to `''` to join the substrings with no space, `' '` to join the substrings with space, or `'/'` to join the substrings in a directory-like manner.
For example:
```Python
>>path = 'home/user/hoangsonle/Desktop' 
>>split_list = path.split('/')
>>split_list
['home','user','hoangsonle','Desktop']
>>'/'.join(split_list)
'home/user/hoangsonle/Desktop'
```

#  Collections (group of heterogeneous elements )

#  Types 
#       1> IMMUTABLE / NON-MODIFIABLE   
#               --> can't be updated 
#       2> MUTABLE / MODIFIABLE
#               --> can be updated


#### 1> IMMUTABLE / NON-MODIFIABLE Collection
##  a> Tuple  --- Fixed Collection
######      represented by () or tuple()
######      can't be created, updated or deleted
######      Tuple length always fixed


# b=()  # ### can be created but we can't place a new element in a empty tuple
# print(b)

# a = (1,2,3,23,234)
# print(a)

# a = 1,2,3,23,234
# print(a)
# print(len(a))
# print(min(a))
# print(max(a))
# print(sum(a))
# print(type(a))


# a = 1,2,3,23,234,'Hello', 'a', 'Z','A'
# print(a)
# print(len(a))
# print(type(a))


# a = 'Hello', 'a', 'Z','A'
# print(min(a))
# print(max(a))


# a = 'Hello', 'a', 'Z','A'
# print(dir(a))

# print(a.count('A'))
# print(a.index('A'))

# print(a[0])
# print(a[-4])

# b = a[0:2]
# print(b)


##### Tuple Packing / Unpacking
# a = 'Hello', 'a', 'Z','A'   #### Tuple Packing

# p,q,r,s = a   #### Tuple Unpacking
# print(p)
# # print(q)
# # print(r)
# print(s)


# a = 0
# b=0 
# c=9

# a,b,c = 0,0,9



##  b> Set  --- Collection with random indexes of elements
######      represented by set() if set is empty
######      if not empty, then can be represented by {element1, element2, ...}
######      can be created or deleted
######      can't be updated 
######      always removes duplicate element
######      only holds unique elements but with random indexes


# ## to create a empty set
# a = set()
# print(a)

# ## to create a set of pre-defined elements
# a = {1,2,3,45,32,4,3,3,3,123,123,123,456,423,434,53,454,64, 'ram', 'shyam', 'mohan'}
# print(a)


#####  Set Operations
a = {1,2,4,5,3}
b = {'a','b','c','d',1,2,3}


# ## union 
# print(a.union(b))
# print(a|b)

# ## intersection
# print(a.intersection(b))
# print(a&b)

# ## difference

# print(a.difference(b))
# print(a-b)

# print(b.difference(a))
# print(b-a)


# print(dir(a))
###### 'add', 'clear', 'copy', 'difference', 'discard', 'intersection', 'issubset', 'issuperset', 'pop', 'remove', 'union', 'update'

b = {'a','b','c','d',1,2,3}
# b.add('Hello')
# print(b)

# b.remove('d')
# print(b)

# b.remove('z')  ## if element is not available , then it will throw an error
# print(b)

# b.discard('d')
# print(b)

# b.discard('z')
# print(b)

# b.update('a', 'z')
# print(b)

# print(b.pop())
# print(b)

# b.remove('a')
# print(b)

# c = b.copy()
# print(c)

# c = b
# print(c)


# b = {'a','b','c','d',1,2,3}   ### Universal Set
# c = {1,2,3}

# print(c.issubset(b))
# print(c.issuperset(b))

# b.clear()
# print(b)
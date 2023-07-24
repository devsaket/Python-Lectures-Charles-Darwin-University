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
# a = {1,2,4,5,3}
# b = {'a','b','c','d',1,2,3}


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

# b = {'a','b','c','d',1,2,3}
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



#### 2> MUTABLE / MODIFIABLE Collection
##  a> List  --- Dynamic Collection
######      represented by [] or list()
######      can be created, updated or deleted
######      List length always Flexible

### to create a empty list 
# li = []
# print(type(li))
# print(li)

# li = list()
# print(type(li))
# print(li)


### to create a list with pre-defined elements
# li = [1,2,3,4,6,84,45]
# print(li)

# t = 1,2,3,4,6,84,45
# li = list(t)
# print(li)

# t = {1,2,3,4,6,84,4,5,6,45}
# li = list(t)
# print(li)


##### to find all the unique element of list
# li = [1,2,3,4,6,84,4,5,6,45]
# print(list(set(li)))



#######################################
#############  LIST OPERATION
#######################################

# li1 = [1,2,3,4,5,5,5,6,6,7]
# li2 = ['a','b','c','d','e','f']

#### List Extending
# print(li1+li2) 

# List Repeation
# print(li1*2)

# print(len(li1))
# print(min(li1))
# print(max(li1))
# print(sum(li1))

# print(len(li2))
# print(min(li2))
# print(max(li2))



# ####### List Traversal / Accessing of element
# print(li2[2])
# print(li2[-5])


# # ### List Slicing / Sub-List
# print(li2[1:-1])
# print(li2[1:-1 : 2])
# print(li2[::-1])


##### ### LIST METHODS
# li1 = [1,2,3,4,5,5,5,6,6,7]
# li2 = ['a','b','c','d','e','f']

# print(dir(li1))
####'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

# li3 = li1 + li2
# print(li3)


# print(li1,li2)
# # li1 = li1 + li2
# li1.extend(li2)
# print(li1)

# ### append  (insert element at the end of the list)
# li1.append(12312)
# print(li1)


# ### insert  (insert element at the any specified index of the list)
# li1.insert(3, 'Hello World')
# print(li1)

# # ### pop  (delete element at the end of the list)
# li1.pop()
# print(li1.pop())
# print(li1)

# ### remove  (remove any specified element of the list)
# li1.remove(5)
# print(li1)

# ### delete element at the any specified index of the list)
# del(li1[2])
# print(li1)

# del(li1)
# print(li1)


# ### to count repetition of any element
# print(li1.count(5))

# ### to find index of any specified element
# print(li1.index(4))

# print(li1.index(5,6,8))
# print(li1.index(5,7,9))


# #####  to reverse a list
# print(li1[::-1])
# li1.reverse()
# print(li1)

# #####  to sort (ascending order) a list
li3= [12,3,4,23,6,5,8,34,56,22]
# li3.sort()
# print(li3)

# #####  to sort in descending order 
li3= [12,3,4,23,6,5,8,34,56,22]
# li3.sort()
# li3.reverse()
# print(li3)

# li3.sort(reverse=True)
# print(li3)

# li3.sort()
# print(li3[::-1])


# #### to copy a list
# li3= [12,3,4,23,6,5,8,34,56,22]

# li4 = li3  ### Soft copy / Soft Link
# li5 = li3.copy()   ### Hard copy / Hard Link
# print(li4)
# print(li5)

# li3[4]= 'Hello'
# print(li3)
# print(li4)
# print(li5)

# ### to delete all element of list
# li3.clear() 
# print(li3)

# # #### to  delete a list 
# del(li3)
# print(li3)
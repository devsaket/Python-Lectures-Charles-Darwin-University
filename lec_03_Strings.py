#  String 

# Sequence of characters 
# represented by "" or '' 

# a = 'Hello World'
# b = "Ram's Car"
# c = 'My Name is "XYZ", from "CHD"'

# print(a, b)
# print(c)


# ### Multi-line String (used for documentation)
# d = '''Hello World 
#                     My Name is saket
# '''

# print(d)




#########################################
############     String Operations    ###
#########################################

#### string concatenation

# a = 'hello'
# b= 'world'
# c = '23123'

# d = a +' '+ b + ' ' + c
# print(d)


#### string repetition
# a = 'Hello'
# print(a*5)
# print((a + ' ')*5)
# print((a + '\n')*5)
# print((a + '--')*5)


#########################################
############    Indexing of String    ###
#########################################

# a = 'Hello World'

###  -11 -10 -9 -8 -7 -6 -5 -4 -3 -2  -1   [ negative | RL indexing]
###   H   e   l  l  o     W  o  r  l   d
###   0   1   2  3  4  5  6  7  8  9  10   [ positive | LR indexing | indexes]

# print(a[3])
# print(a[-5])




#########################################
############    Slicing of String    ###
#########################################

# a = 'Hello World'

###  -11 -10 -9 -8 -7 -6 -5 -4 -3 -2  -1   [ negative | RL indexing]
###   H   e   l  l  o     W  o  r  l   d
###   0   1   2  3  4  5  6  7  8  9  10   [ positive | LR indexing | indexes]

# print(a[3])
# print(a[-5])

# print(a[1:8])  ##  'ello Wo'
# print(a[-10:-3])
# print(a[-10:8])
# print(a[1:-3])


#### variable[start index : end index : step]
# print(a[1:8:1])
# print(a[1:8:2])

##### substring from beginning to index 8
# print(a[0:8:1])
# print(a[:8:1])
# print(a[:8])

##### substring from index 4 to end of string
# print(a[4:11:1])
# print(a[4::1])
# print(a[4:])


#####  Reverse of a string
# a = 'Hello World'
# print(a[::-1])
# print(a[::-2])



#########################################
############    String Methods        ###
#########################################
# a = 'Hello World'
# print('Length of string = ', len(a))
# print('to find Data Type of string = ', type(a))

# ### whitespace, number, Uppercase , Lowercase 
# print(min(a))
# print(max(a))

# a = 'Hello World'
# print(dir(a))  ## to list all methods of string


# #####Possible Methods
###########
### 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'


# a= 'Hello'
# b= 'world'

# print(a+b)
# print(a.__add__(b))


# #########  Text Formatting Methods
# c = 'india is my country'
# d = "HELlo WorLD"
# print(c.capitalize())
# print(c.upper())
# print(d.lower())
# print(d.casefold())
# print(d.swapcase())
# print(c.title())

# ###  '             india is my country             ' = 60character
# print(c.center(60))
# print(c.center(60,'-'))
# print(c.ljust(60,'-'))
# print(c.rjust(60,'-'))


# e = 'Https://www.google.com/'
# f = '          Hello      Ram             '

# print(f.strip())
# print(f.lstrip())
# print(f.rstrip())

# print(e.lstrip('Https://www.'))
# print(e.removeprefix('Https://www.'))  

# print(e.rstrip('.com/'))
# print(e.removesuffix('.com/'))


# print('-'.join("Hello"))

# g= '22134234'
# print(g.zfill(17))

a =12
b = 13
c = 14
d =34

# print("value of a = ", a,"\tvalue of b = ",b,"\tvalue of c = ",c,"\tvalue of d = ",d)
# print("value of a = {}\tvalue of b = {}\tvalue of c = {}\tvalue of d = {}".format(a,b,c,d))
# print("value of a = {0}\tvalue of b = {1}\tvalue of c = {2}\tvalue of d = {3}".format(a,b,c,d))

# print("value of a = {m}\tvalue of b = {n}\tvalue of c = {p}\tvalue of d = {q}".format(m = a,n=b,p=c,q=d))

# print(f"value of a = {a}\tvalue of b = {b}\tvalue of c = {c}\tvalue of d = {d}")



# #########  Other Useful Methods

a = 'Hello World'
# print(a.count('l'))
# print(a.index('W'))
# print(a.find('W'))


#### print(a.index('Z'))
# print(a.find('Z'))

# print(a.rindex('l'))
# print(a.rfind('l'))

# a = a.replace("Hello", "Nyi duniya")
# print(a)


# a = "India is my country"
# print(a.split())
# print(a.split('i'))
# print(a.rsplit())
# print(a.rsplit('i'))

# a = "India is my country.\nHello Everyone\n How do you do?"
# print(a.splitlines())


# a = "India is my country"
# print(a.partition(' '))
# print(a.rpartition(' '))


# #########  String Conditional Methods

a= "Hello World 123"
# print(a.startswith('he'))  ### False
# print(a.endswith('he'))  ## False

# print(a.isalnum())  ## False
# print(a.isalpha())  ## False
# print(a.isascii())  ## True
# print(a.islower())  
# print(a.isupper())
# print(a.istitle())

print("Hello\n World")
# print(' \n\t'.isspace())


d = '2134324'
# print(d.isdigit())
# print(d.isnumeric())
# print(d.isdecimal())

# print(d.isidentifier())
# print(d.isprintable())

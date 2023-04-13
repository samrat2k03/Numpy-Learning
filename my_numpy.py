import numpy as np 

### sample code for numpy ###
a = np.array([1,2])
b = np.array([2,2])
print(a+b)

# #check dimension 
# a = np.array([1,2])
# print(a.ndim)  ### it throws the dimensions of the a varibles array
 

### 1 dimensions ###
oneD = np.array([1,2])
print(type(oneD))
print(oneD.ndim)   

### 2 Dimensions ###
two_d = np.array([[1,2,3],[3,2,1]])
print(two_d)
print(two_d.ndim)

### 3 Dimensions ###
three_d = np.array([[[1,2,3],[3,2,1],[0,2,3]]])
print(three_d)
print(three_d.ndim)

###  shape ### 
### it shows the matix order of the array
print(oneD.shape)
print(two_d.shape)
print(three_d.shape)

### total size ###
print(a.nbytes)

### Accessing changing the specific element, rows, columns ###
### ------------------------------------------------------------

samrat = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(samrat)

# specific element --> (row,column)
s = samrat[0,2]
print(s)

# specific row --> it throws only 0th row ie... first row
r = samrat[0,:]
print(r)

# specific column --> it throws only column 
c = samrat[:,3]
print(c)

# Changing a specific element

samrat[0,4] = 1000
print(samrat)


# selecting specific items (many items) [row,startindex:endindex:stepsize]
samrat_special_case = samrat[0,0:3:1]
print(samrat_special_case)

### initializing different types of arrays
# --> all zeros
zeroes = np.zeros([1,5])
print(zeroes)

# --> all ones
one = np.ones([3,10])
print(one)

#all other numbers

other_number = np.full([2,2],100)
print(other_number)

# --> full like --> it changes all character in list into specified number
samrat1 = [[1,2,654,7665,887]]
full_like_example = np.full_like(samrat1,10)
print(full_like_example)

### Random decimal number ###

# np.random.rand(10,2,3)
print(np.random.rand(10,2,3))

### random integer values
samrat2 = np.random.randint(7,10,size=(2,2))
print(samrat2)

### identity matrix 
print(np.identity(5))

### repeat an array
samrat3 = np.array([[1,2,3,4,5]])
print(samrat3)
repeat_array = np.repeat(samrat3,3, axis = 0)
print(repeat_array)

### copying 

# first = np.array([1,2])
# second = first
# second[1]=1000
# print(second)
# print(first) ## i changes to second(variable) it will reflect to the first(variable)

# so we use .copy()
first = np.array([1,2])
second = first.copy()
second[1]=1000
print(second)
print(first)

#### mathematics
# we can do maths in array (basic operations)
# we can do trignometry

#sin in trignometry
trig = [0,1]
print(np.sin(trig))

#cos in trignometry
cos = np.cos(trig)
print(cos)

### we can do all trignometry operations

### ---------------------------------------------------------------------------------------------------------------- ###


### LINEAR ALGEBRA ###

lin = np.ones([5,5])
print(lin)

lin1 = np.full([5,2],10)
print(lin1)

mul = np.matmul(lin,lin1)
print(mul)

### STATISTICS ###

stat = np.array([[11,222,3],[40,5,6]])
print(stat)
#min
print(np.min(stat))
#max
print(np.max(stat))
#sum
print(np.sum(stat))


### Reorganizing array ###

before = ([[1,2,3,4,5,6,7,8,9,0],[100,200]])
print(before)
# ---> it looks like unorganized 

# after = before.reshape((12,1))
# print(after)


### stacking vectors
# --> horizontal stack vector

v1 = np.array([11,22,33,44,55])
v2= np.array([10,20,30,40,50])

horizontal_vector = np.vstack([v1,v2,v1,v2])
print(horizontal_vector)

# --> vertical stack vector
vertical_vector = np.hstack([v1,v2,v1,v2])
print(vertical_vector)


### Miscellanous ###
# --> load data from file

load_data = np.genfromtxt('sample.txt', delimiter=',')
print(load_data)

# print(np.genfromtxt('sample.txt', delimiter=','))

### Boolean masking and advanced indexing
print(load_data > 5) 
# --> it throws the if the numbers are greater than 5 it shows true or otherwise it shows false
print(load_data[load_data > 5])
# --> it throws numbers that are greater than 5

print((~((load_data > 2) & (load_data <5))))




### ----> finished some of the concepts of numpy 💪
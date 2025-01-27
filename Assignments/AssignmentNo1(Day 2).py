# Write a Python program that accepts three lists 
# finds the elements that are unique across all three lists (i.e., appear in only one of the lists). 

'''l1=['mango','orange','Banana','Apple','Blueberry']
l2=['Grapes','orange','Banana','Apple','Coconut']
l3=['mango','Grapes','Apple','Banana','Watermelon']

unique_elements=[]
def unique_element_from_all_list(l1,l2,l3):
    for i in l1:
        if i not in l2 and i not in l3:
            unique_elements.append(i)

    for i in l2:
        if i not in l1 and i not in l3:
            unique_elements.append(i)

    for i in l3:
        if i not in l1 and i not in l2:
            unique_elements.append(i)
unique_element_from_all_list(l1,l2,l3)
print(unique_elements)

# Using Counter
from collections import Counter
list3=l1+l2+l3
ctr=Counter(list3)  # create a dictionary that stores count of each item
# print(ctr)
for item,count in ctr.items():
    if count==1:
        print(item)'''


# Given a list of tuples, group them by their first element and
# create a dictionary where the keys are the first elements, and
# the values are lists of corresponding second elements. 

'''list_of_tuple= [(1, 2), (2, 3), (1, 4), (3, 5), (2, 6)] 
dict1={}  # create a empty dictionary
for i,j in list_of_tuple:  # check the tuple values
    # print(i,j)
    if i not in dict1:  # if value not in dict then create
        dict1[i]=[]
    dict1[i].append(j)  # if the key present the add the value for that key
print(dict1)'''


# Write a program that accepts three lists of integers, merges them into a single list,
# removes duplicates, and sorts the final list in descending order.
'''l1=[1,4,6,7,8,53,56,3]
l2=[34,65,45,12,34,3,6,7,89,90]
l3=[99,34,2,3,6,5,6,7,8,87]
def sorted_list(l1,l2,l3):
    final_list=list(set(l1+l2+l3)) # create a new list and add a unique set values 
    final_list.sort(reverse=True) # sort the new list in descending order
    return final_list
result=sorted_list(l1,l2,l3)
print(result)'''


# Write a Python program to filter tuples from a given list where the 
# sum of the elements in the tuple is greater than a specified threshold. 

'''t1=[(1, 2), (3, 4), (5, 1), (2, 6)]

def specify(t1):
    Threshold = 6
    result=[] # create a empty list
    for i,j in t1:  # check the values in each tuple
        if i+j>Threshold: # check the codition
            result.append((i,j)) # condition =True then append the tuple values in empty list
    return result

result=specify(t1)
print(result)'''

# Develop a program that takes a list of integers and calculates the following statistics using lambda functions: 
    # Mean # Median # Standard deviation 

'''import math
l1=[15,20,25,30,45,60]

n=len(l1)
# print(n)
mean=sum(l1)/n  #mean 
print(f'mean : {round(mean,2)}')

def calculate_median(l1):
    l1.sort()
    n = len(l1)
    if n % 2 == 1:
        return l1[n // 2]
    else:
        return (l1[(n // 2) - 1] + l1[n // 2]) / 2

median = calculate_median(l1)
print(f"The median is: {median}")

variance = sum((i - mean) ** 2 for i in l1) / len(l1)
standard_deviation=math.sqrt(variance) # standard deviation
print(f'Standard Deviation: {round(standard_deviation,2)}')'''

# using inbuild fuctions

import statistics
l1=[15,20,25,30,45,60]
mean_of_list=lambda l1:statistics.mean(l1)
median_of_list=lambda l1:statistics.median(l1)
standard_deviation_of_list=lambda l1:statistics.stdev(l1)

print(f'Mean:{mean_of_list(l1)}')
print(f'Median:{median_of_list(l1)}')
print(f'Standard_Deviation:{standard_deviation_of_list(l1)}')

# Write a Python program to find the longest word(s) in a given list of strings. 
# If there are multiple words with the same maximum length, return them all. 

'''
list1=['apple', 'banana', 'pear', 'blueberry','Rushikesh','om']
max_length=max(len(i) for i in list1)  # calculate the longest length of word in list 
logest_word=[]  # creating empty list
# print(max_length)
for word in list1: # check each word in list
    if len(word)==max_length: # check the condition
        logest_word.append(word) # if condition is true then add to the empty list
print(logest_word)'''


# Write a Python program to count the frequency of each element across all nested lists. 

'''l1= [[1, 2, 3], [2, 3, 4], [3, 4, 5]] 
dict1={}  # created a empty dictionary
for i in l1: # Go inside in the list l1
    for j in i: # check the values in list l1
        if j in dict1: # if value is already present then increase count
            dict1[j]+=1
        else:
            dict1[j]=1 # if value is not  present then set count=1
print(dict1)'''


# Write a program to sort a dictionary by its values in descending order and return the sorted dictionary. 

'''dict1= { 'a': 3, 'b': 5, 'c': 1, 'd': 4 } 
item=list(dict1.items()) # store the key and values in list of tuples 
# print(item)
for i in range(len(item)):
    # print(item)
    for j in range(len(item)-1-i):
        print(item)
        if item[j][1]<item[j+1][1]: # if value is < second value then swap them
            item[j],item[j+1]=item[j+1],item[j]
print(dict(item))'''

# [ 
#   [1], 
#   [1, 1], 
#   [1, 2, 1], 
#   [1, 3, 3, 1], 
#   [1, 4, 6, 4, 1] 
# ] 
'''number=int(input('Enter Number:'))
output=[] # createa empty list
for rows  in range(number): # create a list of number of items
    row=[None for _ in range(rows+1)]
    row[0],row[-1]=1,1 # assign first and last value=1

    for j in range(1,len(row)-1): # for getting the sum of previus values
        row[j]=output[rows-1][j-1]+output[rows-1][j]  # check previous rows values and add sum of two 
    output.append(row) # add the new row in output list
# print(output)
for row in output:
    print(row)'''

#  Write a Python program that accepts a list of strings and transforms it into a list of tuples where: 
# The first element of the tuple is the string in uppercase. 
# The second element is the length of the string. 
# The third element is the reversed string. 
# [('PYTHON', 6, 'nohtyp'), ('DATA', 4, 'atad'), ('SCIENCE', 7, 'ecneics')]
'''list1=['python','data','science']
l1=[]
def reverse(i):
    reversed_str=''
    for char in i:
        reversed_str=char+reversed_str
    return reversed_str

for i in list1:
    l1.append((i.upper(),len(i),reverse(i)))
print(l1)'''
    


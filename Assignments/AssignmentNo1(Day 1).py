# 1. Remove all occurrences of a specific value from list 

# Basic
'''list1=[]
a=int(input('Enter how many values you want to insert:'))
for i in range(a):
    value=input(f'Insert Value {i+1}:')
    list1.append(value)
print(list1)

# To delete all occurences
removed_name=input('Enter value you want to remove:')

for i in list1:
    list1.remove(removed_name)

print(list1)'''


# Using Function
'''list1=[]
def inputs_for_list(): # adding list items through users
    num=int(input('Enter how many values you want to insert:'))
    for i in range(num):
        value=input(f'insert value{i+1}:')
        list1.append(value)
    return list1
inputs_for_list()

name=input('Enter value you want to remove :')
def delete_all_occurenses(name): # to delete all occurenses from list
    for i in list1:
        list1.remove(name)
    return list1
print(delete_all_occurenses(name))'''


# 2. Find intersection of two list

# Basic
'''l1=['Mango','Orange',1,3,'Banana','Red','Green']
l2=['Orange','Grapes',3,'Purple','Blue']
l3=[]

# using For loop
for i in l1:
    if i in l2:
        l3.append(i)
print(l3)

# using logical operator
print(list(set(l1)&set(l2))) 

# using set intersection method
print(list((set(l1)).intersection(set(l2))))'''


# Function

'''l1=['Mango','Orange',1,3,'Banana','Red','Green']
l2=['Orange','Grapes',3,'Purple','Blue']

def intersection_of_list(l1,l2):
    return list(set(l1).intersection(set(l2))) # convert list into set and use intersection method

print(intersection_of_list(l1,l2))
'''

# 3 Get Smallest and Largest number from list

# Basic
'''number_list=[28,76,56,67,43,12,36,89,99]
number_list.sort()
print(number_list)
print('Smallest number is: ',number_list[0])
print('Largest number is :',number_list[-1])'''

# using built in libraries
'''number_list=[28,76,56,67,43,12,36,89,99]
minimum_number=min(number_list)
maximum_number=max(number_list)
print(f'Minimun Number : {minimum_number}')
print(f'Maximum Number : {maximum_number}')'''

# function

'''number_list=[28,76,56,67,43,12,36,89,99]
def small_and_large_number(list_of_numbers):
    list_of_numbers.sort()  # sort the function in ascending order
    return  print(f'Smallest Number :{number_list[0]} \nGreatest Number:{number_list[-1]}')
small_and_large_number(number_list)'''





# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples 

Sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)] 

# Expected output = [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)] 

# using sorted function
'''result=sorted(Sample_list , key=lambda x:x[1])
print(result)'''


# using looping condition
'''sorted_list=[]
while Sample_list:
    min_tuple=Sample_list[0]
    for i in Sample_list:
        if i[-1]<min_tuple[-1]:
            min_tuple=i
    sorted_list.append(min_tuple)
    Sample_list.remove(min_tuple)
print(sorted_list)
'''

# using Bubble Sort

'''Sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)] 
n = len(Sample_list)

for i in range(n):
    for j in range(0, n-i-1):
        if Sample_list[j][-1] > Sample_list[j+1][-1]:
            Sample_list[j], Sample_list[j+1] = Sample_list[j+1], Sample_list[j]

print("Sorted list:", Sample_list)'''


# 5. start pattern

# 1 
# Basic
'''n=int(input('Enter number:'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=' ')
    print(' ')
for i in range(n+1):
    for j in range(n-i+1):
        print("*",end=' ')
    print(' ')'''

# function
'''n=int(input('Enter number:'))
def start_pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end=' ')
        print(' ')
    for i in range(n+1):
        for j in range(n-i+1):
            print("*",end=' ')
        print(' ')
start_pattern(n)'''


# 2
# Pyramid Pattern
'''n=int(input('Enter Number'))
for i in range(n):
    for j in range(n-i-1):  # loop for printing spaces
        print(' ',end=' ')
    for k in range(2*i-1): # loop for printing stars
        print('*',end=' ')
    print()
'''

'''n=int(input('Enter Number : '))
for i in range(n,0,-1):
    for j in range(n-i):
        print(' ',end='')
    for k in range(2*i-1):
        print('*',end='')
    print()'''


# 6.
def add_student(): # To add student information
    student_data=[]
    number=int(input('Enter number of student you want to enter:'))
    for _ in range(number):
        name=input('Enter Student Name:')
        exam1=int(input('Marks of exam 1:'))
        exam2=int(input('Marks of exam 2:'))
        exam3=int(input('Marks of exam 3:'))
        cal_average=lambda e1,e2,e3:(e1+e2+e3)/3    # calculate average using lambda function
        average=cal_average(exam1,exam2,exam3)

        grade=calculate_grade(average) # calculating average by calling calculate_grade function
        
        student={
            'Name':name,
            'Exam 1':exam1,
            'Exam 2':exam2,
            'Exam 3':exam3,
            'Average':round(average,2),
            'Grade':grade,
        }
        student_data.append(student) # adding each student separately
    print("\nStudent Data:")
    print(f"{'Name':<20} {'Exam 1':<10} {'Exam 2':<10} {'Exam 3':<10} {'Average':<10} {'Grade':<5}")

    for student in student_data:
        print(f"{student['Name']:<20} {student['Exam 1']:<10} {student['Exam 2']:<10} {student['Exam 3']:<10} {student['Average']:<10.2f} {student['Grade']:<5}")

def calculate_grade(average): # To calculate grade from the average
    if average>=90:
        return 'A'
    elif average>=80 and average<90:
        return 'B'

    elif average>=70 and average<80:
        return 'C'
    elif average>=60 and average<70:
        return 'D'
    else:
        return 'F'
    
def main_function(): # main function 
    add_student()
    
main_function() # calling main function

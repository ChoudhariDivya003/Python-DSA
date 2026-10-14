'''
SORTING ALGORITHM
-------------

1.BUBBLE SORT:
-->is a part of sorting algo. Here we are sorting element by element
compare next and current element and condition is true then swap
condition not satisfied ignore that step
-working on n-1 principle

In bubble sort we are getting unsorted elements and we need to sort them 

'''
x=[10,15,13,27,4]

'''
internally memory is arranged in the form of :
    0    1     2    3   4
    ______________________
   | 10 | 15 | 13 | 27 |4 |
   |______________________|

   x[0]>x[1]-->10>15-->False---->completed

   x[1]>x[2]--->15>13--->True 
   Then swap the elements--->x[1]=13
                             x[2]=15
    
    Updated list---> | 10 | 13 | 15 | 27 | 4 |
                       0    1    2    3   4

    x[2]>x[3]-->15>27--->False-->skip

    x[3]>x[4]-->27>4--->True
    swap--->x[4]=27
            s[3]=4

    updated list--> | 10 | 13 | 15 | 4 | 27 |
                      0     1   2    3   4
This is 1st iteration and last element is sorted 
pass 1


In the 2nd iteration:
x[0]>x[1]-->10>13--->false

x[1]>x[2]-->13>15-->false

x[2]>x[3]-->15>4-->true
swap x[2]=4, x[3]=15

updated list : | 10 | 13 | 4 | 15 | 27 |

pass 2

iteration3:
x[0]>x[1]-->10>13-->false

x[1]>x[2]-->13>4-->true 
swap x[1]=4, x[2]=13

updated list--> 10  4  13 15 27
pass3

iteration4:
x[0]>x[1]-->10>4-->true 
swap-->x[0]=4, x[1]=10

updated--> | 4 | 10 | 13 | 15 | 27 |

pass 4


'''
x=[10,15,13,27,4]
for i in range(len(x)-1):       #getting position of the elment
    if x[i]>x[i+1]:
        x[i],x[i+1]=x[i+1],x[i]
print("First pass",x)
# First pass [10, 13, 15, 4, 27]
print()

for i in range(len(x)-2):       #getting position of the elment
    if x[i]>x[i+1]:
        x[i],x[i+1]=x[i+1],x[i]
print("second pass",x)
# second pass [10, 13, 4, 15, 27]

print()


for i in range(len(x)-3):       #getting position of the elment
    if x[i]>x[i+1]:
        x[i],x[i+1]=x[i+1],x[i]
print("Third pass",x)
# Third pass [10, 4, 13, 15, 27]
print()

for i in range(len(x)-4):       #getting position of the elment
    if x[i]>x[i+1]:
        x[i],x[i+1]=x[i+1],x[i]
print("Fourth pass",x)
# Fourth pass [4, 10, 13, 15, 27]--->sorted list

print("-----------------------")

# at a time output in one code --->nested for loop
# ascending to descending
for i in range(len(x)):
    for j in range(len(x)-1-i):
        if x[j]>x[j+1]:
            x[j],x[j+1]=x[j+1],x[j]
print("sorted list-asc",x)

# o/p--->sorted list [4, 10, 13, 15, 27]
print()

# descending to ascending
for i in range(len(x)):
    for j in range(len(x)-1-i):
        if x[j]<x[j+1]:
            x[j],x[j+1]=x[j+1],x[j]
print("sorted list-desc",x)

# sorted list-desc [27, 15, 13, 10, 4]
print()

#ex2
d=[45,12,10,16,7,19,90]
# asc
for i in range(len(d)):
    for j in range(len(d)-1-i):
        if d[j]>d[j+1]:
            d[j],d[j+1]=d[j+1],d[j]
print("sorted asc-list",d)
# sorted asc-list [7, 10, 12, 16, 19, 45, 90]
print()

# desc
for i in range(len(d)):
    for j in range(len(d)-1-i):
        if d[j]<d[j+1]:
            d[j],d[j+1]=d[j+1],d[j]
print("sorted desc-list",d)
# sorted desc-list [90, 45, 19, 16, 12, 10, 7]
print()

# pass wise output
d=[45,12,10,16,7,19,90]
for i in range(len(d)-1):
    if d[i]>d[i+1]:
        d[i],d[i+1]=d[i+1],d[i]
print("first pass-->",d)
# first pass--> [45, 19, 16, 12, 10, 7, 90]

print()

for i in range(len(d)-2):
    if d[i]>d[i+1]:
        d[i],d[i+1]=d[i+1],d[i]
print("second pass-->",d)
# second pass--> [10, 12, 7, 16, 19, 45, 90]
print()

for i in range(len(d)-3):
    if d[i]>d[i+1]:
        d[i],d[i+1]=d[i+1],d[i]
print("Third pass-->",d)
# Third pass--> [10, 7, 12, 16, 19, 45, 90]
print()

for i in range(len(d)-4):
    if d[i]>d[i+1]:
        d[i],d[i+1]=d[i+1],d[i]
print("Fourth pass-->",d)
# Fourth pass--> [7, 10, 12, 16, 19, 45, 90]
print("---------------")

#Sort String List
arr=["Banana","Apple","Orange","Mango"]
for i in range(len(arr)):
    for j in range(len(arr)-1-i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)
# o.p--->['Apple', 'Banana', 'Mango', 'Orange']


#Sort Floating Numbers
s=[2.5,1.1,4.6,0.8]
for i in range(len(s)):
    for j in range(len(s)-1-i):
        if s[j]>s[j+1]:
            s[j],s[j+1]=s[j+1],s[j]
print(s)
# o/p-->[0.8, 1.1, 2.5, 4.6]
print()


#Bubble Sort using Function
marks=[45,90,78,35,65]
def Sort_marks(marks):
    for i in range(len(marks)):
        for j in range(len(marks)-1-i):
            if marks[j]>marks[j+1]:
                marks[j],marks[j+1]=marks[j+1],marks[j]
    print(marks)
Sort_marks([45,90,78,35,65])
# o.p--->[35, 45, 65, 78, 90]
print()

#Count the Number of Swaps
a= [5, 2, 8, 1, 9]
swap=0
comp=0
for i in range(len(a)):
    for j in range(len(a)-1-i):
        comp+=1
        if a[j]>a[j+1]:
            swap+=1
            a[j],a[j+1]=a[j+1],a[j]
            
print(a)
print("No. of comparisons--->",comp)
print("Total Swap-->",swap)

# [1, 2, 5, 8, 9]
# No. of comparisons---> 10
# Total Swap--> 4
print("--------")

#Count the Number of Comparisons
a1= [5, 2, 8, 1, 9] 
comp=0
for i in range(len(a1)):
    for j in range(len(a1)-1-i):
        comp+=1
        if a1[j]>a1[j+1]:
            a1[j],a1[j+1]=a1[j+1],a1[j]
print(a1)
print(comp)

# o/p-->[1, 2, 5, 8, 9]
        #  10


# In bubble sort we are making unsorted to sorted 






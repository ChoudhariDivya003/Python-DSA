'''
MERGE SORT
-------------

Works on divide and conquer rule.
We will divide the collection/array until we will get the single single elements 
Then after, we will merge this elements 


'''


'''
Ex1:
x=[1,8,7,5,18,3]
   0 1 2 3  4 5

   li=0,hi=5
Find mid-->(li+hi)//2
-->mid=(0+5)//2=5//2=2
mid=2
x[mid]-->7

left hand side-->positions-->0,1,2
Right hand side-->positions-->3,4,5

i.e-->LHS-->li-mid
      RHS-->mid+1 to hi

                   ________________________
                  | 1 | 8 | 7 | 5 | 18 | 3 |
                   ________________________
                              /\\

              0   1   2                       0    1   2   
              __________                     ___________           
            | 1 | 8 | 7 |                   | 5 | 18 | 3|
             ___________                     ___________

            mid=0+2//2=1                     mid=0+2 //2-->1
                 /\\                           / \\
     _______           ___              ______      __
    | 1 | 8 |         | 7 |            |5 | 18|    |3 |
     _______           ___              ______      __
    mid-->0+1 //2                       mid=0+1//2
    mid=0                                mid=0
       /\\                                 /\\
 ___       ___                       ___      ____
| 1 |     | 8 |                     | 5 |    | 18 |
 ___       ___                       ___      ____

 Divide done
 -------------------------------------------------------------
 
Conquer-->
Left                         Right            
--------------------------------------------------------
1>8-->false             5>18-->False
[1,8]                    [5,18]

now,
[1,8][7]                 [5,18] [3]
1>7-->false               5>3-->True swap 5 and 3
8>7-->true                [3,18][5]
swap 8 and 7              3>5-->false
                          18>5--true
[1,7,8]                   swap 18 and 5
therefore LHS sorted      [3,5,18]-->RHS sorted

LHS + RHS--->[1,7,8] + [3,5,18]

For intialization part 
we have 3 list

original list-->x=[1,8,7,5,18,3]
                k->0

Left-->left=[1,7,8]
             0 1 2
       i=0

Right-->right=[3,5,18]
               0 1  2
       j=0

check the condition:
if i<len(left) and j<len(right)
if -->0<3 and 0<3 -->True
If True-->
then check
        if left[i]<right[j]
        1<3--true

        x[k]=left[i]
        k=k+1  -->k=0+1
        i=i+1  -->i=0+1


if i<len(left) and j<len(right)
1<3 and 0<3-->true
check
        if left[i]<right[j]
        7<3-->False
        x[k]=right[j]
        8<=3
        k=k+1
        i=i+1

if i<len(left) and j<len(right)
1<3 and 1<3 --True
        if left[i]<right[j]
        7<5 --->False
        x[k]=right[j]
        k=k+1
        j=j+1

if i<len(left) and j<len(right)
1<3 and 2<3 
        if left[i]<right[j]
        7<18-->True
        x[k]=left[i]
        k=k+1
        i=i+1--->1+1=2

if i<len(left) and j<len(right)
2<3 and 2<3--True
        if left[i]<right[j]
        8<18 ---True
        x[k]=left[i]
        k=k+1
        i=i+1

if i<len(left) and j<len(right)
3<3 and 2<3 --False

Now check only right side
j<len(right)
2<3-->true
x[k]=right[j]
k=k+1
j=j+1

x=[1,2,3,5,7,8,18]


''' 
#ex1
x=[1,8,7,5,18,3]
# def Divide(x,li,hi):
#     if li>=hi:               #once you got single element we need to stop(li>=hi)
#         return 
#     mid=(li+hi)//2
#     left=x[li:mid+1:]
#     right=x[mid+1::]
#     print(left,right)
#     Divide(left,0,len(left)-1)
#     Divide(right,0,len(right)-1)
# Divide(x,0,len(x)-1)
# o/p-->
# [1, 8, 7] [5, 18, 3]
# [1, 8] [7]
# [1] [8]
# [5, 18] [3]
# [5] [18]
print("---------")

#ex
x=[1,8,7,5,18,3]

def Divide(x,li,hi):
    if li>=hi:               #once you got single element we need to stop(li>=hi)
        return 
    mid=(li+hi)//2
    left=x[li:mid+1:]
    right=x[mid+1::]
    print(left,right)
    Divide(left,0,len(left)-1)
    Divide(right,0,len(right)-1)
    # Merge(x,left,right)
# Divide(x,0,len(x)-1)

def Merge(x,L,R):
    k=0    
    i=0
    j=0

    while i<len(L) and j<len(R):
        if L[i]<R[j]:
            x[k]=L[i]
            i=i+1
            k=k+1
        else:
            x[k]=R[j]
            k=k+1
            j=j+1

    while i<len(L):
        x[k]=L[i]
        i=i+1
        k=k+1
    while j<len(R):
        x[k]=R[j]
        j=j+1
        k=k+1
Merge(x,[1,8,7],[5,18,3])
Divide(x,0,len(x)-1)
print(x)

# o/p--->
# [1, 5, 8] [7, 18, 3]
# [1, 5] [8]
# [1] [5]
# [7, 18] [3]
# [7] [18]
# [1, 5, 8, 7, 18, 3]
print("--------")

#EX
# x=[30,20,7,17,31,4,1]
# def Divide(x,low,high):
#         if low>=high:
#                 return
#         mid=(low+high)//2
#         left=x[low:mid+1]
#         right=x[mid+1:high+1]
#         print("-------------->")
#         print("Dividing the data ")
#         print("left part",left)
#         print("right part",right)
#         Divide(x,low,mid)     #Divide(left,0,len(left)-1)
#         Divide(x,mid+1,high)
# print("original array--->",x)
# Divide(x,0,len(x)-1)

# o/p-->
# original array---> [30, 20, 7, 17, 31, 4, 1]
# -------------->
# Dividing the data 
# left part [30, 20, 7, 17]
# right part [31, 4, 1]
# -------------->
# Dividing the data 
# left part [30, 20]
# right part [7, 17]
# -------------->
# Dividing the data 
# left part [30]
# right part [20]
# -------------->
# Dividing the data 
# left part [7]
# right part [17]
# -------------->
# Dividing the data 
# left part [31, 4]
# right part [1]
# -------------->
# Dividing the data 
# left part [31]
# right part [4]
print("-----------------------")
'''
#ex
x=[30,20,7,17,31,4,1]
def Merge(x,low,mid,high):
    left=x[low:mid+1]
    right=x[mid+1:high+1]
    print("\n--------")
    print("before merging--->")
    print("Left part",left)
    print("Right part-->",right)
    i=0
    j=0
    k=low
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            x[k]=left[i]
            k=k+1
            i=i+1
        else:
            x[k]=right[j]
            k=k+1
            j=j+1

        while i<len(left):
            x[k]=left[i]
            k=k+1
            i=i+1

        while j<len(right):
            x[k]=right[j]
            k=k+1
            j=j+1

        print("Merging list-->",x[low:high+1:1])
            
def Divide(x,low,high):
        if low>=high:
                return
        mid=(low+high)//2
        left=x[low:mid+1]
        right=x[mid+1:high+1]
        print("-------------->")
        print("Dividing the data ")
        print("left part",left)
        print("right part",right)
        Divide(x,low,mid)     #Divide(left,0,len(left)-1)
        Divide(x,mid+1,high)
        Merge(x,low,mid,high)
        print(x)
print("original array--->",x)
Divide(x,0,len(x)-1)
print("final array-->",x)
'''

x=[30,20,7,17,31,4,1]
def Merge(x,low,mid,high):
    left = x[low:mid + 1]
    right = x[mid + 1:high + 1]
    print("\n--------------------->>>")
    print("Before Mergeing")
    print("LEFT---PART", left)
    print("RIGHT---PART", right)
    i=0
    j=0
    k=low
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            x[k]=left[i]
            k=k+1
            i=i+1
        else:
            x[k]=right[j]
            k=k+1
            j=j+1

    while i<len(left):
        x[k]=left[i]
        k=k+1
        i=i+1

    while j<len(right):
        x[k]=right[j]
        k=k+1
        j=j+1
    print("Merging List----->",x[low:high+1:1])
def Divide(x,low,high):
    if low>=high:
        return
    mid=(low+high)//2
    left=x[low:mid+1]
    right=x[mid+1:high+1]
    print("\n--------------------->>>")
    print("dividing_The_Data")
    print("LEFT---PART",left)
    print("RIGHT---PART",right)
    Divide(x,low,mid) #Divide(left,0,len(left)-1)
    Divide(x,mid+1,high)#Divide(right,0,len(right)-1)
    Merge(x,low,mid,high)
print("Orginal Array---->")
print(x)
Divide(x,0,len(x)-1)
print("Final sorted array----->")
print(x)
print("---------------------------")

x=[30,20,7,17,31,4,1]
def Merge(x,left,right):
    k=0
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            x[k]=left[i]
            k=k+1
            i=i+1
        else:
            x[k]=right[j]
            k=k+1
            j=j+1
    while i<len(left):
        x[k]=left[i]
        k=k+1
        i=i+1

    while j<len(right):
        x[k]=right[j]
        k=k+1
        j=j+1
def Divide(x,low,high):
    if low>=high:
        return
    mid=(low+high)//2
    left=x[:mid+1]
    right=x[mid+1::]
    print(left,right)
    Divide(left,0,len(left)-1)
    Divide(right,0,len(right)-1)
    Merge(x,left,right)
Divide(x,0,len(x)-1)
print("final data",x)
print("---------------------------")


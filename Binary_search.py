'''
2.BINARY SEARCH ALGORITHM
-------------------------

Time complexity of Binary search--->
1. Best: o(1)
2. Average: o(Log(n))
3. Worst : o(Log(n))

So to reduce the comparison we use binary search algo.
-Always we need to pass sorted data

While we are doing binary search, it will divide the data in two parts-->
left part and right part


so that comparison will be easy and reduced
Code Efficiency will be increased

Steps to use binary--->
STEP 1] consider the collection and key to check
STEP 2] Initialize the least Index as 0 and highest index as len(collection)-1
STEP 3] least index <= Highest index or not
STEP 4] calculate mid index using mid=(LeastIndex+HighestIndex)//2 formula
STEP 5] Check whether key==col[mid] 
        if True--->return mid
        elif check key>col[mid] if True-->change leastIndex=Mid+1
        else check key<col[mid] if True change HigestIndex=mid-1

STEP 6] Repeat all the points from 3 tp 5 until you get index of key


Ex-->
x=[10,20,30,40,50,60,70,80]
key=60

Internally data is arranged in the form of:
least index
  |
  0    1   2    3    4   5   6    7 --->highest index=len(col)-1=8-1==7
 ____________________________________
| 10 | 20| 30 | 40 |50 |60 | 70 | 80 |
 ____________________________________
               mid


 check -->least index<= highest index--->if true 
          0<=7  --->True

 Find mid--->(Li+Hi)//2--->0+7//2=7//2-->3
    x[3]-->40

 Check, if key==x[mid]--->60==40--->False
  
 Then, elif key>col[mid]--->60>40--->True
       So change li=mid+1--->li= 3+1 = 4--->li=4
       --->x[4]=50

 Now, li=4 and hi=7
     find the mid index--> mid=(li+hi)//2
                           mid=(4+7)//2-->11//2-->2
                           mid=5
                           x[mid]=60
    
     Again check key==col[mid]--->key==x[5]
                                  60==60---->True
    
    60 element is searched at mid value 5
    so output should be 5

'''

# x=[10,20,30,40,50,60,70,80]
# key=60
def Binary_search(x,key):   #declaration
    li=0                    #li=0
    hi=len(x)-1             #hi=7
    while li<=hi:  #true
        mid=(li+hi)//2      #mid=7//2==3               
        if key==x[mid]:     #60==40-->False
            return mid
        elif key>x[mid]:   #60>40                       
            li=mid+1       #li=3+1=4-->50==60 False   li=4+1=5-->x[mid]=60-->60==60 True
        else:
            hi=mid-1
    return "Element not found"
print(Binary_search([10,20,30,40,50,60,70,80],60))   #5
print()

#ex2 
x=[1,2,3,4,5,6,7]
key=3

'''
    0   1   2   3   4   5   6
   ___________________________
  | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
   __________________________
   li=0                     hi=6

   mid=(li+hi)//2-->6//2-->3

   check if x[mid]==key-->x[3]==3
                         4==3-->False
    
        elif key<x[mid]--->3<4-->True
            change hi= mid-1-->3-1= 2
                        hi=2
            
            again check, li<=hi-->0<=2--->True
            
            check mid--->mid=(li+hi)//2-->2//2=1

            if key==x[mid]-->3==2-->False
            elif key>x[mid]-->3>2-->True
                            change li=mid+1
                            li= 1+1= 2
                        
            li=2,hi=2
            check li<=hi-->2<=2
                          
                      check if key==x[mid]
                                3==3--->True
                                mid position was 2

'''
def Binary_search(x,key):   #declaration
    li=0                    #li=0
    hi=len(x)-1             #hi=6
    while li<=hi:  #true
        mid=(li+hi)//2      #mid=6//2==3               
        if key==x[mid]:     #3==4-->False
            return mid
        elif key>x[mid]:                        
            li=mid+1       
        else:
            hi=mid-1
    return "Element not found"
print(Binary_search([1,2,3,4,5,6,7],3))   #2
print()

#ex3
d=[100,150,200,250,300,350]
key=200

def Binary_search(d,key):
    li=0
    hi=len(d)-1
    while li<=hi:
        mid=(li+hi)//2
        if key==d[mid]:
            return mid
        elif key>d[mid]:
            li=mid+1
        else:
            hi=mid-1
    return -1
print(Binary_search(d,200))   #2
print()

#ex 4-->finding 1st,2nd 3rd occurance of the duplicate elements
# 1. find 1st occurance
x=[10,20,20,20,30,40,50]
key=20

'''
internally memory is arrange in the form of :
    0    1   2     3     4    5    6    
   __________________________________
  | 10 | 20 | 20 | 20 | 30 | 40 | 50 | 
  |__________________________________|
      left         mid      right
---------------------------------------------------
li-->0   hi--->6   first=-1
if li<=hi--->0<=6--->True
 mid=(0+6)//2-->3
 mid=3--->mid value position
---------------------------------------------------
                centre(mid)
                    /   \
            left              right
positions->| 0 | 1 |2|      |4 |5|6|

 NOTE: always we have to find out least index position
-----------------------------------------------------------------
 if key==d[mid]
    20==20   True
   then, first=3
         hi=3-1= 2
                           mid
          | 10 | 20 | 20 | 20 | 30 | 40 | 50 |
                      hi

------------------------------------------------------  
    li<=2--->0<=2  True
    mid=(0+2)//2=1
               
                _____________
               | 10 | 20 | 20|
               | ___________ |
                li    mid  hi
--------------------------------------------
    if key==x[mid]
      20==20   True
      mid=1--->output

'''

def Searching_firstoccurance(x,key):   #declaration
    li=0
    hi=len(x)-1
    first=-1    #if specified element is not present automatically it will display -1
                #and if element is present then the element position will be stored in first variable
    while li<=hi:
        mid=(li+hi)//2
        if key==x[mid]:
            first=mid        #storing the mid value position into first variable
            hi=mid-1
        elif key>x[mid]:
            li=mid+1
        else:
            hi=mid-1
    return first
print(Searching_firstoccurance(x,20))   #1
print(Searching_firstoccurance(x,200))   #-1   -->if element is not present
print()

#2. finding last occurance
x=[10,20,20,20,30,40,50]
key=20
def Searching_lastoccurance(x,key):   #declaration
    li=0
    hi=len(x)-1
    first=-1    #if specified element is not present automatically it will display -1
                #and if element is present then the element position will be stored in first variable
    while li<=hi:
        mid=(li+hi)//2
        if key==x[mid]:
            first=mid        #storing the mid value position into first variable
            hi=mid-1         #first occurance element
            li=mid+1         #last occurance   element
        elif key>x[mid]:
            li=mid+1
        else:
            hi=mid-1
    return first
print(Searching_lastoccurance(x,20))   #3
print()

#3. finding 2nd occurance element position
first =Searching_firstoccurance(x,key)
print("First occurance value:",first)   #First occurance value: 1

if first!=-1 and first+1<len(x) and x[first+1]==key:
    print("Second occurance value-->",first+1)   #Second occurance value--> 2

print()

#ex5
r=(2,5,8,10,99,105,105,105,200)
key=105

'''

'''

#1. first occurance
def First_occurance(r,key):
    li=0
    hi=len(r)-1
    first=-1
    while li<=hi:
        mid=(li+hi)//2
        if key==r[mid]:
            first=mid
            hi=mid-1
        elif key>r[mid]:
            li=mid+1
        else:
            hi=mid-1
    return first
print(First_occurance(r,105))   #5
print()

#2. last occurance
r=(2,5,8,10,99,105,105,105,200)
key=105
def Last_occurance(r,key):
    li=0
    hi=len(r)-1
    last=-1
    while li<=hi:
        mid=(li+hi)//2
        if key==r[mid]:
            last=mid
            hi=mid-1
            li=mid+1
        elif key>r[mid]:
            li=mid+1
        else:
            hi=mid-1
    return last
print(Last_occurance(r,105))   #6
print()

#3. 2nd occurance of 105
first=First_occurance(r,key)
print("first occurance-->",first)

if first!=-1 and first+1<len(r) and r[first+1]==key:
    print("second occurance",first+1)

print("-----------------------------")

#examples

a=[11,12,13,14,15]
key=14
def First_occ(a,key):
    li=0
    hi=len(a)-1
    while li<=hi:
        mid=(li+hi)//2
        if key==a[mid]:
            return mid
        elif key>a[mid]:
            li=mid+1
        else:
            hi=mid-1
print(First_occ(a,14))  #3
print()

b=[10,20,30,30,30,40]
key=30
#first occ
def first_occ(b,key):
    li=0
    hi=len(b)-1
    first=-1
    while li<=hi:
        mid=(li+hi)//2
        if key==b[mid]:
            first=mid
            hi=mid-1
        elif key> b[mid]:
            li=mid+1
        else:
            hi=mid-1
    return first 
print(first_occ([10,20,30,30,40],30))   #2

print()

#last occurance
b=[10,20,30,30,30,40]
key=30
def Second(b,key):
    li=0
    hi=len(b)-1
    last=-1
    while li<=hi:
        mid=(li+hi)//2
        if key==b[mid]:
            last=mid
            # hi=mid-1
            li=mid+1
        elif key> b[mid]:
            li=mid+1
        else:
            hi=mid-1
    return last
print(Second([10,20,30,30,30,40],30))   #4
print()

data=first_occ(b,key)
print(data)  #2

if first!=-1 and first+1 <len(b) and b[first+1]==key:
    print("second occurance-->",first+1)
else:
    print("not found")

print("-----------------")

#ex
y=[20,40,40,40,50,60]
key=40
'''
#last occurance
def Searching_Data(y,key):
    li=0
    hi=len(y)-1
    last=-1
    while li<=hi:
        mid=(li+hi)//2
        if key==y[mid]:
            last=mid
            # hi=mid-1
            li=mid+1
        elif key>y[mid]:
            li=mid+1
        else:
            hi=mid-1
    return last
print(Searching_Data(y,40))   #3
print(Searching_Data(y,404))   #-1
print()

#first occurance
def Searching_Data(y,key):
    li=0
    hi=len(y)-1
    last=-1
    while li<=hi:
        mid=(li+hi)//2
        if key==y[mid]:
            last=mid
            hi=mid-1
            # li=mid+1
        elif key>y[mid]:
            li=mid+1
        else:
            hi=mid-1
    return last
print(Searching_Data(y,40))   #1
# print(Searching_Data(y,404))   #-1
print()


# finding nth element
def Nth_element(y,key,n):
    if n<=0:      #if the element is not present
        return -1
    first=Searching_Data(y,key)   #1th position..1st occ data 
    position=first+(n-1)          #position-->index no.= first_occ_value+(n-1)
    if first!=-1 and 0<=position<len(y) and y[position]==key:
        return position
    return -1
print("0th element-->",Nth_element(y,40,0))
print("1th element-->",Nth_element(y,40,1))
print("2nd element-->",Nth_element(y,40,2))
print("3rd element-->",Nth_element(y,40,3))
print("4th element-->",Nth_element(y,40,4))
print("5th element-->",Nth_element(y,40,5))

# 0th element--> -1
# 1th element--> 1
# 2nd element--> 2
# 3rd element--> 3
# 4th element--> -1
# 5th element--> -1
print("--------")

'''
'''
position-->first+(n-1)
           1+(0-1)=1-1=0-->10 not present --> -1
           1+(1-1)=1--->40-->present 1
           1+(2-1)=1+1=2-->40--->present-->2
           1+(3-1)=1+2=3-->40-->present --->3
           1+(4-1)=1+3=4-->50--->not present --->-1
           1+(5-1)=1+4=5-->60-->not present --->-1

'''

y=[20,40,40,40,50,60]
key=40
#TOTAL COUNT
def Searching_Data(y,key):
    li=0
    hi=len(y)-1
    first=-1
    while li<=hi:
        mid=(li+hi)//2
        if key==y[mid]:
            first=mid
            hi=mid-1
            # li=mid+1
        elif key>y[mid]:
            li=mid+1
        else:
            hi=mid-1
    return first
print(Searching_Data(y,40))   #1
# print(Searching_Data(y,404))   #-1
print()

def Searching_Data2(y,key):
    li=0
    hi=len(y)-1
    last=-1
    while li<=hi:
        mid=(li+hi)//2
        if key==y[mid]:
            last=mid
            # hi=mid-1
            li=mid+1
        elif key>y[mid]:
            li=mid+1
        else:
            hi=mid-1
    return last
print(Searching_Data2(y,40))   #3
print()

def Total_occ(y,key):
    first=Searching_Data(y,key)
    if first==-1:
        return 0
    
    last=Searching_Data2(y,key)
    total=last-first+1
    return total
print(Total_occ(y,40))  #3
print()

#ex
s=[10,10,10,10,10,20,30,40]
#  0  1  2   3  4  5  6  7
key=10

#first occ_
def One(s,key):
    li=0
    hi=len(s)-1
    first=-1
    while li<=hi:
        mid=(li+hi)//2
        if key==s[mid]:
            first=mid
            hi=mid-1
        elif key> s[mid]:
            li=mid+1
        else:
            hi=mid-1
    return first
print("1st occurance in s--->")
print(One(s,10)) 

# 1st occurance in s--->
# 0
print()

#last occ
def Last(s,key):
    li=0
    hi=len(s)-1
    last=-1
    while li<=hi:
        mid=(li+hi)//2
        if key==s[mid]:
            last=mid
            li=mid+1
        elif key>s[mid]:
            li=mid+1
        else:
            hi=mid-1
    return last
print("last occurance of 10")
print(Last(s,10))

# last occurance of 10
# 4
print()

#second occ
ele=One(s,key)
print(ele)  #0

if ele!=-1 and ele+1<len(s) and s[ele+1]==key:
    print("second occ--->",ele+1)

#second occ---> 1
print("-------")

#Nth occurance
def Nth_occ(s,key,n):
    if n<0:
        return -1
    
    first=One(s,key)
    if first==-1:
        return -1
    
    pos=first+(n)
    if first != -1 and 0 <= pos < len(s) and s[pos] == key:
        return pos
    return -1
print("0th position-->",Nth_occ(s,10,0))
print("1th position-->",Nth_occ(s,10,1))
print("2nd position-->",Nth_occ(s,10,2))
print("3rd position-->",Nth_occ(s,10,3))

# 0th position--> 0
# 1th position--> 1
# 2nd position--> 2
# 3rd position--> 3
print("------------")

def Total_count(s,key):
    first=One(s,key)
    if first==-1:
        return 0
    
    last=Last(s,key)
    total=last-first+1
    return total
print("Total count of 10 element--->")
print(Total_count(s,key))  #5
print("------------------")

'''
Important question in binary search
-----------------------------------
1. 1st occurance
2. last occurance
3. 2nd occurance
4. Nth occurance
5. Total count

'''




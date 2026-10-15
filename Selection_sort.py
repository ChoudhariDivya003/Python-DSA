'''
2. SELECTION SORT
------------------
We can sort the collection by the help of assumed element
it will work for small arrays
we can reduce comparisons here
where condition satisfied we need to change assusmed position and compare with the remaining elements 
and the swap the previous and current assumed position.

-We need to consider one assumed position... always we need to take it as 0th position

steps----------->
consider a collection
idetify assumed position(known as minimum pos)
compare assumed pos with all the element
once condition becomes true then change assumed position value
compare the updated assumed value with the remaining positions
Then swap the previous assumed position with the current assumed position
Repeat the comparison steps until we get the sorted list.
'''

#ex1--->selected sort displaying one one iteration
# x=[3,7,10,1,2]
# minp=0
# for i in range(1,len(x)):
#     if x[minp]>x[i]:
#         minp=i
# # swap
# x[minp],x[i]=x[i],x[minp]
# print(x)
        
'''
Ex1:
x=[3,7,10,1,2]

internally-->
    0   1   2    3   4
    ____________________
   | 3 | 7 | 10 | 1 | 2 |
    ___________________

consider assumed position--->x[0]-->3

if x[0]>x[1]-->3>7-->False
if x[0]>x[2]--->3>10-->False
if x[0]>x[3]-->3>1-->True
Then, change assumed position value

so, assumed pos value--->x[3]-->1

check 
  if x[3]>x[4]-->1>2-->False
Now, swap previous assumed position with current assumed position
swap(x[0],x[3])

updated list-->  | 1 | 7 | 10 | 3 | 2 |
                   0   1   2    3   4
     here 1st (one) element gets sorted
     Now consider assumed pos-->x[1]-->7
    
if x[1]>x[2]-->7>10-->False
if x[1]>x[3]-->7>3-->true
change the assumed pos-->x[3]-->3

if x[3]>x[4]-->3>2-->true
assumed position-->x[4]-->2

swap(x[1],x[4])
updated list-->  | 1 | 2 | 10 | 3 | 7 | 
                   0   1   2    3   4


Now, assumed pos-->x[2]
if x[2]>x[3]--->10>3-->true
change assumed pos-->x[3]-->3
if x[3]>x[4]-->3>7--->False

swap(x[2],x[3])
Updated--> | 1 | 2 | 3 | 10 | 7 |
             0   1   2   3    4 

assumed pos--->x[3]--->10
if x[3]>x[4]-->10>7--->true
change assumed position--->x[4]
swap(x[3],x[4])

Updated--> [1,2,3,7,10]

'''

'''
#Ex2

y=[100,2,20,35,40,9,18]

'''

#ex2 iteration wise selection sort
# iteration 1
x=[100,2,20,35,40,9,18]
minp=0
for i in range(1,len(x)):
    if x[minp]>x[i]:
        minp=i
# swap
x[minp],x[0]=x[0],x[minp]
print("First pass->",x)

# iteration 1 o/p-->First pass-> [2, 100, 20, 35, 40, 9, 18]
print()

# iteration 2
minp=1
for i in range(2,len(x)):
    if x[minp]>x[i]:
        minp=i
# swap
x[minp],x[1]=x[1],x[minp]
print("second pass->",x)

# o/p--->second pass-> [2, 9, 20, 35, 40, 100, 18]
print()

# iteration 3
minp=2
for i in range(3,len(x)):
    if x[minp]>x[i]:
        minp=i
# swap
x[minp],x[2]=x[2],x[minp]
print("Third pass->",x)
# o/p-->Third pass-> [2, 9, 18, 35, 40, 100, 20]
print()

# iteration 4
minp=3
for i in range(4,len(x)):
    if x[minp]>x[i]:
        minp=i
# swap
x[minp],x[3]=x[3],x[minp]
print("Fourth pass->",x)
# o/p-->Fourth pass-> [2, 9, 18, 20, 40, 100, 35]
print()

## iteration 5
minp=4
for i in range(5,len(x)):
    if x[minp]>x[i]:
        minp=i
# swap
x[minp],x[4]=x[4],x[minp]
print("Fifth pass->",x)
# o/p--->Fifth pass-> [2, 9, 18, 20, 35, 100, 40]
print()

## iteration 6
minp=5
for i in range(6,len(x)):
    if x[minp]>x[i]:
        minp=i
# swap
x[minp],x[5]=x[5],x[minp]
print("Sixth pass->",x)
# o/p-->Sixth pass-> [2, 9, 18, 20, 35, 40, 100]

print("------------")

#ex3
y=[1000,250,1500,50,33,2,0.5]
for i in range(len(y)):
    minp=i
    for j in range(i+1,len(y)):
        if y[minp]>y[j]:
            minp=j
        y[i],y[minp]=y[minp],y[i]
print(y)
# [0.5, 2, 33, 50, 250, 1000, 1500]
print("--------------------------------")




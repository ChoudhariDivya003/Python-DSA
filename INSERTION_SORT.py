'''
INSERTION SORT
-------------
It is a type of sorting algorithm where the current value 
will get compared with its previous value for soting purpose

It will not work for big dataset...comparisons will be more

Here always we need to compare with backward element
------------------
Time complexity-->
1. best-->o(n)
2. avg-->o(n^2)
3. worst-->0(n^2)
------------------

steps--->
1. consider a list collection to be sorted
2. start passes from 1 because at 0th pass there will be 
   no previous value for comparison

3. check whether i is not equal to zero or not if true then check 
   if current value is less than its previous value

4. If above condition is true then swap the both values and 
   decrement value of i by 1



'''

'''
ex1:
a=[10,3,8,7,1]
  ____________________
 | 10 | 3 | 8 | 7 | 1 |
 |____________________|
  0    1    2   3   4

  always start with a[1] for comparison
  i=1
  a[1]<a[0]-->3<10--->True
  then swap the element(shift the element)

  a[1]---->i=a[i]-1

  updated--> | 3 | 10 | 8 | 7 | 1 |
               0   1    2   3   4
----------------------------------------

Next iteration,
now i=2

now, a[2]<a[1]-->8<10-->True
swap-->a[2],a[1]
i=i-1-->2-1-->i=1

updated--> | 3 | 8 | 10 | 7 | 1 |
             0   1   2    3   4

a[1]<a[0]-->8<3--->false(stop)

updated-->[3,8,10,7,1]
---------------------------

next iteration,
i=3
a[3]<a[2]-->7<10-->True
swap-->a[3],a[2]

[3,8,7,10,1]
 0 1 2  3 4

now,i=i-1-->3-1-->i=2

a[2]<a[1]--<7<8-->true
swap-->a[2],a[1]
i=i-1-->2-1-->i=1

updates list-->
[ 3, 7, 8, 10, 1]
 0   1  2   3  4

 a[1]<a[0]-->7<3-->false-->stop
---------------------------------

 Next iteration,
 i=4
 a[4]<a[3]-->1<10 -->true 
 swap-->a[4],a[3]

 i=i-1-->4-1-->i=3
 updated list --> [3, 7, 8, 1, 10]

 a[3]<a[2]-->1<8-->true
 swap (a[3],a[2])
 updated -->[3, 7, 1, 8, 10]

 i=2
 a[2]<a[1]-->1<7-->true
 swap(a[2],a[1])

 updated-->[3,1,7,8,10]
----------------------------

 next iteration,
 i=1
 a[1]<a[0]-->1<3-->True
 swap-->a[1],a[0]

 Updated
 -->[1,3,7,8,10]

 stop until i value becomes zero

'''

'''
ex2 :
w=[10,13,2,14,5,7,1]

i=1
a[1]<a[0]-->13<10-->False stop

i=2
w[2]<w[1]-->2<13-->true 
swap(w[2],w[1])
[10,2,13,14,5,7,1]

i=i-1
i=1
w[1]<w[0]-->2<10-->true
swap-->w[1],w[0]
i=i-1

[2,10,13,14,5,7,1]
i=0-->stop

Now, i=3
a[3]<a[2]-->14<13-->False
w[3]<w[1]-->14<10 False
stop

[2,10,13,14,5,7,1]
i=4
w[4]<w[3]-->5<14-->true
swap(w[4],w[3])
i=i-1

[2,10,13,5,14,7,1]
 0  1  2 3 4  5 6
i=4-1=3

w[3]<w[2]-->5<13-->True
swap(w[3],w[2])

[2,10,5,13,14,7,1]

'''




#EX1
x=[7,3,11,5,2,6,1]
for Pass_data in range(1,len(x)):
    i=Pass_data
    while i!=0 and x[i]<x[i-1]:
        x[i],x[i-1]=x[i-1],x[i]
        i=i-1
print("final output data-->",x)
# o/p-->final output data--> [1, 2, 3, 5, 6, 7, 11]
print("------")

#ex2
s=[11,17,5,1,6,0.5]


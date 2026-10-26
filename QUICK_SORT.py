'''
QUICK SORT
-------------

Here we initialize three variables
pivot element-->p
lowest value-->i
highest value-->j

'''

'''#ex1
z=[4,3,2,1]
def Sorted_data(z,low,high):
    p=z[low]
    i=low+1
    j=high
    while i<=j:
        while i<=j and z[i]<p:
            i=i+1
        while i<=j and z[j]>p:
            j=j-1
        if i<=j:
            z[i],z[j]=z[j],z[i]
            i=i+1
            j=j-1
    z[low],z[j]=z[j],z[low]
    return j                        #3   pivot element position
# print(Sorted_data(z,0,len(z)-1))
# print(z)                           #[1, 3, 2, 4]

# before writing this code we need to check the position of the pivot element
def Quick_sort(z,low,high):
    if low>=high:
        return 

    j=Sorted_data(z,low,high)    #3   in previous code we return the j position

    Quick_sort(z,low,j-1)
    Quick_sort(z,j+1,high)
Quick_sort(z,0,len(z)-1)
print(z)

# o/p--->[1, 2, 3, 4]
'''
print()

#ex2
s=[10,56,23,90,111,45,1,23,0.5]
def Sorting(s,low,high):
    p=s[low]
    i=low+1
    j=high
    while i<=j:
        while i<=j and s[i]<p:
            i=i+1
        while i<=j and s[j]>p:
            j=j-1
        if i<=j:
            s[i],s[j]=s[j],s[i]
            i=i+1
            j=j-1
    s[low],s[j]=s[j],s[low]
    return j
# print(Sorting(s,0,len(s)-1))
# print(s)
# 2
# [1, 0.5, 10, 90, 111, 45, 23, 23, 56]

def QuickSort(s,low,high):
    if low>=high:
        return
    j=Sorting(s,low,high)
    QuickSort(s,low,j-1)
    QuickSort(s,j+1,high)
QuickSort(s,0,len(s)-1)
print(s)

# [0.5, 1, 10, 23, 23, 45, 56, 90, 111]
    




    
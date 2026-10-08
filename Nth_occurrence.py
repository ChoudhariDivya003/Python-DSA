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
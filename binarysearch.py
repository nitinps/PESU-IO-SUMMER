numbers=[]
pos=-1
found=0
low=0
high=int(input("Enter length of list: "))
print("Enter numbers: ")
for i in range(0,high):
    k=int(input())
    numbers.append(k)
x=int(input("Enter number you want to search: "))
while low<=high and found==0:
    mid=int((low+high)/2)
    if(numbers[mid]==x):
      pos=mid
      found=1
    elif x<numbers[mid]:
      high=mid-1
    else:
      low=mid+1
if pos==-1:
      print('Not found')
else:
      print('found at position: ',pos)

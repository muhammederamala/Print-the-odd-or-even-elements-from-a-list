from os import lstat


def odd(lst,oddlst):
    for i in range(0,n):
        if(lst[i]%2!=0):
            oddlst.append(lst[i])
    return oddlst

def even(lst,evenlst):
    for i in range (0,n):
        if(lst[i]%2==0):
            evenlst.append(lst[i])
    return evenlst

lst = []
oddlst = []
evenlst = []
n = int(input("enter number of elements \n"))
print("\nenter the elements \n")
for i in range(0,n):
    num = int(input())
    lst.append(num)
print(lst)

choice = input(" Do you want to print odd elements or even elements \n (odd/even) \n")
if choice == 'odd':
    odd(lst,oddlst)
    print(oddlst)
elif choice=='even':
    even(lst,evenlst)
    print(evenlst)
else:
    print("invalid choice")

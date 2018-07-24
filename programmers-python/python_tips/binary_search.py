import bisect
mylist = [1, 2, 3, 7, 9, 11, 33]
num = 2
print(mylist[bisect.bisect(mylist, num)-1] == num)
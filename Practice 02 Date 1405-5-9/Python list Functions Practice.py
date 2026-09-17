# Python list Functions Practice 

'''
Method     	Description

-append()   Adds an element at the end of the list
-clear()	    Removes all the elements from the list
-copy()	    Returns a copy of the list
-count()	    Returns the number of elements with the specified value
-extend()	Add the elements of a list (or any iterable), to the end of the current list
-index()	    Returns the index of the first element with the specified value
-insert()	Adds an element at the specified position
-pop()	    Removes the element at the specified position
-remove()	Removes the first item with the specified value
-reverse()	Reverses the order of the list
-sort()	    Sorts the list

'''

#append()   Example:
a=[1,2,3,4,5,6]
print(a.append(7))


#clear()   Example:
b=[1,2,3,4,5,6,7]
print(b.clear())


#copy()   Example:
c=[1,2,3,4,5,6,7]
print(c.copy())


#count()   Example:
d=[1,2,3,1,4,5,2,6,7,1,8,2,2]
print(d.count(2))



#extend()   Example:
e=[1,2,3,4,5,]
f=[6,7,8,9,10]
e.extend(f)
print(e)


#index()   Example:
g=[7,8,9,10,11,12,13,14,15]
print(g.index(13))


#insert()   Example:
h=[1,2,3,4,5,6,8,9,10]
h.insert(6, 7)
print(h)


#pop()   Example:
i=[10,11,12,13,14,15,16]
print(i.pop())
print(i)


#remove()   Example:
j=[10,11,12,13,14,15,16]
print(j.remove(13))
print(j)
    


#reverse()   Example:
k=[7,8,9,10,11,12,13]
print(k.reverse())


#sort()   Example:
l=[3,1,4,2,6,7,13,9]
print(l.sort())
print(l)


#THE END .... Yours Sincerely .... HFAzar.















# set_elements = {} #If we don't put value in the {}, it will take it as a dictionary rather than set.
set_elements = {"Sajad","Farhad",1, 2, 3, 4, 5, False, "Haseena",3,5,7.67}
print(set_elements)

farh = set() #Empty Set
print(type(farh))
print("Values of Set are :")
for i in set_elements:
    print(i)

#Methods in Set:
s1 = {1,3,4,8,7}
s2 = {2,3,5,6,9,8}
print("Union of the two sets is :",s1.union(s2))

print("Symmetric difference",s1.symmetric_difference(s2)) #elements which ar enot common..
print("Difference ",s1.difference(s2)) #values which are present in the original set but not in the second set.
print("Difference Update : ",s1.difference_update(s2))
print("Disjoin ",s1.isdisjoint(s2))
print("Superset ",s1.issuperset(s2))
print("Subset ",s1.issubset(s2))
print("Removing Element",s1.pop())
print(s1)
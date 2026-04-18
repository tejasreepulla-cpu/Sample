#Sets:collection of unordered elements,won't allow duplicates,mutable data type
# set_1={1,}
# print(set_1)
# print(type(set_1))

# set_1=set()
# print(set_1)
# print(type(set_1))

# sample={3,5.7,"python",(1,2,3)}
# print(sample)

# set methods:
# 1.add:used to add an element to the set
# sample={3,5.7,"python",(1,2,3)}
# sample.add(97)
# print(sample)

# 2.clear:removes all elements from the set
# sample={3,5.7,"python",(1,2,3)}
# sample.clear()
# print(sample)

# 3.copy:returns shallow copy of the original set
# sample={3,5.7,"python",(1,2,3)}
# sample_1=sample.copy()
# print(sample_1)
# sample_1.clear()
# print(sample_1)
# print(sample)

# 4.pop:used to remove random element from the set
# sample={3,5.7,"python",(1,2,3)}
# sample.pop()
# print(sample)

# sample={3,5.7,"python",(1,2,3)}
# obj=sample.pop()
# print(obj)

# sample={3,5.7,"python",(1,2,3)}
# sample.pop(3)
# print(sample) #Type error

# 5.remove:used to remove particular element from the set
# sample={3,5.7,"python",(1,2,3)}
# sample.remove("python")
# print(sample)

# sample={3,5.7,"python",(1,2,3)}
# obj=sample.remove("python")
# print(obj)

# 6.update:used to add one set elements to the another set
# sample={3,5.7,"python",(1,2,3)}
# sample_1={5,"sita"}
# sample.update(sample_1)
# print(sample)

# sample={3,5.7,"python",(1,2,3)}
# sample_1={5,"sita",5.7}
# sample.update(sample_1)
# print(sample)

# Set operations:
# 1.union:returns a set containing the union of sets
# set_1={1,2,3,4,5}
# set_2={4,5,6,7,8}
# print(set_1.union(set_2))

# set_1={1,2,3,4,5}
# set_2={4,5,6,7,8}
# set_3=set_1.union(set_2)
# print(set_3)

# 2.intersection:returns common elements
# set_1={1,2,3,4,5}
# set_2={4,5,6,7,8}
# print(set_1.intersection(set_2))

# set_1={1,2,3,4,5}
# set_2={4,5,6,7,8}
# set_3=set_1.intersection(set_2)
# print(set_3)

# 3.symmetric_difference:returns non common elements
# set_1={1,2,3,4,5}
# set_2={4,5,6,7,8}
# set_3=set_1.symmetric_difference(set_2)
# print(set_3)

# set_1={1,2,3,4,5}
# set_2={4,5,6,7,8}
# print(set_1.symmetric_difference(set_2))

# 4.difference:compares both the sets and return non common elements from set A
# set_1={1,2,3,4,5}
# set_2={4,5,6,7,8}
# print(set_1.difference(set_2))

# set_1={1,2,3,4,5}
# set_2={4,5,6,7,8}
# set_3=set_1.difference(set_2)
# print(set_3)

# 5.isdisjoint:it will check for common elements if t's there return false else true
# set_1={1,2,3,4,5}
# set_2={4,5,6,7,8}
# print(set_1.isdisjoint(set_2))

# set_1={1,2,3,4,5}
# set_2={9,6,7,8}
# print(set_1.isdisjoint(set_2))

# 6.issuperset:
# set_1={1,2,3,4,5}
# set_2={4,5,3}
# print(set_1.issuperset(set_2))

# set_1={1,2,3,4,5}
# set_2={1,2,3,4,5}
# print(set_1.issuperset(set_2))

# set_1={1,2,3,4,5}
# set_2={4,5,3,8}
# print(set_1.issuperset(set_2))

# set_1={1,2,3,4,5}
# set_2={1,2,3,4}
# print(set_1.issuperset(set_2))

# set_1={1,2,3,4,5}
# set_2={1,2,3,4,5,6}
# print(set_1.issuperset(set_2))

# 7.issubset:
# set_1={1,2,3,4,5}
# set_2={1,2,3,4}
# print(set_2.issubset(set_1))

# set_1={1,2,3,4,5}
# set_2={1,2,3,4,8}
# print(set_2.issubset(set_1))

# voter_data={"vasu","kiran","raju","ravi"}
# voter_data_1={"vasu","kiran","ravi"}
# print(voter_data.issuperset(voter_data_1))
# print(voter_data_1.issubset(voter_data))

# voter_data={"vasu","kiran","raju","ravi"}
# voter_data_1={"vasu","kiran","ravi","ramu"}
# print(voter_data.issuperset(voter_data_1))
# print(voter_data.issubset(voter_data_1))
# print(voter_data_1.issuperset(voter_data))

# frozen_set:returns immutable frozen set
# set_1={1,2,3,4,5}
# print(set_1)
# set_1.add("python")
# print(set_1)

# set_1={1,2,3,4,5}
# set_2=frozenset(set_1)
# print(set_2)
# set_2.add('python')
# print(set_2)  #Attribute error

# Task1---->set and frozenset
# union
# set_1={1,2,3,4,5}
# set_2={4,5,6,7,8}
# frozen_set=frozenset(set_2)
# print(set_1.union(frozen_set))

# intersection:
# set_1={1,2,3,4,5}
# set_2={4,5,6,7,8}
# frozen_set=frozenset(set_2)
# print(set_1.intersection(frozen_set))

# symmetric_difference:
# set_1={1,2,3,4,5}
# set_2={4,5,6,7,8}
# frozen_set=frozenset(set_2)
# print(set_1.symmetric_difference(frozen_set))

# difference:
# set_1={1,2,3,4,5}
# set_2={4,5,6,7,8}
# frozen_set=frozenset(set_2)
# print(set_1.difference(frozen_set))

# isdisjoint:
# set_1={1,2,3,4,5}
# set_2={4,5,6,7,8}
# frozen_set=frozenset(set_2)
# print(set_1.isdisjoint(frozen_set))

# issuperset:
# set_1={1,2,3,4,5}
# set_2={4,5}
# frozen_set=frozenset(set_2)
# print(set_1.issuperset(frozen_set))

# set_1={1,2,3,4,5}
# set_2={4,5,6,7,8}
# frozen_set=frozenset(set_2)
# print(set_1.issuperset(frozen_set))

# issubset:
# set_1={1,2,3,4,5}
# set_2={4,5,6,7,8}
# frozen_set=frozenset(set_2)
# print(frozen_set.issubset(set_1))

# set_1={1,2,3,4,5}
# set_2={4,5}
# frozen_set=frozenset(set_2)
# print(frozen_set.issubset(set_1))

# Task2---->frozenset and frozenset
# union
# set_1={1,2,3,4,5}
# set_2={4,5,6,7,8}
# frozen_set_1=frozenset(set_1)
# frozen_set_2=frozenset(set_2)
# print(frozen_set_1.union(frozen_set_2))

#intersection:
# set_1={1,2,3,4,5}
# set_2={4,5,6,7,8}
# frozen_set_1=frozenset(set_1)
# frozen_set_2=frozenset(set_2)
# print(frozen_set_1.intersection(frozen_set_2))

# symmetric_difference:
# set_1={1,2,3,4,5}
# set_2={4,5,6,7,8}
# frozen_set_1=frozenset(set_1)
# frozen_set_2=frozenset(set_2)
# print(frozen_set_1.symmetric_difference(frozen_set_2))

# difference
# set_1={1,2,3,4,5}
# set_2={4,5,6,7,8}
# frozen_set_1=frozenset(set_1)
# frozen_set_2=frozenset(set_2)
# print(frozen_set_1.difference(frozen_set_2))

# isdisjoint:
# set_1={1,2,3,4,5}
# set_2={4,5,6,7,8}
# frozen_set_1=frozenset(set_1)
# frozen_set_2=frozenset(set_2)
# print(frozen_set_1.isdisjoint(frozen_set_2))

# set_1={1,2,3,4,5}
# set_2={6,7,8}
# frozen_set_1=frozenset(set_1)
# frozen_set_2=frozenset(set_2)
# print(frozen_set_1.isdisjoint(frozen_set_2))

# issuperset:
# set_1={1,2,3,4,5}
# set_2={1,2,4}
# frozen_set_1=frozenset(set_1)
# frozen_set_2=frozenset(set_2)
# print(frozen_set_1.issuperset(frozen_set_2))

# set_1={1,2,3,4,5}
# set_2={1,2,4,8}
# frozen_set_1=frozenset(set_1)
# frozen_set_2=frozenset(set_2)
# print(frozen_set_1.issuperset(frozen_set_2))

# issubset:
# set_1={1,2,3,4,5}
# set_2={1,2,4,8}
# frozen_set_1=frozenset(set_1)
# frozen_set_2=frozenset(set_2)
# print(frozen_set_2.issubset(frozen_set_1))

# set_1={1,2,3,4,5}
# set_2={1,2,4}
# frozen_set_1=frozenset(set_1)
# frozen_set_2=frozenset(set_2)
# print(frozen_set_2.issubset(frozen_set_1))

# Task3---->frozenset and set
# union
# set_1={1,2,3,4,5}
# set_2={4,5,6,7,8}
# frozen_set_1=frozenset(set_1)
# print(frozen_set_1.union(set_2))

#Tuple:collection of elements,immutable datatype,ordered,()
# tuple_1=()
# print(tuple_1)
# print(type(tuple_1))

# tuple_1=tuple()
# print(tuple_1)
# print(type(tuple_1))

# tuple_1=(1,2,3.5,"python",(1,2,3),{1,2,3},{1:"name"})
# print(tuple_1)
# print(len(tuple_1))
# print(tuple_1[4])
# print(tuple_1[len(tuple_1)-1])
# print(tuple_1[3:7])
# print(tuple_1[-3:-1])

# a=5
# b=10
# print(a)
# print(b)

# a=5,2.5,"python",(1,2,3)
# print(a)

# a=b=c="sample"
# print(a)
# print(b)
# print(c)

# a,b,c=10,20,30
# print(a)
# print(b)
# print(c)

# a=5
# b=10
# a,b=b,a
# print(a)
# print(b)

# Tuple methods:
# 1.count:
# tuple_1=('python',1,2,3,1,3,1)
# print(tuple_1.count(1))

# 2.all:
# tuple_1=('python',1,2,3,1,3,1)
# print(all(tuple_1))

# tuple_1=('python',1,2,3,1,3,0,1)
# print(all(tuple_1))

# tuple_1=('python',1,2,3,False,1,3,1)
# print(all(tuple_1))

# tuple_1=(1,2,3)
# tuple_2=('a',2,"123")
# print(tuple_1+tuple_2)

# tuple_1=(1,2,3)
# print(tuple_1*2)
# print(2 in tuple_1)








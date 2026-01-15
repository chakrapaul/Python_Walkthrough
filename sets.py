# s={1,2,2,3,4}
# print(s)

# # paul={}
# # print(type(paul))

# paul=set() #rightway to do empty set

# info = {"carla", 19, False , 45.43}
# # print(info)

# for i in info:
#     print(i,end=" ")

# s1={1,2,5,6}
# s2={3,6,7}
# print(s1.union(s2))
# print(s1.intersection(s2))
# s1.update(s2)
# print(s1,s2)

cities={'tokyo','madrid','berlin','delhi'}
cities2={'tokyo','seoul','kabul','madrid'}
cities3 = cities.symmetric_difference(cities2)
print(cities3)

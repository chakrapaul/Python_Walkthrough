# l=[1,2,3,4]
# print(l)
# l.append(7)
# print(l)

l=[11,23,1,42,94,1,1,1]
print(l)
l.sort()
print(l.index(1))
print(l.count(1))

m=l.copy()
m[0] = [0]
print(l)

l.insert(2,9)

print(l)
n=[1,2,3]
l.extend(n)
print(l)
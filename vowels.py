text=str(input("Enter your text:"))

vowels = ['a','e','i','o','u']
count=0

for ch in text:
    if ch in vowels:
        count+=1

print(count)
# for i in text:
#     for j in vowels:
#         if(i==j):
#             count = count + 1
# print(count)
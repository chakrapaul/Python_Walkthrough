s="anagram"
t="nagaram"


# for ch in s:
#     print(ch,end=" ")

for ch in s:
    for tx in t:
        if(ch==tx):
            print(True)
        else:
            print(False)
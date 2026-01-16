def unique_char(s):
    count={}

    for ch in s:
        count[ch] = count.get(ch,0)+1

    count_first_val = list(count.values())[0]

    return count_first_val

s=input()
print(unique_char(s))
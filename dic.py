# dic={"haryy":"human being",
#      "spoon":"object"}

# dic={344:"harry",
#      24:"paul",
#      35:"neha"}
# print(dic)

info={"name":"harry","age":19,"eligible":True}
print(info)
print(info["name"])
print(info.get('name'))

print(info.keys())
print(info.values())

print(info.items())

for key,value in info.items():
    print(f"The value corresponding to the key {key} is {value}")
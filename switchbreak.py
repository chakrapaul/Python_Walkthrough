# for i in range(12):
#     if(i==10):
#         break
#     print("5 x",i+1,"=" , 5 * (i+1))
# print("out of the loop")

for i in range(12):
    if(i==10):
        print("skip the iteration")
        continue
    print("5 x",i,"=",5*i)
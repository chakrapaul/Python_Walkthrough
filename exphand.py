# n=input("Enter you number:")
# print(f"Multplication table of {n} is:")

# try:
#     for i in range(1,11):
#         print(f"{n} x {i} = {int(n)*i}")
# except Exception as e:
#     print("Theres an error occured",e)


# print("Print some important lines")
# print("End of the code")

# try:
#     n=int(input())
#     a=[6,3]
#     print(a[n])
# except ValueError:
#     print("val error")
# except IndexError:
#     print("idx error")

try:
    l=[1,2,3,4]
    i=int(input("Enter the idx you want:"))
    print(l[i])
except:
    print("Error occured")

finally:
    print("Im always executed")
 


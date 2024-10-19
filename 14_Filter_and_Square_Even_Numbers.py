inlst = input("Enter a list: ")
lst = []
for i in inlst:
  lst.append(int(i))

res = [num**2 for num in lst if num%2 == 0]
print(res)
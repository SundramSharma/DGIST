inlst = input("Enter a list: ")
lst = []
for i in inlst:
  lst.append(int(i))

lst.sort()
maxx = max(lst)
nlst = [i for i in lst if i != maxx]
print(max(nlst))

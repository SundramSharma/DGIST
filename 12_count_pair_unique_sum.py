inlst = input("Enter a list: ")
lst = []
for i in inlst:
  lst.append(int(i))

tar = int(input("Enter Target Sum: "))
ans = []

for i in lst:
  for j in lst:
    if i+j == tar:
      pair = (i,j)
      reversepair = (j,i)
      if (pair and reversepair) not in ans:
        ans.append(pair)
      else:
        pass
print(len(ans))
print(ans)
    